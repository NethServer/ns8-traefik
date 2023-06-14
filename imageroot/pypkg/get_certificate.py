#!/usr/bin/env python3

#
# Copyright (C) 2023 Nethesis S.r.l.
# http://www.nethesis.it - nethserver@nethesis.it
#
# This script is part of NethServer.
#
# NethServer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License,
# or any later version.
#
# NethServer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NethServer.  If not, see COPYING.
#

import json
import os
import agent
import urllib.request

def get_certificate(data):
    try:
        fqdn = data['fqdn']
        certificate = {}
        api_path = os.environ["API_PATH"]
        moduleid = os.environ["MODULE_ID"]

        # Get the certificate route from the API
        with urllib.request.urlopen(f'http://127.0.0.1/{api_path}/api/http/routers/certificate-{fqdn}@redis') as res:
            traefik_https_route = json.load(res)

        # Check if the route is ready to use
        if traefik_https_route['status'] == 'disabled':
            return {}

        certificate['fqdn'] = fqdn
        certificate['type'] = 'internal'

        certificate['obtained'] = False

        # Open the certificates storage file
        with open(f'/home/{moduleid}/.local/share/containers/storage/volumes/traefik-acme/_data/acme.json') as f:
            acme_storage = json.load(f)

        resolver = traefik_https_route['tls']['certResolver']
        certificates = acme_storage[resolver].get('Certificates')

        # Check if the certificate is present in the storage
        for cert in certificates if certificates else []:
            if cert['domain']['main'] == data['fqdn']:
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
