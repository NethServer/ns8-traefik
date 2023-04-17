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

any of

*   [Untitled undefined type in set-route input](set-route-input-anyof-0.md "check type definition")

*   [Untitled undefined type in set-route input](set-route-input-anyof-1.md "check type definition")

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
  "instance": "module1",
  "url": "http://127.0.0.0:2000",
  "host": "module.example.org",
  "lets_encrypt": true,
  "http2https": true,
  "forward_auth": {
    "address": "http://127.0.0.1:9311/module/mod1/http-basic/action-fake",
    "skip_tls_verify": true
  }
}
```

# set-route input Properties

| Property                       | Type      | Required | Nullable       | Defined by                                                                                                                                                       |
| :----------------------------- | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [instance](#instance)          | `string`  | Required | cannot be null | [set-route input](set-route-input-properties-instance-name.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/instance")                  |
| [url](#url)                    | `string`  | Required | cannot be null | [set-route input](set-route-input-properties-backend-url.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/url")                         |
| [host](#host)                  | `string`  | Optional | cannot be null | [set-route input](set-route-input-properties-virtualhost.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/host")                        |
| [path](#path)                  | `string`  | Optional | cannot be null | [set-route input](set-route-input-properties-request-path-prefix.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/path")                |
| [lets\_encrypt](#lets_encrypt) | `boolean` | Optional | cannot be null | [set-route input](set-route-input-properties-lets-encrypt-certificate.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/lets_encrypt")   |
| [http2https](#http2https)      | `boolean` | Required | cannot be null | [set-route input](set-route-input-properties-http-to-https-redirection.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/http2https")    |
| [strip\_prefix](#strip_prefix) | `boolean` | Optional | cannot be null | [set-route input](set-route-input-properties-strip-prefix-path.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/strip_prefix")          |
| [user\_created](#user_created) | `boolean` | Optional | cannot be null | [set-route input](set-route-input-properties-user-created-route-flag.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/user_created")    |
| [headers](#headers)            | `object`  | Optional | cannot be null | [set-route input](set-route-input-properties-headers-list.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/headers")                    |
| [forward\_auth](#forward_auth) | `object`  | Optional | cannot be null | [set-route input](set-route-input-properties-forward-auth-configuration.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/forward_auth") |

## instance

The instance name, which is unique inside the cluster.

`instance`

*   is required

*   Type: `string` ([Instance name](set-route-input-properties-instance-name.md))

*   cannot be null

*   defined in: [set-route input](set-route-input-properties-instance-name.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/instance")

### instance Type

`string` ([Instance name](set-route-input-properties-instance-name.md))

### instance Examples

```json
"module1"
```

## url

The backend target URL.

`url`

*   is required

*   Type: `string` ([Backend URL](set-route-input-properties-backend-url.md))

*   cannot be null

*   defined in: [set-route input](set-route-input-properties-backend-url.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/url")

### url Type

`string` ([Backend URL](set-route-input-properties-backend-url.md))

### url Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc3986 "check the specification")

## host

A fully qualified domain name as virtualhost.

`host`

*   is optional

*   Type: `string` ([Virtualhost](set-route-input-properties-virtualhost.md))

*   cannot be null

*   defined in: [set-route input](set-route-input-properties-virtualhost.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/host")

### host Type

`string` ([Virtualhost](set-route-input-properties-virtualhost.md))

### host Constraints

**hostname**: the string must be a hostname, according to [RFC 1123, section 2.1](https://tools.ietf.org/html/rfc1123 "check the specification")

## path

A path prefix, the matching evaluation will be performed whit and without the trailing slash, eg /foo will match `/foo and `/foo/*, also `/foo/` will match /foo and /foo/*

`path`

*   is optional

*   Type: `string` ([Request path prefix](set-route-input-properties-request-path-prefix.md))

*   cannot be null

*   defined in: [set-route input](set-route-input-properties-request-path-prefix.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/path")

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

## lets\_encrypt

Request a valid Let's Encrypt certificate.

`lets_encrypt`

*   is optional

*   Type: `boolean` ([Let's Encrypt certificate](set-route-input-properties-lets-encrypt-certificate.md))

*   cannot be null

*   defined in: [set-route input](set-route-input-properties-lets-encrypt-certificate.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/lets_encrypt")

### lets\_encrypt Type

`boolean` ([Let's Encrypt certificate](set-route-input-properties-lets-encrypt-certificate.md))

## http2https

Redirect all the HTTP requests to HTTPS

`http2https`

*   is required

*   Type: `boolean` ([HTTP to HTTPS redirection](set-route-input-properties-http-to-https-redirection.md))

*   cannot be null

*   defined in: [set-route input](set-route-input-properties-http-to-https-redirection.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/http2https")

### http2https Type

`boolean` ([HTTP to HTTPS redirection](set-route-input-properties-http-to-https-redirection.md))

## strip\_prefix

Strip the path prefix from the request

`strip_prefix`

*   is optional

*   Type: `boolean` ([Strip prefix path](set-route-input-properties-strip-prefix-path.md))

*   cannot be null

*   defined in: [set-route input](set-route-input-properties-strip-prefix-path.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/strip_prefix")

### strip\_prefix Type

`boolean` ([Strip prefix path](set-route-input-properties-strip-prefix-path.md))

## user\_created

If true, the route is flagged as manually created by a user

`user_created`

*   is optional

*   Type: `boolean` ([User created route flag](set-route-input-properties-user-created-route-flag.md))

*   cannot be null

*   defined in: [set-route input](set-route-input-properties-user-created-route-flag.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/user_created")

### user\_created Type

`boolean` ([User created route flag](set-route-input-properties-user-created-route-flag.md))

## headers

Headers to add or remove from an HTTP's request or response

`headers`

*   is optional

*   Type: `object` ([Headers list](set-route-input-properties-headers-list.md))

*   cannot be null

*   defined in: [set-route input](set-route-input-properties-headers-list.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/headers")

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

If set enabled forwardAuth prop on traefik

`forward_auth`

*   is optional

*   Type: `object` ([Forward Auth configuration](set-route-input-properties-forward-auth-configuration.md))

*   cannot be null

*   defined in: [set-route input](set-route-input-properties-forward-auth-configuration.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/forward_auth")

### forward\_auth Type

`object` ([Forward Auth configuration](set-route-input-properties-forward-auth-configuration.md))