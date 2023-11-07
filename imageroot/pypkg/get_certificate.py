#!/usr/bin/env python3

#
# Copyright (C) 2023 Nethesis S.r.l.
# SPDX-License-Identifier: GPL-3.0-or-later
#

import json
import os
import agent
import urllib.request

def get_certificate(data):
    try:
        name = data.get('name','')
        fqdn = data.get('fqdn','')
        certificate = {}
        api_path = os.environ["API_PATH"]
        moduleid = os.environ["MODULE_ID"]

        # we retrieve route and certificate for list-certificates action
        if name != "":
            with urllib.request.urlopen(f'http://127.0.0.1/{api_path}/api/http/routers/{name}') as res:
                traefik_https_route = json.load(res)

        # we retrieve cert from fqdn for backward compatibility (it is an acme certificate)
        elif fqdn != "":
             with urllib.request.urlopen(f'http://127.0.0.1/{api_path}/api/http/routers/certificate-{fqdn}@file') as res:
                 traefik_https_route = json.load(res)

        # Check if the route is ready to use
        if traefik_https_route['status'] == 'disabled':
            return {}

        certificate['fqdn'] = traefik_https_route['tls']['domains'][0]['main']
        # either from internal or route (type could be also custom cert)
        certificate['type'] = 'internal' if traefik_https_route['name'].startswith('certificate-') else 'route'
        certificate['obtained'] = False

        # Open the certificates storage file
        with open(f'/home/{moduleid}/.local/share/containers/storage/volumes/traefik-acme/_data/acme.json') as f:
            acme_storage = json.load(f)

        resolver = traefik_https_route['tls']['certResolver']
        certificates = acme_storage[resolver].get('Certificates')

        # Check if the certificate is present in the storage
        for cert in certificates if certificates else []:
            if cert['domain']['main'] == certificate['fqdn']:
                certificate['obtained'] = True
                break

    except urllib.error.HTTPError as e:
        if e.code == 404:
            # If the certificate is not found, return an empty JSON object
            pass

    except urllib.error.URLError as e:
        raise Exception(f'Error reaching traefik daemon: {e.reason}') from e

    except json.decoder.JSONDecodeError:
            # The acme storage is empty or corrupted, return the certificate as requested but not obtained
            pass

    return certificate
