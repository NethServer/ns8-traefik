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
  "host": "127.0.0.1",
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
The action takes 1 parameter:
- `instance`: the instance name

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

- `fqdn` (string): the name of the TLS certificate
- `type` (one of `internal` or `custom`): use `internal` for Let's Encrypt
  certificates, `custom` for uploaded certificates.

The effects depend on the certificate type:

- `internal` If the certificate was obtained from Let's Encrypt using the
  ACME protocol, the `fqdn` is removed from Traefik's
  `defaultGeneratedCert` configuration. The certificate will **not**
  actually be removed from Traefik's `acme.json` certificate storage. Even
  if unused, it will be renewed as long as the conditions permit.
- `custom` If the certificate was uploaded, it is erased from disk along
  with its private key and removed from Traefik's TLS configuration.

Example:

```
api-cli run module/traefik1/delete-certificate --data '{"fqdn":"myhost.example.com","type":"internal"}'
```

## list-certificates

This action returns a list of requested certificate, the list is an JSON array, and if no certificate was requested, an
empty array is returned.

The action takes 1 optional parameter:
- `expand_list`: if set to `true` the list will be expanded with all certificate's details

Example:
```
api-cli run module/traefik1/list-certificates
```

Output (brief format):
```json
["myhost.example.com"]
```

Example list expanded:
```
api-cli run module/traefik1/list-certificates --data '{"expand_list": true}'
```

Output (expanded format):
```json
[{"fqdn": "myhost.example.com", "obtained": true, "type": "internal"}]
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
