#!/usr/bin/env python3

#
# Copyright (C) 2022 Nethesis S.r.l.
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
import re
import urllib.request

# Try to parse the stdin as JSON.
# If parsing fails, output everything to stderr

def get_route(data, ignore_error = False):

    module = data['instance']
    route = {}
    middlewares = []
    api_path = os.environ["API_PATH"]

    agent_id = os.environ["AGENT_ID"]
    try:
        # Get the http route from the API
        with urllib.request.urlopen(f'http://127.0.0.1/{api_path}/api/http/routers/{module}-https@file') as res:
            traefik_https_route = json.load(res)
        # Get the https route from the API
        with urllib.request.urlopen(f'http://127.0.0.1/{api_path}/api/http/routers/{module}-http@file') as res:
            traefik_http_route = json.load(res)

        # Check if the route is ready to use
        if traefik_http_route['status'] == 'disabled' or traefik_https_route['status'] == 'disabled':
            return {}

        service_name = traefik_https_route['service']
        # Get the service from the API
        with urllib.request.urlopen(f'http://127.0.0.1/{api_path}/api/http/services/{service_name}@file') as res:
            service = json.load(res)

        route['instance'] = data['instance']

        # Extract the hostname from the rule of the router
        r =  re.match(r"^.*Host\(`(.*?)`\).*$", traefik_https_route['rule'])
        if r:
            route['host'] = r.group(1)

        # Extract the path from the rule of the router
        r =  re.match(r"^.*Path\(`(.*?)`\).*$", traefik_https_route['rule'])
        if r:
            route['path'] = r.group(1)

        # Get the target URL from the service
        route['url'] = service['loadBalancer']['servers'][0]['url']

        # Check if the certificate is retrieved automatically
        route['lets_encrypt'] = True if traefik_https_route['tls'].get("certResolver") else False

        # Strip @file suffix  from middlware names
        for mid in traefik_http_route.get("middlewares",[]):
            middlewares.append(mid[0:mid.index('@')])

        # Check if redirect http to https is enabled
        route['http2https'] = True if middlewares and "http2https-redirectscheme" in middlewares else False

        # Check if the path is striped from the request
        if route.get("path"):
            route['strip_prefix'] = True if middlewares and f'{module}-stripprefix' in middlewares else False

        # Check if the route was created manually
        route['user_created'] = os.path.isfile(f'manual_flags/{module}')

        if middlewares and f'{module}-headers' in middlewares:
            try:
                with urllib.request.urlopen(f'http://127.0.0.1/{api_path}/api/http/middlewares/{module}-headers@file') as res:
                    route['headers'] = {}
                    headers_middleware = json.load(res)

                    if 'customRequestHeaders' in headers_middleware['headers']:
                        route['headers']['request'] = headers_middleware['headers']['customRequestHeaders']
                    if 'customResponseHeaders' in headers_middleware['headers']:
                        route['headers']['response'] = headers_middleware['headers']['customResponseHeaders']

            except urllib.error.HTTPError as e:
                raise Exception(f'Error reaching traefik daemon (middlewares): {e.reason}')

        if middlewares and f'{module}-auth' in middlewares:
            try:
                with urllib.request.urlopen(f'http://127.0.0.1/{api_path}/api/http/middlewares/{module}-auth@file') as res:
                    auth_middleware = json.load(res)
            except urllib.error.HTTPError as e:
                raise Exception(f'Error reaching traefik daemon (middlewares): {e.reason}')

            route['forward_auth'] = {
                'address': auth_middleware['forwardAuth']['address'],
            }
            try:
                route['forward_auth']['skip_tls_verify'] = auth_middleware['forwardAuth']['tls']['insecureSkipVerify']
            except KeyError:
                # The TLS skip certificate verification flag may be missing completely: ignore.
                pass

    except urllib.error.HTTPError as e:
        if e.code == 404:
            # If the route is not found, return an empty JSON object
            pass

    except urllib.error.URLError as e:
        if ignore_error:
            return route
        else:
            raise Exception(f'Error reaching traefik daemon: {e.reason}')

    return route
