# README

## Top-level Schemas

*   [delete-certificate input](./set-certificate-input.md "Delete a let's encrypt certificate") – `http://schema.nethserver.org/traefik/set-certificate-input.json`

*   [delete-certificate output](./delete-certificate-output.md "Just a boolean value") – `http://schema.nethserver.org/traefik/delete-certificate-output.json`

*   [delete-route input](./delete-route-input.md "Delete a HTTP route") – `http://schema.nethserver.org/traefik/delete-route-input.json`

*   [get-acme-server output](./get-acme-eserver-output.md "Get the URL of the ACME server") – `http://schema.nethserver.org/traefik/get-acme-eserver-output.json`

*   [get-certificate input](./get-certificate-input.md "Get status of a requested certificate") – `http://schema.nethserver.org/traefik/get-certificate-input.json`

*   [get-certificate output](./get-certificate-output.md "Status of a requested certificate") – `http://schema.nethserver.org/traefik/get-certificate-output.json`

*   [get-route input](./get-route-input.md "Get a configured route") – `http://schema.nethserver.org/traefik/get-route-input.json`

*   [get-route output](./get-route-output.md "Show the configuration of a  HTTP route") – `http://schema.nethserver.org/traefik/get-route-output.json`

*   [list-certificates input](./list-certificates-output.md "Get a list of requested certificates") – `http://schema.nethserver.org/traefik/list-certificates-output.json`

*   [list-certificates output](./list-certificates-output-1.md "Return a list of requested certificates fqdn") – `http://schema.nethserver.org/samba/list-certificates-output.json`

*   [list-routes input](./list-routes-output.md "Get a list of configured routes") – `http://schema.nethserver.org/traefik/list-routes-output.json`

*   [list-routes output](./list-routes-output-1.md "Return a list of configured routes") – `http://schema.nethserver.org/samba/list-routes-output.json`

*   [set-certificate output](./set-certificate-output.md "State of the requested certificate") – `http://schema.nethserver.org/traefik/set-certificate-output.json`

*   [set-route input](./set-route-input.md "Reserve a HTTP route") – `http://schema.nethserver.org/traefik/set-route-input.json`

## Other Schemas

### Objects

*   [A certificate expanded](./list-certificates-output-1-items-oneof-a-certificate-expanded.md) – `http://schema.nethserver.org/samba/list-certificates-output.json#/items/oneOf/0`

*   [A route expanded](./list-routes-output-1-items-oneof-a-route-expanded.md) – `http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0`

*   [Headers list](./get-route-output-properties-headers-list.md "Headers to add or remove from an HTTP's request or response") – `http://schema.nethserver.org/traefik/get-route-output.json#/properties/headers`

*   [Headers list](./set-route-input-properties-headers-list.md "Headers to add or remove from an HTTP's request or response") – `http://schema.nethserver.org/traefik/set-route-input.json#/properties/headers`

*   [Untitled object in get-route output](./get-route-output-properties-headers-list-properties-request.md) – `http://schema.nethserver.org/traefik/get-route-output.json#/properties/headers/properties/request`

*   [Untitled object in get-route output](./get-route-output-properties-headers-list-properties-response.md) – `http://schema.nethserver.org/traefik/get-route-output.json#/properties/headers/properties/response`

*   [Untitled object in list-certificates input](./list-certificates-output-oneof-0.md) – `http://schema.nethserver.org/traefik/list-certificates-output.json#/oneOf/0`

*   [Untitled object in list-routes input](./list-routes-output-oneof-0.md) – `http://schema.nethserver.org/traefik/list-routes-output.json#/oneOf/0`

*   [Untitled object in set-route input](./set-route-input-properties-headers-list-properties-request.md) – `http://schema.nethserver.org/traefik/set-route-input.json#/properties/headers/properties/request`

*   [Untitled object in set-route input](./set-route-input-properties-headers-list-properties-response.md) – `http://schema.nethserver.org/traefik/set-route-input.json#/properties/headers/properties/response`

### Arrays



## Version Note

The schemas linked above follow the JSON Schema Spec version: `http://json-schema.org/draft-07/schema#`
