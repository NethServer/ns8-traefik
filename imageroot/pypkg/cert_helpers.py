#
# Copyright (C) 2025 Nethesis S.r.l.
# SPDX-License-Identifier: GPL-3.0-or-later
#

import agent
import sys
import os
import yaml
import json
import time
import glob
import subprocess
import datetime
import select
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def extract_certified_names(cert_data : bytearray) -> set:
    """
    Extract the subject common name and subject alternative names (SAN)
    from a PEM certificate.

    :param cert_data: Certificate, PEM-encoded.
    :return: A set of certified host names.
    """
    cert = x509.load_pem_x509_certificate(cert_data, default_backend())
    hostnames = set()
    # Extract Common Name (CN) from the Subject field
    subject = cert.subject
    cn = subject.get_attributes_for_oid(x509.NameOID.COMMON_NAME)
    if cn:
        hostnames.add(cn[0].value)
    # Extract Subject Alternative Names (SANs), if any
    try:
        ext = cert.extensions.get_extension_for_oid(x509.ExtensionOID.SUBJECT_ALTERNATIVE_NAME)
        san = ext.value
        hostnames.update(san.get_values_for_type(x509.DNSName))
    except x509.ExtensionNotFound:
        pass
    return hostnames

def read_default_cert_names():
    """Return the list of host names configured in the
    defaultGeneratedCert section."""
    conf = parse_yaml_config('configs/_default_cert.yml')
    try:
        main = [conf['tls']['stores']['default']['defaultGeneratedCert']['domain']['main']]
    except KeyError:
        main = []
    try:
        sans = conf['tls']['stores']['default']['defaultGeneratedCert']['domain']['sans']
    except KeyError:
        sans = []
    return main + sans

def read_custom_cert_names():
    """Return the list of main hostnames provided by custom/uploaded
    certificates."""
    main_hostnames = list()
    for cert_path in glob.glob("custom_certificates/*.crt"):
        hostname = cert_path.removeprefix("custom_certificates/").removesuffix(".crt")
        main_hostnames.append(hostname)
    return main_hostnames

def remove_custom_cert(name):
    """Remove the custom/uploaded certificate files and its Traefik
    configuration."""
    for path in [
        f"custom_certificates/{name}.crt",
        f"custom_certificates/{name}.key",
        f"configs/certificate_{name}.yml",
    ]:
        try:
            os.unlink(path)
        except FileNotFoundError:
            pass
    rdb = agent.redis_connect(privileged=True)
    rdb.delete(f'module/{os.environ["MODULE_ID"]}/certificate/{name}')

def has_acmejson_name(name):
    """Return True if name is found among acme.json Certificates."""
    try:
        with open('acme/acme.json', 'r') as fp:
            acmejson = json.load(fp)
        for ocert in acmejson['acmeServer']["Certificates"] or []:
            if ocert["domain"]["main"] == name or name in ocert["domain"].get("sans", []):
                return True
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        pass
    return False

def has_acmejson_cert(main, sans=[]):
    """Return True if a certificate matching main and sans is found among
    acme.json Certificates."""
    try:
        with open('acme/acme.json', 'r') as fp:
            acmejson = json.load(fp)
        for ocert in acmejson['acmeServer']["Certificates"] or []:
            if ocert["domain"]["main"] == main and set(ocert["domain"].get("sans", [])) == set(sans):
                return True
        return False
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        pass
    return False

def wait_acmejson_sync(timeout=120, interval=2.1, names=[]):
    """Poll the acme.json file every 'interval' seconds, until a
    certificate matching 'names' appears, an error occurs, or timeout
    seconds are elapsed. If list 'names' is given, it is expected to have
    subject at index 0 and sans in the rest of the list. If not, this
    function waits for the default certificate."""
    if not names:
        # Wait for the default certificate.
        names = read_default_cert_names()
    if not names:
        return True # Consider as obtained, if no names are set.
    elapsed = 0.0
    tstart = datetime.datetime.now(datetime.UTC)
    logcli_cmd = [
        "logcli",
        "query",
        "--tail",
        "--limit=1",
        "--from=" + tstart.isoformat(),
        "--timezone=Local", # use system timezone for output
        "--quiet",
        "--no-labels",
        '{module_id=~"traefik.+"} | json | line_format "{{.MESSAGE}}"' + \
        '| logfmt | providerName="acmeServer.acme" and error!=""' + \
        '| line_format "{{.error}}"',
    ]
    obtained = False
    with subprocess.Popen(logcli_cmd, stdout=subprocess.PIPE, text=True) as logcli_proc:
        fdmon = logcli_proc.stdout.fileno()
        while True:
            time.sleep(interval)
            elapsed += interval
            if elapsed >= timeout:
                print(agent.SD_ERR + f"Timeout after about {timeout} seconds. Certificate not obtained for {names}.", file=sys.stderr)
                obtained = False
                break
            if has_acmejson_cert(names[0], names[1:]):
                obtained = True # certificate obtained successfully!
                break
            read_fds, _, _ = select.select([fdmon], [], [], 0) # 0 = non blocking
            if read_fds:
                obtained = False
                break # got some error messages from logcli.
        logcli_proc.terminate()
    return obtained

def add_default_certificate_name(main, sans=[]):
    """Add 'main' and 'sans' to the current certificate configuration. If
    the current certificate is already configured, 'main' is added as SAN,
    otherwise it is used to initialize a new defaultGeneratedCert
    configuration."""
    tlsconf = parse_yaml_config("configs/_default_cert.yml")
    defstore = tlsconf['tls']['stores']['default']
    if 'defaultCertificate' in defstore:
        # Remove self-signed cert config.
        del defstore['defaultCertificate']
        # Initialize config for ACME.
        defstore['defaultGeneratedCert'] = {
            'resolver': 'acmeServer',
            'domain': {
                'main': main,
                'sans': sans,
            },
        }
    elif 'defaultGeneratedCert' in defstore:
        # ACME config already exists. Merge names from request into SANs of
        # defaultGeneratedCert.
        sans = set(defstore['defaultGeneratedCert']['domain']['sans'])
        sans.add(main)
        sans.update(set(sans))
        sans.discard(defstore['defaultGeneratedCert']['domain']['main'])
        defstore['defaultGeneratedCert']['domain']['sans'] = list(sans)
    write_yaml_config(tlsconf, 'configs/_default_cert.yml')

def remove_default_certificate_name(name):
    """Remove 'name' from defaultGeneratedCert configuration. If 'name'
    matches the certificate main name, the first item of sans becomes the
    certificate main name. If there are no more sans available, the
    default self-signed certificate configuration is applied."""
    tlsconf = parse_yaml_config("configs/_default_cert.yml")
    defstore = tlsconf['tls']['stores']['default']
    main = defstore['defaultGeneratedCert']['domain']['main']
    names = defstore['defaultGeneratedCert']['domain'].get('sans', [])
    if name == main:
        if len(names) == 0:
            reset_selfsigned_certificate()
        elif len(names) == 1:
            defstore['defaultGeneratedCert']['domain']['main'] = names[0]
            defstore['defaultGeneratedCert']['domain']['sans'] = []
            write_yaml_config(tlsconf, 'configs/_default_cert.yml')
        else:
            defstore['defaultGeneratedCert']['domain']['main'] = names[0]
            defstore['defaultGeneratedCert']['domain']['sans'] = names[1:]
            write_yaml_config(tlsconf, 'configs/_default_cert.yml')
    else:
        defstore['defaultGeneratedCert']['domain']['sans'].remove(name)
        write_yaml_config(tlsconf, 'configs/_default_cert.yml')

def reset_selfsigned_certificate():
    """Replaces the default certificate configuration, restoring the
    config for the self-signed one."""
    tlsconf = {
        "tls": {
            "stores": {
                "default": {
                    "defaultCertificate": {
                        "certFile": "/etc/traefik/selfsigned.crt",
                        "keyFile": "/etc/traefik/selfsigned.key",
                    }
                }
            }
        }
    }
    write_yaml_config(tlsconf, 'configs/_default_cert.yml')

def write_yaml_config(conf, path):
    """Safely write a configuration file."""
    with open(path + '.tmp', 'w') as fp:
        fp.write(yaml.safe_dump(conf, default_flow_style=False, sort_keys=False, allow_unicode=True))
    os.rename(path + '.tmp', path)

def parse_yaml_config(path):
    """Parse a YAML configuration file."""
    with open(path, 'r') as fp:
        conf = yaml.safe_load(fp)
    return conf

def traefik_last_acme_error_since(tstart):
    """Get the last Traefik error related to ACME from Loki.

    :param tstart: a ISO8601 string with TZ offset
    :return: string
    """
    try:
        acme_error = subprocess.check_output([
            "logcli",
            "query",
            "--limit=1",
            "--from=" + tstart.isoformat(),
            "--timezone=Local", # use system timezone for output
            "--quiet",
            "--no-labels",
            '{module_id=~"traefik.+"} | json | line_format "{{.MESSAGE}}"' + \
            '| logfmt | providerName="acmeServer.acme" and error!=""' + \
            '| line_format "{{.error}}"',
        ], timeout=15, text=True)
    except subprocess.TimeoutExpired as ex:
        acme_error = 'traefik_last_acme_error_since(): logcli timeout - ' + str(ex)
    except subprocess.CalledProcessError as ex:
        acme_error = 'traefik_last_acme_error_since(): logcli error - ' + str(ex)
    return acme_error

def validate_certificate_names(main, sans=[], timeout=30):
    """Issue a certificate request to ACME server and return if it has
    been obtained or not."""
    # Check if we already have the same certificate in acme.json:
    if has_acmejson_cert(main, sans):
        return True
    routerconf = {
        "http": {
            "services": {
                "_validation000": {
                    "loadBalancer": {
                        "servers": ["ping@internal"]
                    }
                }
            },
            "routers": {
                "_validation000": {
                    "rule": f"Host(`{main}`) && Path(`/_validation000`)",
                    "priority": 100001,
                    "service": "_validation000",
                    "entryPoints": ["https"],
                    "tls": {
                        "domains": [{"main": main, "sans": sans}],
                        "certResolver": "acmeServer",
                    }
                }
            }
        }
    }
    write_yaml_config(routerconf, "configs/_validation000.yml")
    obtained = wait_acmejson_sync(timeout=timeout, interval=1.1, names=[main] + sans)
    os.unlink("configs/_validation000.yml")
    return obtained
