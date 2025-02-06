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

def read_default_cert_names():
    """Return the list of host names configured in the
    defaultGeneratedCert section."""
    with open('configs/_default_cert.yml', 'r') as fp:
        conf = yaml.safe_load(fp)
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
    with open('acme/acme.json', 'r') as fp:
        acmejson = json.load(fp)
    for ocert in acmejson['acmeServer']["Certificates"] or []:
        if ocert["domain"]["main"] == name or name in ocert["domain"].get("sans", []):
            return True
    return False

def has_acmejson_cert(main, sans=[]):
    """Return True if a certificate matching main and sans is found among
    acme.json Certificates."""
    with open('acme/acme.json', 'r') as fp:
        acmejson = json.load(fp)
    for ocert in acmejson['acmeServer']["Certificates"] or []:
        if ocert["domain"]["main"] == main and set(ocert["domain"].get("sans", [])) == set(sans):
            return True
    return False

def wait_acmejson_sync(timeout=120, interval=2.1, names=[]):
    """Poll the acme.json file every 'interval' seconds, until a
    certificate matching 'names' appears, or timeout seconds are elapsed.
    If list 'names' is given, it is expected to have subject at index 0
    and sans in the rest of the list. If not, this function waits for the
    default certificate."""
    if not names:
        # Wait for the default certificate.
        names = read_default_cert_names()
    elapsed = 0.0
    while elapsed < timeout:
        time.sleep(interval)
        elapsed += interval
        if has_acmejson_cert(names[0], names[1:]):
            return True
    return False

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
