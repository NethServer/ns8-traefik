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

def read_default_cert_names():
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

def has_acmejson_name(name):
    """Return True if name is found among acme.json Certificates."""
    with open('acme/acme.json', 'r') as fp:
        acmejson = json.load(fp)
    for ocert in acmejson['acmeServer']["Certificates"]:
        if ocert["domain"]["main"] == name or name in ocert["domain"].get("sans", []):
            return True
    return False

def has_acmejson_cert(main, sans=[]):
    """Return True if a certificate matching main and sans is found among
    acme.json Certificates."""
    with open('acme/acme.json', 'r') as fp:
        acmejson = json.load(fp)
    for ocert in acmejson['acmeServer']["Certificates"]:
        if ocert["domain"]["main"] == main and set(ocert["domain"].get("sans", [])) == set(sans):
            return True
    return False

def wait_acmejson_sync(names=[], timeout=120, interval=2.1):
    if not names:
        names = read_default_cert_names()
    elapsed = 0.0
    while elapsed < timeout:
        if has_acmejson_cert(names[0], names[1:]):
            return True
        time.sleep(interval)
        elapsed += interval
    return False

def add_default_certificate_name(main, sans=[]):
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

def write_yaml_config(conf, path):
    with open(path + '.tmp', 'w') as fp:
        fp.write(yaml.safe_dump(conf, default_flow_style=False, sort_keys=False, allow_unicode=True))
    os.rename(path + '.tmp', path)

def parse_yaml_config(path):
    with open(path, 'r') as fp:
        conf = yaml.safe_load(fp)
    return conf
