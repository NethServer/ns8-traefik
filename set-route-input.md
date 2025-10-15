# set-route input Schema

```txt
http://schema.nethserver.org/traefik/set-route-input.json
```

Reserve a HTTP route

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [set-route-input.json](traefik/set-route-input.json "open original schema") |

## set-route input Type

`object` ([set-route input](set-route-input.md))

## set-route input Examples

```json
{
  "instance": "module1",
  "url": "http://127.0.0.0:2000",
  "host": "module.example.org",
  "lets_encrypt": true,
  "http2https": true
}
```

```json
{
  "instance": "module1",
  "url": "http://127.0.0.0:2000",
  "host": "module.example.org",
  "path": null,
  "lets_encrypt": true,
  "http2https": true
}
```

```json
{
  "instance": "module2",
  "url": "http://127.0.0.0:2000",
  "host": "module.example.org",
  "path": "/foo",
  "lets_encrypt": true,
  "http2https": true
}
```

```json
{
  "instance": "module3",
  "url": "http://127.0.0.0:2000",
  "path": "/foo",
  "lets_encrypt": true,
  "http2https": true
}
```

```json
{
  "instance": "module3",
  "url": "http://127.0.0.0:2000",
  "path": "/foo",
  "host": null,
  "lets_encrypt": true,
  "http2https": true
}
```

```json
{
  "instance": "wants-slash",
  "url": "http://127.0.0.0:9311",
  "path": "/foo",
  "lets_encrypt": false,
  "http2https": true,
  "slash_redirect": true
}
```

```json
{
  "instance": "module3",
  "url": "http://127.0.0.0:2000",
  "path": "/foo",
  "lets_encrypt": true,
  "http2https": true,
  "ip_allowlist": [
    "192.168.13.0/24",
    "10.12.21.3"
  ]
}
```

```json
{
  "instance": "module1",
  "url": "http://127.0.0.0:2000",
  "host": "module.example.org",
  "lets_encrypt": true,
  "http2https": true,
  "forward_auth": {
    "address": "http://127.0.0.1:9311/module/mod1/http-basic/action-fake",
    "skip_tls_verify": true,
    "auth_response_headers": [
      "X-Auth-User"
    ]
  }
}
```

# set-route input Properties

| Property                                        | Type      | Required | Nullable       | Defined by                                                                                                                                                              |
| :---------------------------------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [instance](#instance)                           | `string`  | Required | cannot be null | [set-route input](set-route-input-properties-instance-name.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/instance")                         |
| [url](#url)                                     | `string`  | Optional | cannot be null | [set-route input](set-route-input-properties-backend-url.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/url")                                |
| [host](#host)                                   | `string`  | Optional | can be null    | [set-route input](set-route-input-properties-virtualhost.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/host")                               |
| [path](#path)                                   | `string`  | Optional | can be null    | [set-route input](set-route-input-properties-request-path-prefix.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/path")                       |
| [priority](#priority)                           | `integer` | Optional | cannot be null | [set-route input](set-route-input-properties-priority.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/priority")                              |
| [lets\_encrypt](#lets_encrypt)                  | `boolean` | Optional | cannot be null | [set-route input](set-route-input-properties-lets-encrypt-certificate.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/lets_encrypt")          |
| [lets\_encrypt\_check](#lets_encrypt_check)     | `boolean` | Optional | cannot be null | [set-route input](set-route-input-properties-lets_encrypt_check.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/lets_encrypt_check")          |
| [lets\_encrypt\_cleanup](#lets_encrypt_cleanup) | `boolean` | Optional | cannot be null | [set-route input](set-route-input-properties-lets_encrypt_cleanup.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/lets_encrypt_cleanup")      |
| [http2https](#http2https)                       | `boolean` | Optional | cannot be null | [set-route input](set-route-input-properties-http-to-https-redirection.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/http2https")           |
| [strip\_prefix](#strip_prefix)                  | `boolean` | Optional | cannot be null | [set-route input](set-route-input-properties-strip-prefix-path.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/strip_prefix")                 |
| [slash\_redirect](#slash_redirect)              | `boolean` | Optional | cannot be null | [set-route input](set-route-input-properties-slash-redirect.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/slash_redirect")                  |
| [skip\_cert\_verify](#skip_cert_verify)         | `boolean` | Optional | cannot be null | [set-route input](set-route-input-properties-skip-certificate-verification.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/skip_cert_verify") |
| [user\_created](#user_created)                  | `boolean` | Optional | cannot be null | [set-route input](set-route-input-properties-user-created-route-flag.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/user_created")           |
| [ip\_allowlist](#ip_allowlist)                  | `array`   | Optional | cannot be null | [set-route input](set-route-input-properties-ip_allowlist.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/ip_allowlist")                      |
| [headers](#headers)                             | `object`  | Optional | cannot be null | [set-route input](set-route-input-properties-headers-list.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/headers")                           |
| [forward\_auth](#forward_auth)                  | `object`  | Optional | cannot be null | [set-route input](set-route-input-properties-forward-auth-configuration.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/forward_auth")        |

## instance

The instance name, which is unique inside the cluster.

`instance`

* is required

* Type: `string` ([Instance name](set-route-input-properties-instance-name.md))

* cannot be null

* defined in: [set-route input](set-route-input-properties-instance-name.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/instance")

### instance Type

`string` ([Instance name](set-route-input-properties-instance-name.md))

### instance Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[a-zA-Z0-9_\.-]+$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-zA-Z0-9_%5C.-%5D%2B%24 "try regular expression with regexr.com")

### instance Examples

```json
"module1"
```

## url

The backend target URL.

`url`

* is optional

* Type: `string` ([Backend URL](set-route-input-properties-backend-url.md))

* cannot be null

* defined in: [set-route input](set-route-input-properties-backend-url.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/url")

### url Type

`string` ([Backend URL](set-route-input-properties-backend-url.md))

### url Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc3986 "check the specification")

## host

A fully qualified domain name as virtualhost. NULL clears the current value.

`host`

* is optional

* Type: `string` ([Virtualhost](set-route-input-properties-virtualhost.md))

* can be null

* defined in: [set-route input](set-route-input-properties-virtualhost.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/host")

### host Type

`string` ([Virtualhost](set-route-input-properties-virtualhost.md))

### host Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
\.
```

[try pattern](https://regexr.com/?expression=%5C. "try regular expression with regexr.com")

**hostname**: the string must be a hostname, according to [RFC 1123, section 2.1](https://tools.ietf.org/html/rfc1123 "check the specification")

## path

A path prefix, the matching evaluation will be performed whit and without the trailing slash, eg /foo will match `/foo and `/foo/*, also `/foo/` will match /foo and /foo/*.  NULL clears the current value.

`path`

* is optional

* Type: `string` ([Request path prefix](set-route-input-properties-request-path-prefix.md))

* can be null

* defined in: [set-route input](set-route-input-properties-request-path-prefix.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/path")

### path Type

`string` ([Request path prefix](set-route-input-properties-request-path-prefix.md))

### path Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^/.*$
```

[try pattern](https://regexr.com/?expression=%5E%2F.*%24 "try regular expression with regexr.com")

### path Examples

```json
"/foo"
```

```json
"/foo/"
```

## priority

Override the default priority assignment (1,2,3), based on host and path

`priority`

* is optional

* Type: `integer`

* cannot be null

* defined in: [set-route input](set-route-input-properties-priority.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/priority")

### priority Type

`integer`

### priority Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## lets\_encrypt

Request a valid Let's Encrypt certificate.

`lets_encrypt`

* is optional

* Type: `boolean` ([Let's Encrypt certificate](set-route-input-properties-lets-encrypt-certificate.md))

* cannot be null

* defined in: [set-route input](set-route-input-properties-lets-encrypt-certificate.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/lets_encrypt")

### lets\_encrypt Type

`boolean` ([Let's Encrypt certificate](set-route-input-properties-lets-encrypt-certificate.md))

## lets\_encrypt\_check

When set true, return a validation error if a Let's Encrypt certificate is not immediately obtained

`lets_encrypt_check`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [set-route input](set-route-input-properties-lets_encrypt_check.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/lets_encrypt_check")

### lets\_encrypt\_check Type

`boolean`

### lets\_encrypt\_check Default Value

The default value is:

```json
false
```

## lets\_encrypt\_cleanup

If true and lets\_encrypt attribute is false, the Let's Encrypt certificate is removed and Traefik is restarted if needed.

`lets_encrypt_cleanup`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [set-route input](set-route-input-properties-lets_encrypt_cleanup.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/lets_encrypt_cleanup")

### lets\_encrypt\_cleanup Type

`boolean`

### lets\_encrypt\_cleanup Default Value

The default value is:

```json
false
```

## http2https

Redirect all the HTTP requests to HTTPS

`http2https`

* is optional

* Type: `boolean` ([HTTP to HTTPS redirection](set-route-input-properties-http-to-https-redirection.md))

* cannot be null

* defined in: [set-route input](set-route-input-properties-http-to-https-redirection.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/http2https")

### http2https Type

`boolean` ([HTTP to HTTPS redirection](set-route-input-properties-http-to-https-redirection.md))

## strip\_prefix

Strip the path prefix from the request

`strip_prefix`

* is optional

* Type: `boolean` ([Strip prefix path](set-route-input-properties-strip-prefix-path.md))

* cannot be null

* defined in: [set-route input](set-route-input-properties-strip-prefix-path.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/strip_prefix")

### strip\_prefix Type

`boolean` ([Strip prefix path](set-route-input-properties-strip-prefix-path.md))

## slash\_redirect

Redirect to path with trailing slash

`slash_redirect`

* is optional

* Type: `boolean` ([Slash redirect](set-route-input-properties-slash-redirect.md))

* cannot be null

* defined in: [set-route input](set-route-input-properties-slash-redirect.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/slash_redirect")

### slash\_redirect Type

`boolean` ([Slash redirect](set-route-input-properties-slash-redirect.md))

## skip\_cert\_verify

Do not verify the backend's certificate

`skip_cert_verify`

* is optional

* Type: `boolean` ([Skip certificate verification](set-route-input-properties-skip-certificate-verification.md))

* cannot be null

* defined in: [set-route input](set-route-input-properties-skip-certificate-verification.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/skip_cert_verify")

### skip\_cert\_verify Type

`boolean` ([Skip certificate verification](set-route-input-properties-skip-certificate-verification.md))

## user\_created

If true, the route is flagged as manually created by a user

`user_created`

* is optional

* Type: `boolean` ([User created route flag](set-route-input-properties-user-created-route-flag.md))

* cannot be null

* defined in: [set-route input](set-route-input-properties-user-created-route-flag.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/user_created")

### user\_created Type

`boolean` ([User created route flag](set-route-input-properties-user-created-route-flag.md))

## ip\_allowlist

List of allowed client ip addresses, in CIDR format

`ip_allowlist`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [set-route input](set-route-input-properties-ip_allowlist.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/ip_allowlist")

### ip\_allowlist Type

`string[]`

## headers

Headers to add or remove from an HTTP's request or response

`headers`

* is optional

* Type: `object` ([Headers list](set-route-input-properties-headers-list.md))

* cannot be null

* defined in: [set-route input](set-route-input-properties-headers-list.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/headers")

### headers Type

`object` ([Headers list](set-route-input-properties-headers-list.md))

### headers Examples

```json
{
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
}
```

## forward\_auth

If set enabled forwardAuth prop on traefik. If null

`forward_auth`

* is optional

* Type: `object` ([Forward Auth configuration](set-route-input-properties-forward-auth-configuration.md))

* cannot be null

* defined in: [set-route input](set-route-input-properties-forward-auth-configuration.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/forward_auth")

### forward\_auth Type

`object` ([Forward Auth configuration](set-route-input-properties-forward-auth-configuration.md))
