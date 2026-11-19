# README

## Top-level Schemas

* [delete-certificate input](./set-certificate-input.md "Delete one or more TLS certificates matching the input") – `http://schema.nethserver.org/traefik/set-certificate-input.json`

* [delete-certificate output](./delete-certificate-output.md "JSON schema matching anything") – `http://schema.nethserver.org/traefik/delete-certificate-output.json`

* [delete-route input](./delete-route-input.md "Delete a HTTP route") – `http://schema.nethserver.org/traefik/delete-route-input.json`

* [get-acme-server output](./get-acme-eserver-output.md "Get ACME configuration") – `http://schema.nethserver.org/traefik/get-acme-eserver-output.json`

* [get-certificate input](./get-certificate-input.md "Get certificates matching the fqdn parameter") – `http://schema.nethserver.org/traefik/get-certificate-input.json`

* [get-certificate output](./get-certificate-output.md "Get one or more certificates for the given FQDN") – `http://schema.nethserver.org/traefik/get-certificate-output.json`

* [get-route input](./get-route-input.md "Get a configured route") – `http://schema.nethserver.org/traefik/get-route-input.json`

* [get-route output](./get-route-output.md "Show the configuration of a  HTTP route") – `http://schema.nethserver.org/traefik/get-route-output.json`

* [list-certificates input](./list-certificates-input.md "Placeholder, see bug NethServer/dev#7058") – `http://schema.nethserver.org/traefik/list-certificates-input.json`

* [list-certificates-v2 output](./list-certificates-v2-output.md "List the TLS certificates obtained by ACME or manually uploaded, with detailed attributes") – `http://schema.nethserver.org/traefik/list-certificates-v2-output.json`

* [list-routes input](./list-routes-output.md "Get a list of configured routes") – `http://schema.nethserver.org/traefik/list-routes-output.json`

* [list-routes output](./list-routes-output-1.md "Return a list of configured routes") – `http://schema.nethserver.org/samba/list-routes-output.json`

* [set-acme-server input](./set-acme-server-input.md "Set ACME configuration") – `http://schema.nethserver.org/traefik/set-acme-server-input.json`

* [set-certificate output](./set-certificate-output.md) – `http://schema.nethserver.org/traefik/set-certificate-output.json`

* [set-default-certificate input](./set-default-certificate.md "Change Traefik's configuration to obtain and enable a new default certificate with the required names") – `http://schema.nethserver.org/traefik/set-default-certificate.json`

* [set-route input](./set-route-input.md "Reserve a HTTP route") – `http://schema.nethserver.org/traefik/set-route-input.json`

* [set-trusted-proxies input](./set-trusted-proxies-input.md "Set the IP addresses that are trusted as front-end proxies") – `http://schema.nethserver.org/traefik/set-trusted-proxies-input.json`

* [set-trusted-proxies output](./set-trusted-proxies-output.md "Get the IP addresses that are trusted as front-end proxies") – `http://schema.nethserver.org/traefik/set-trusted-proxies-output.json`

* [upload-certificate input](./upload-certificate-input.md "Upload a certificate to be used by Traefik") – `http://schema.nethserver.org/traefik/upload-certificate-input.json`

## Other Schemas

### Objects

* [A route expanded](./list-routes-output-1-items-oneof-a-route-expanded.md) – `http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0`

* [Forward Auth configuration](./get-route-output-properties-forward-auth-configuration.md "If set enabled forwardAuth prop on traefik") – `http://schema.nethserver.org/traefik/get-route-output.json#/properties/forward_auth`

* [Forward Auth configuration](./list-routes-output-1-items-oneof-a-route-expanded-properties-forward-auth-configuration.md "If set enabled forwardAuth prop on traefik") – `http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/forward_auth`

* [Headers list](./get-route-output-properties-headers-list.md "Headers to add or remove from an HTTP's request or response") – `http://schema.nethserver.org/traefik/get-route-output.json#/properties/headers`

* [Headers list](./set-route-input-properties-headers-list.md "Headers to add or remove from an HTTP's request or response") – `http://schema.nethserver.org/traefik/set-route-input.json#/properties/headers`

* [Headers list](./list-routes-output-1-items-oneof-a-route-expanded-properties-headers-list.md "Headers to add or remove from an HTTP's request or response") – `http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/headers`

* [Untitled object in get-certificate output](./get-certificate-output-properties-certificates-items.md) – `http://schema.nethserver.org/traefik/get-certificate-output.json#/properties/certificates/items`

* [Untitled object in get-route output](./get-route-output-properties-headers-list-properties-request.md) – `http://schema.nethserver.org/traefik/get-route-output.json#/properties/headers/properties/request`

* [Untitled object in get-route output](./get-route-output-properties-headers-list-properties-response.md) – `http://schema.nethserver.org/traefik/get-route-output.json#/properties/headers/properties/response`

* [Untitled object in list-certificates-v2 output](./list-certificates-v2-output-defs-tlscert.md "TLS certificate object") – `http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert`

* [Untitled object in list-routes input](./list-routes-output-oneof-0.md) – `http://schema.nethserver.org/traefik/list-routes-output.json#/oneOf/0`

* [Untitled object in list-routes output](./list-routes-output-1-items-oneof-a-route-expanded-properties-headers-list-properties-request.md) – `http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/headers/properties/request`

* [Untitled object in list-routes output](./list-routes-output-1-items-oneof-a-route-expanded-properties-headers-list-properties-response.md) – `http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/headers/properties/response`

* [Untitled object in set-route input](./set-route-input-properties-headers-list-properties-request.md) – `http://schema.nethserver.org/traefik/set-route-input.json#/properties/headers/properties/request`

* [Untitled object in set-route input](./set-route-input-properties-headers-list-properties-response.md) – `http://schema.nethserver.org/traefik/set-route-input.json#/properties/headers/properties/response`

### Arrays

* [Auth response headers](./set-route-input-properties-forward-auth-configuration-properties-auth-response-headers.md "A list of headers to be copied from backend response to the client") – `http://schema.nethserver.org/traefik/set-route-input.json#/properties/forward_auth/properties/auth_response_headers`

* [Untitled array in get-certificate output](./get-certificate-output-properties-certificates.md "List of certificates for FQDN, ordered by relevance (high first)") – `http://schema.nethserver.org/traefik/get-certificate-output.json#/properties/certificates`

* [Untitled array in get-route output](./get-route-output-properties-ip_allowlist.md "List of allowed client ip addresses, in CIDR format") – `http://schema.nethserver.org/traefik/get-route-output.json#/properties/ip_allowlist`

* [Untitled array in list-certificates-v2 output](./list-certificates-v2-output-properties-certificates.md) – `http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/properties/certificates`

* [Untitled array in list-certificates-v2 output](./list-certificates-v2-output-defs-tlscert-properties-names.md) – `http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/names`

* [Untitled array in set-default-certificate input](./set-default-certificate-properties-names.md) – `http://schema.nethserver.org/traefik/set-default-certificate.json#/properties/names`

* [Untitled array in set-route input](./set-route-input-properties-ip_allowlist.md "List of allowed client ip addresses, in CIDR format") – `http://schema.nethserver.org/traefik/set-route-input.json#/properties/ip_allowlist`

* [Untitled array in set-trusted-proxies input](./set-trusted-proxies-input-properties-proxies.md) – `http://schema.nethserver.org/traefik/set-trusted-proxies-input.json#/properties/proxies`

* [Untitled array in set-trusted-proxies output](./set-trusted-proxies-output-properties-proxies.md) – `http://schema.nethserver.org/traefik/set-trusted-proxies-output.json#/properties/proxies`

## Version Note

The schemas linked above follow the JSON Schema Spec version: `http://json-schema.org/draft-07/schema#`
