# Traefik

This module implements a proxy for web applications using [Traefik](https://doc.traefik.io/traefik/).

The following table summarizes the available actions and the role(s)
required to invoke them. For simplicity, the builtin `owner` and `reader`
roles are omitted.

| Action      | Roles    |
|-------------|----------|
| `set-route` | routeadm, fulladm |
| `get-route` | routeadm, fulladm |
| `delete-route` | routeadm, fulladm |
| `list-routes` | routeadm, fulladm |
| `set-certificate` | certadm, fulladm |
| `get-certificate` | certadm, fulladm |
| `delete-certificate` | certadm, fulladm |
| `list-certificates` | certadm, fulladm |
| `set-acme-server` | |
| `get-acme-server` | |
| `upload-certificate` | |

## set-route

This action creates HTTP routes based on a combination of host and path, is possible to define three type
of rules:

* only `host`: These rules will capture all the requests directed to a specific host
* `host` and `path`: These rules will capture all the requests directed to a specific combination of host and path prefix
* only `path`: These rules will capture all the requests directed to a specific path prefix, regardless of the host.

This is the priority of the rules type evaluation (top-down):

1. `host` and `path`
1. only `host`
1. only `path`

### Parameters

- `instance`: the instance name, which is unique inside the cluster, mandatory
- `skip_cert_verify`: do not verify self signed certificate (boolean)
- `url`: the backend target URL, mandatory
- `host`: a fully qualified domain name as virtual host
- `path`: a path prefix, the matching evaluation will be performed whit and without the trailing slash, eg `/foo` will match `/foo` and `/foo/*`, also `/foo/` will match `/foo` and `/foo/*`
- `lets_encrypt`: can be `true` or `false`, if set to `true` request a valid Let's Encrypt certificate, mandatory
- `http2https` can be `true` or `false`, if set to `true` HTTP will be redirect to HTTPS, mandatory
- `strip_prefix`: can be `true` or `false`, if set to `true` the prefix of the requested path will be stripped from the original request before sending it to the downstream server.
- `user_created`: can be `true` or `false`, if set to `true` the route will be marked as manually created.
- `headers`: list of headers to add/remove from an HTTP request/response before reaching the service/client, to remove the the header an empty value must be set. Example:
```json
      "headers": {
        "request": {
          "X-foo-add": "foo",
          "X-bar-remove": ""
        },
        "response": {
          "X-bar-add": "bar",
          "X-foo-remove": ""
        }
      }
```
- `forward_auth`: prop to configure the forwardAuth config, to remove the the header an empty value must be set. Example:
```json
      "forward_auth": {
        "address": "http://127.0.0.1:9311/api/module/test/http-basic/test-action",
        "skip_tls_verify": true
      }
```
- `lets_encrypt_cleanup` (optional): when the HTTP route Let'Encrypt certificate is no longer
  needed (i.e. `lets_encrypt` is set to `false`), this optional boolean attribute
  can trigger the cleanup of the internal certificate store (`acme.json`
  file) with immediate Traefik restart.

- `lets_encrypt_check` (optional): if this optional attribute is `true`, the action
  fails immediately with a validation error if a Let's Encrypt certificate
  cannot be obtained. The full ACME error message is returned in the
  `details` attribute.

### Examples

Only `host`
```
api-cli run set-route --agent module/traefik1 --data - <<EOF
{
  "instance": "module1",
  "url": "http://127.0.0.1:2000",
  "host": "module.example.org",
  "lets_encrypt": true,
  "http2https": true,
  "skip_cert_verify": false
}
EOF
```

`host` and `path`
```
api-cli run set-route --agent module/traefik1 --data - <<EOF
{
  "instance": "module1",
  "url": "http://127.0.0.1:2000",
  "host": "module.example.org",
  "path": "/foo",
  "lets_encrypt": true,
  "http2https": true,
  "skip_cert_verify": false
}
EOF
```
Only `path`

```
api-cli run set-route --agent module/traefik1 --data - <<EOF
{
  "instance": "module1",
  "url": "http://127.0.0.1:2000",
  "path": "/foo",
  "lets_encrypt": true,
  "http2https": true,
  "skip_cert_verify": false
}
EOF
```

With `forward_auth`
```
api-cli run set-route --agent module/traefik1 --data - <<EOF
{
  "instance": "module1",
  "url": "http://127.0.0.1/add-module1",
  "host": "module.example.org",
  "lets_encrypt": false,
  "http2https": false,
  "skip_cert_verify": false,
  "forward_auth": {
      "address": "http://127.0.0.1:9311/api/module/module1/http-basic/add-module1",
      "skip_tls_verify": true
  }
}
EOF
```

With `forward_auth` and `auth_response_headers`
```
api-cli run set-route --agent module/traefik1 --data - <<EOF
{
  "instance": "module1",
  "url": "http://127.0.0.1/add-module1",
  "host": "module.example.org",
  "lets_encrypt": false,
  "http2https": false,
  "skip_cert_verify": false,
  "forward_auth": {
      "address": "http://127.0.0.1:9311/api/module/module1/http-basic/add-module1",
      "skip_tls_verify": true,
      "auth_response_headers": [
        "X-Auth-User",
        "X-Auth-Group"
      ]
  }
}
EOF
```
## get-route

This action get an existing route. It returns a JSON object that describes the route configuration, if the
route is not found an empty JSON object is returned.
The action takes 1 parameter:
- `instance`: the instance name

Example:
```
api-cli run get-route --agent module/traefik1 --data '{"instance": "module1"}'
```

Output:
```json
{"instance": "module3", "host": "module.example.org", "path": "/foo", "url": "http://127.0.0.1:2000", "lets_encrypt": true, "http2https": true, "strip_prefix": false}
```

## delete-route

This action delets an existing route. It can be used when removing a module instance.
The action takes the following parameters:
- `instance`: the instance name
- `lets_encrypt_cleanup` (optional): if a Let's Encrypt certificate was
  obtained trigger the cleanup of the internal certificate store
  (`acme.json` file) with immediate Traefik restart.


Example:
```
api-cli run delete-route --agent module/traefik1 --data '{"instance": "module1"}'
```

## list-routes

This action returns a list of configured routes, the list is an JSON array, and if no route is configured, an
empty array is returned.

The action takes 1 optional parameter:
- `expand_list`: if set to `true` the list will be expanded with all route's details

Example:
```
api-cli run list-routes --agent module/traefik1
```

Output:
```json
["module1", "module2", "module3"]
```

Example list expanded:
```
api-cli run list-routes --agent module/traefik1 --data '{"expand_list": true}'
```

Output:
```json
[
  {
    "instance": "module1",
    "host": "module.example.org",
    "url": "http://127.0.0.1:2000",
    "lets_encrypt": true,
    "http2https": true,
    "skip_cert_verify": false
  },
  {
    "instance": "module2",
    "host": "module.example.org",
    "path": "/foo",
    "url": "http://127.0.0.1:2000",
    "lets_encrypt": true,
    "http2https": true,
    "strip_prefix": false,
    "skip_cert_verify": true

  },
  {
    "instance": "module3",
    "path": "/foo",
    "url": "http://127.0.0.1:2000",
    "lets_encrypt": false,
    "http2https": true,
    "strip_prefix": false,
    "skip_cert_verify": false

  }
]
```

## set-default-certificate

Use this action to obtain and enable a new default certificate in Traefik.
The certificate will cover the requested domain names and can optionally
merge with the existing default certificate names. The action validates
requested names against existing HTTP routes to avoid conflicts.

### Input

* `names` (array of strings, required): List of domain names to include in
  the default certificate.

  * Can include FQDNs (e.g., `www.nethserver.org`) or wildcard domains (e.g., `*.nethserver.com`).
  * Must contain at least one name.

* `check_routes` (boolean, optional, default: true): If true, the action
  will verify that the requested names are not already used by existing
  HTTP routes.

* `sync_timeout` (integer, optional, default: 30): Maximum number of
  seconds to wait for the ACME certificate response.

* `merge` (boolean, optional, default: false): If true, the resulting
  certificate names will be the union of the current default certificate
  names with the requested names.

### Examples

Set a new default certificate for specific names:

```json
{
    "names": [
        "www.nethserver.org",
        "*.nethserver.com"
    ]
}
```

Merge new names with the existing default certificate:

```json
{
    "names": [
        "api.nethserver.org"
    ],
    "merge": true
}
```

Set a new default certificate and wait up to 60 seconds for the ACME certificate:

```json
{
    "names": [
        "secure.nethserver.org"
    ],
    "sync_timeout": 60
}
```

### Notes

* Changing the default certificate does not trigger a Traefik restart.
* Ensure that domain names provided are valid and properly resolvable for
  ACME validation.
* During the validation period Traefik may temporarily present a self-signed
  certificate on HTTP routes that are not based on the Host name.
* If the certificate cannot be obtained, Traefik will keep the previous
  default certificate and a validation error is returned. Full ACME
  protocol error is in the `details` attribute.


## set-certificate

Run this action to request a new default certificate for Traefik. The
action parameters are:

- `fqdn` (string): the name of the requested certificate
- `sync_timeout` (integer, default `30`): the maximum number of seconds to
  wait for the certificate to be obtained

If ACME challenge requirements are met, the new certificate will be valid
for the given `fqdn` and any other names configured by previous action
calls. See also <https://letsencrypt.org/docs/challenge-types/>. If not,
the previous configuration is retained.

Example:

```
api-cli run module/traefik1/set-certificate --data '{"fqdn":"myhost.example.com"}'
```

## get-certificate

Run this action to get the status of requested a Let's Encrypt certificate

The action takes 1 parameter:
- `fqdn`: the fqdn of the requested certificate

Example:
```
api-cli run module/traefik1/get-certificate --data '{"fqdn":"myhost.example.com"}'
```

Output:
```
{"fqdn": "myhost.example.com", "obtained": true, "type": "internal"}
```

## delete-certificate

This action deletes a TLS certificate from Traefik's configuration. Its
parameters are:

- `type` (one of `internal` or `custom`): use `internal` for Let's Encrypt
  certificates, `custom` for uploaded certificates.
- `serial` (string): the serial number of an intenal certificate
- `path` (string): the file path of a custom certificate

The effects depend on the certificate type:

- `internal` If the certificate was obtained from Let's Encrypt using the
  ACME protocol, the `serial` is removed from Traefik's `acme.json` file
  and Traefik is immediately restarted.
- `custom` If the certificate was uploaded, the matching `path` is erased
  from disk along with its relative private key and Traefik's
  configuration.

Example:

```
api-cli run module/traefik1/delete-certificate --data '{"serial":"3836656052452775035741651062981017961514023","type":"internal"}'
```

## list-certificates-v2

This action returns the detailed attributes of TLS certificates known to
Traefik. Refer to the action `validate-output.json` schema for the
attribute descriptions.

Example:
```
api-cli run module/traefik1/list-certificates-v2
```

Output:
```json
{
  "certificates": [
    {
      "names": [
        "dokuwiki1.dp.nethserver.net"
      ],
      "subject": "dokuwiki1.dp.nethserver.net",
      "issuer": "CN=(STAGING) Tenuous Tomato R13,O=(STAGING) Let's Encrypt,C=US",
      "serial": "3856185763134404048717648492547484375729159",
      "valid_to": "2025-12-03T06:42:34+00:00",
      "valid_from": "2025-09-04T06:42:35+00:00",
      "validity": "valid",
      "type": "internal",
      "automatic": true
    },
    {
      "names": [
        "piler1.dp.nethserver.net"
      ],
      "subject": "piler1.dp.nethserver.net",
      "issuer": "CN=(STAGING) Riddling Rhubarb R12,O=(STAGING) Let's Encrypt,C=US",
      "serial": "3875501012854752351612754224168371968359414",
      "valid_to": "2025-12-03T06:42:46+00:00",
      "valid_from": "2025-09-04T06:42:47+00:00",
      "validity": "valid",
      "type": "internal"
    },
    {
      "names": [
        "mail.dp.nethserver.net"
      ],
      "subject": "mail.dp.nethserver.net",
      "issuer": "CN=Custom Intermediate CA,O=TestIntermediateCA,L=TestCity,ST=TestState,C=XX",
      "serial": "603545327999770137768033575467090432240151056165",
      "valid_to": "2026-02-07T14:19:38+00:00",
      "valid_from": "2025-02-07T14:19:38+00:00",
      "path": "custom_certificates/mail.dp.nethserver.net.crt",
      "validity": "valid",
      "type": "custom"
    }
  ]
}
```

## set-acme-server

This action allows setting an ACME server that traefik will use to request the HTTPS certificates.
The default ACME server used is Let's Encrypt.

The action parameters are:
- `url`: ACME server URL (required)
- `email`: Email address for Let's Encrypt account and notifications (optional)
- `challenge`: one of `HTTP-01`, `TLS-ALPN-01` (optional)

Example:
```
api-cli run set-acme-server  --agent module/traefik1 --data '{"url":"https://acme-staging-v02.api.letsencrypt.org/directory"}'
```

## get-acme-server

This action returns the current configured ACME server.

The action takes no parameter.

Example:
```
api-cli run get-acme-server  --agent module/traefik1
```

Output:
```
{"url": "https://acme-staging-v02.api.letsencrypt.org/directory", "email":"", "challenge":"HTTP-01"}
```

## upload-certificate

Action allowing the upload of custom certificates to Traefik.

Action takes two parameters:
- `certFile`: Certificate (or a chain of certificates) to upload, base64 encoded.
- `keyfile`: Key used to generate the certificate, also base64 encoded.

Example:
```
api-cli run module/traefik1/upload-certificate --data '{"certFile":"LS0tLS1CRUdJTiBSU0EgU...","keyFile":"LS0tLS1CRUdJTiBSU0EgU..."}'
```

The action verifies whether the certificate is valid. The type of
verification is controlled by the following environment settings:

- `UPLOAD_CERTIFICATE_VERIFY_TYPE=chain` (default) – The certificate must
  be valid according to the host CA certificate store. The uploaded file
  may include an intermediate CA certificate appended to the certificate
  itself.

- `UPLOAD_CERTIFICATE_VERIFY_TYPE=selfsign` – The certificate can be
  self-signed or include a full chain of certificates.

- `UPLOAD_CERTIFICATE_VERIFY_TYPE=none` – Certificate verification is
  skipped. Use this value to disable expiration date checks.

## set-trusted-proxies

This action configures trusted proxies for Traefik, allowing it to correctly identify
and log the original public IP address of incoming requests, rather than the proxy's IP.
This is useful when Traefik is behind a reverse proxy or load balancer.

### Parameters

- `proxies`: List of trusted proxy IP addresses (e.g., `["192.168.100.1"]`)
- `depth`: Number of proxy hops to trust (integer)

### Example

```
api-cli run module/traefik1/set-trusted-proxies --data '{"depth": 1, "proxies": ["192.168.100.1"]}'
```

After setting trusted proxies, the correct public IP will appear in logs:

```
Aug 20 10:51:11 ns8-leader traefik[1916]: xxx.xxx.xxx.xxx - - [20/Aug/2025:08:51:11 +0000] "POST /api/v4/channels/members/me/view HTTP/1.1" 200 42 "-" "-" 221 "mattermost1-https@file" "http://127.0.0.1:20001" 1ms
```

---

## get-trusted-proxies

This action returns the current trusted proxy configuration.

### Example

```
api-cli run module/traefik1/get-trusted-proxies
```

Output:
```json
{"proxies": ["192.168.100.1"], "depth": 1}