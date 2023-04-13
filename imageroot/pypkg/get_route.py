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
import agent
import re
import urllib.request

# Try to parse the stdin as JSON.
# If parsing fails, output everything to stderr

def get_route(data):

    module = data['instance']
    route = {}
    api_path = os.environ["API_PATH"]

    agent_id = os.environ["AGENT_ID"]
    try:
        # Get the http route from the API
        with urllib.request.urlopen(f'http://127.0.0.1/{api_path}/api/http/routers/{module}-https@redis') as res:
            traefik_https_route = json.load(res)
        # Get the https route from the API
        with urllib.request.urlopen(f'http://127.0.0.1/{api_path}/api/http/routers/{module}-http@redis') as res:
            traefik_http_route = json.load(res)

        # Check if the route is ready to use
        if traefik_http_route['status'] == 'disabled' or traefik_https_route['status'] == 'disabled':
            return {}

        service_name = traefik_https_route['service']
        # Get the service from the API
        with urllib.request.urlopen(f'http://127.0.0.1/{api_path}/api/http/services/{service_name}@redis') as res:
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

        middlewares = traefik_http_route.get("middlewares")

        # Check if redirect http to https is enabled
        route['http2https'] = True if middlewares and "http2https-redirectscheme@redis" in middlewares else False

        # Check if the path is striped from the request
        if route.get("path"):
            route['strip_prefix'] = True if middlewares and f'{module}-stripprefix@redis' in middlewares else False

        # Check if the route was created manually
        rdb = agent.redis_connect(privileged=True)
        route['user_created'] = rdb.sismember(f'{agent_id}/user_created_routes', data["instance"])

        if middlewares and f'{module}-headers@file' in middlewares:
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
        
        if middlewares and f'{module}-auth@redis' in middlewares:
            try:
                with urllib.request.urlopen(f'http://127.0.0.1/{api_path}/api/http/middlewares/{module}-auth@redis') as res:
                    route['forward_auth'] = {}
                    auth_middleware = json.load(res)

                    route['forward_auth']['address'] = auth_middleware['forwardAuth']['address']
                    route['forward_auth']['skip_tls_verify'] = auth_middleware['forwardAuth']['tls']['insecureSkipVerify']

            except urllib.error.HTTPError as e:
                raise Exception(f'Error reaching traefik daemon (middlewares): {e.reason}')

    except urllib.error.HTTPError as e:
        if e.code == 404:
            # If the route is not found, return an empty JSON object
            pass

    except urllib.error.URLError as e:
        raise Exception(f'Error reaching traefik daemon: {e.reason}')

    return route
