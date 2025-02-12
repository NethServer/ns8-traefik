# README

## Top-level Schemas

* [delete-certificate input](./set-certificate-input.md "Delete a let's encrypt certificate") – `http://schema.nethserver.org/traefik/set-certificate-input.json`

* [delete-certificate output](./delete-certificate-output.md "Just a boolean value") – `http://schema.nethserver.org/traefik/delete-certificate-output.json`

* [get-acme-server output](./get-acme-eserver-output.md "Get the URL of the ACME server") – `http://schema.nethserver.org/traefik/get-acme-eserver-output.json`

* [get-certificate input](./get-certificate-input.md "Get status of a requested certificate") – `http://schema.nethserver.org/traefik/get-certificate-input.json`

* [get-certificate output](./get-certificate-output.md "Status of a requested certificate") – `http://schema.nethserver.org/traefik/get-certificate-output.json`

* [get-route input](./get-route-input.md "Get a configured route") – `http://schema.nethserver.org/traefik/get-route-input.json`

* [get-route output](./get-route-output.md "Show the configuration of a  HTTP route") – `http://schema.nethserver.org/traefik/get-route-output.json`

* [list-certificates output](./list-certificates-output.md "Return a list of requested certificates fqdn") – `http://schema.nethserver.org/traefik/list-certificates-output.json`

* [list-routes input](./list-routes-output.md "Get a list of configured routes") – `http://schema.nethserver.org/traefik/list-routes-output.json`

* [list-routes output](./list-routes-output-1.md "Return a list of configured routes") – `http://schema.nethserver.org/samba/list-routes-output.json`

* [set-acme-server input](./delete-route-input.md "Set the URL of the ACME server") – `http://schema.nethserver.org/traefik/delete-route-input.json`

* [set-certificate output](./set-certificate-output.md "State of the requested certificate") – `http://schema.nethserver.org/traefik/set-certificate-output.json`

* [set-route input](./set-route-input.md "Reserve a HTTP route") – `http://schema.nethserver.org/traefik/set-route-input.json`

* [set-trusted-proxies input](./set-trusted-proxies-input.md "Set the IP addresses that are trusted as front-end proxies") – `http://schema.nethserver.org/traefik/set-trusted-proxies-input.json`

* [set-trusted-proxies output](./set-trusted-proxies-output.md "Get the IP addresses that are trusted as front-end proxies") – `http://schema.nethserver.org/traefik/set-trusted-proxies-output.json`

* [upload-certificate input](./upload-certificate-input.md "Upload a certificate to be used by Traefik") – `http://schema.nethserver.org/traefik/upload-certificate-input.json`

## Other Schemas

### Objects

* [A route expanded](./list-routes-output-1-items-oneof-a-route-expanded.md) – `http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0`

* [Forward Auth configuration](./get-route-output-properties-forward-auth-configuration.md "If set enabled forwardAuth prop on traefik") – `http://schema.nethserver.org/traefik/get-route-output.json#/properties/forward_auth`

* [Forward Auth configuration](./set-route-input-properties-forward-auth-configuration.md "If set enabled forwardAuth prop on traefik") – `http://schema.nethserver.org/traefik/set-route-input.json#/properties/forward_auth`

* [Forward Auth configuration](./list-routes-output-1-items-oneof-a-route-expanded-properties-forward-auth-configuration.md "If set enabled forwardAuth prop on traefik") – `http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/forward_auth`

* [Headers list](./get-route-output-properties-headers-list.md "Headers to add or remove from an HTTP's request or response") – `http://schema.nethserver.org/traefik/get-route-output.json#/properties/headers`

* [Headers list](./set-route-input-properties-headers-list.md "Headers to add or remove from an HTTP's request or response") – `http://schema.nethserver.org/traefik/set-route-input.json#/properties/headers`

* [Headers list](./list-routes-output-1-items-oneof-a-route-expanded-properties-headers-list.md "Headers to add or remove from an HTTP's request or response") – `http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/headers`

* [Untitled object in get-certificate output](./get-certificate-output-oneof-0.md) – `http://schema.nethserver.org/traefik/get-certificate-output.json#/oneOf/0`

* [Untitled object in get-certificate output](./get-certificate-output-oneof-1.md) – `http://schema.nethserver.org/traefik/get-certificate-output.json#/oneOf/1`

* [Untitled object in get-route output](./get-route-output-properties-headers-list-properties-request.md) – `http://schema.nethserver.org/traefik/get-route-output.json#/properties/headers/properties/request`

* [Untitled object in get-route output](./get-route-output-properties-headers-list-properties-response.md) – `http://schema.nethserver.org/traefik/get-route-output.json#/properties/headers/properties/response`

* [Untitled object in list-certificates output](./list-certificates-output-anyof-1-items.md) – `http://schema.nethserver.org/traefik/list-certificates-output.json#/anyOf/1/items`

* [Untitled object in list-routes input](./list-routes-output-oneof-0.md) – `http://schema.nethserver.org/traefik/list-routes-output.json#/oneOf/0`

* [Untitled object in list-routes output](./list-routes-output-1-items-oneof-a-route-expanded-properties-headers-list-properties-request.md) – `http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/headers/properties/request`

* [Untitled object in list-routes output](./list-routes-output-1-items-oneof-a-route-expanded-properties-headers-list-properties-response.md) – `http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/headers/properties/response`

* [Untitled object in set-route input](./set-route-input-properties-headers-list-properties-request.md) – `http://schema.nethserver.org/traefik/set-route-input.json#/properties/headers/properties/request`

* [Untitled object in set-route input](./set-route-input-properties-headers-list-properties-response.md) – `http://schema.nethserver.org/traefik/set-route-input.json#/properties/headers/properties/response`

### Arrays

* [Untitled array in get-route output](./get-route-output-properties-ip_allowlist.md "List of allowed client ip addresses, in CIDR format") – `http://schema.nethserver.org/traefik/get-route-output.json#/properties/ip_allowlist`

* [Untitled array in set-route input](./set-route-input-properties-ip_allowlist.md "List of allowed client ip addresses, in CIDR format") – `http://schema.nethserver.org/traefik/set-route-input.json#/properties/ip_allowlist`

* [Untitled array in set-trusted-proxies input](./set-trusted-proxies-input-properties-proxies.md) – `http://schema.nethserver.org/traefik/set-trusted-proxies-input.json#/properties/proxies`

* [Untitled array in set-trusted-proxies output](./set-trusted-proxies-output-properties-proxies.md) – `http://schema.nethserver.org/traefik/set-trusted-proxies-output.json#/properties/proxies`

## Version Note

The schemas linked above follow the JSON Schema Spec version: `http://json-schema.org/draft-07/schema#`
