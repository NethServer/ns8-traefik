# get-route output Schema

```txt
http://schema.nethserver.org/traefik/get-route-output.json
```

Show the configuration of a  HTTP route

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                    |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [get-route-output.json](traefik/get-route-output.json "open original schema") |

## get-route output Type

`object` ([get-route output](get-route-output.md))

one (and only one) of

* any of

  * [Untitled undefined type in get-route output](get-route-output-oneof-0-anyof-0.md "check type definition")

  * [Untitled undefined type in get-route output](get-route-output-oneof-0-anyof-1.md "check type definition")

* [Untitled undefined type in get-route output](get-route-output-oneof-1.md "check type definition")

## get-route output Examples

```json
{
  "instance": "module1",
  "url": "http://127.0.0.0:2000",
  "host": "module.example.org",
  "priority": 2,
  "lets_encrypt": true,
  "http2https": true,
  "skip_cert_verify": true
}
```

```json
{
  "instance": "module2",
  "url": "http://127.0.0.0:2000",
  "host": "module.example.org",
  "path": "/foo",
  "priority": 3,
  "lets_encrypt": true,
  "http2https": true,
  "strip_prefix": false,
  "skip_cert_verify": true
}
```

```json
{
  "instance": "module3",
  "url": "http://127.0.0.0:2000",
  "path": "/foo",
  "priority": 3,
  "lets_encrypt": true,
  "http2https": true,
  "strip_prefix": false,
  "skip_cert_verify": true
}
```

# get-route output Properties

| Property                                | Type      | Required | Nullable       | Defined by                                                                                                                                                                 |
| :-------------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [instance](#instance)                   | `string`  | Optional | cannot be null | [get-route output](get-route-output-properties-instance-name.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/instance")                         |
| [priority](#priority)                   | `integer` | Optional | cannot be null | [get-route output](get-route-output-properties-priority.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/priority")                              |
| [url](#url)                             | `string`  | Optional | cannot be null | [get-route output](get-route-output-properties-backend-url.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/url")                                |
| [host](#host)                           | `string`  | Optional | cannot be null | [get-route output](get-route-output-properties-virtualhost.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/host")                               |
| [path](#path)                           | `string`  | Optional | cannot be null | [get-route output](get-route-output-properties-request-path-prefix.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/path")                       |
| [lets\_encrypt](#lets_encrypt)          | `boolean` | Optional | cannot be null | [get-route output](get-route-output-properties-lets-encrypt-certificate.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/lets_encrypt")          |
| [http2https](#http2https)               | `boolean` | Optional | cannot be null | [get-route output](get-route-output-properties-http-to-https-redirection.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/http2https")           |
| [slash\_redirect](#slash_redirect)      | `boolean` | Optional | cannot be null | [get-route output](get-route-output-properties-slash-redirect.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/slash_redirect")                  |
| [strip\_prefix](#strip_prefix)          | `boolean` | Optional | cannot be null | [get-route output](get-route-output-properties-strip-prefix-path.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/strip_prefix")                 |
| [skip\_cert\_verify](#skip_cert_verify) | `boolean` | Optional | cannot be null | [get-route output](get-route-output-properties-skip-certificate-verification.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/skip_cert_verify") |
| [user\_created](#user_created)          | `boolean` | Optional | cannot be null | [get-route output](get-route-output-properties-user-created-route-flag.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/user_created")           |
| [ip\_allowlist](#ip_allowlist)          | `array`   | Optional | cannot be null | [get-route output](get-route-output-properties-ip_allowlist.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/ip_allowlist")                      |
| [headers](#headers)                     | `object`  | Optional | cannot be null | [get-route output](get-route-output-properties-headers-list.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/headers")                           |
| [forward\_auth](#forward_auth)          | `object`  | Optional | cannot be null | [get-route output](get-route-output-properties-forward-auth-configuration.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/forward_auth")        |

## instance

The instance name, which is unique inside the cluster.

`instance`

* is optional

* Type: `string` ([Instance name](get-route-output-properties-instance-name.md))

* cannot be null

* defined in: [get-route output](get-route-output-properties-instance-name.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/instance")

### instance Type

`string` ([Instance name](get-route-output-properties-instance-name.md))

### instance Examples

```json
"module1"
```

## priority

The Traefik router rule priority assigned to the HTTP route

`priority`

* is optional

* Type: `integer`

* cannot be null

* defined in: [get-route output](get-route-output-properties-priority.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/priority")

### priority Type

`integer`

## url

The backend target URL.

`url`

* is optional

* Type: `string` ([Backend URL](get-route-output-properties-backend-url.md))

* cannot be null

* defined in: [get-route output](get-route-output-properties-backend-url.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/url")

### url Type

`string` ([Backend URL](get-route-output-properties-backend-url.md))

### url Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc3986 "check the specification")

## host

A fully qualified domain name as virtualhost.

`host`

* is optional

* Type: `string` ([Virtualhost](get-route-output-properties-virtualhost.md))

* cannot be null

* defined in: [get-route output](get-route-output-properties-virtualhost.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/host")

### host Type

`string` ([Virtualhost](get-route-output-properties-virtualhost.md))

### host Constraints

**hostname**: the string must be a hostname, according to [RFC 1123, section 2.1](https://tools.ietf.org/html/rfc1123 "check the specification")

## path

A path prefix, the matching evaluation will be performed whit and without the trailing slash, eg /foo will match `/foo and `/foo/*, also `/foo/` will match /foo and /foo/*

`path`

* is optional

* Type: `string` ([Request path prefix](get-route-output-properties-request-path-prefix.md))

* cannot be null

* defined in: [get-route output](get-route-output-properties-request-path-prefix.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/path")

### path Type

`string` ([Request path prefix](get-route-output-properties-request-path-prefix.md))

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

* is optional

* Type: `boolean` ([Let's Encrypt certificate](get-route-output-properties-lets-encrypt-certificate.md))

* cannot be null

* defined in: [get-route output](get-route-output-properties-lets-encrypt-certificate.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/lets_encrypt")

### lets\_encrypt Type

`boolean` ([Let's Encrypt certificate](get-route-output-properties-lets-encrypt-certificate.md))

## http2https

Redirect all the HTTP requests to HTTPS

`http2https`

* is optional

* Type: `boolean` ([HTTP to HTTPS redirection](get-route-output-properties-http-to-https-redirection.md))

* cannot be null

* defined in: [get-route output](get-route-output-properties-http-to-https-redirection.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/http2https")

### http2https Type

`boolean` ([HTTP to HTTPS redirection](get-route-output-properties-http-to-https-redirection.md))

## slash\_redirect

Redirect to path with trailing slash

`slash_redirect`

* is optional

* Type: `boolean` ([Slash redirect](get-route-output-properties-slash-redirect.md))

* cannot be null

* defined in: [get-route output](get-route-output-properties-slash-redirect.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/slash_redirect")

### slash\_redirect Type

`boolean` ([Slash redirect](get-route-output-properties-slash-redirect.md))

## strip\_prefix

Strip the path prefix from the request

`strip_prefix`

* is optional

* Type: `boolean` ([Strip prefix path](get-route-output-properties-strip-prefix-path.md))

* cannot be null

* defined in: [get-route output](get-route-output-properties-strip-prefix-path.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/strip_prefix")

### strip\_prefix Type

`boolean` ([Strip prefix path](get-route-output-properties-strip-prefix-path.md))

## skip\_cert\_verify

Do not verify the backend's certificate

`skip_cert_verify`

* is optional

* Type: `boolean` ([Skip certificate verification](get-route-output-properties-skip-certificate-verification.md))

* cannot be null

* defined in: [get-route output](get-route-output-properties-skip-certificate-verification.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/skip_cert_verify")

### skip\_cert\_verify Type

`boolean` ([Skip certificate verification](get-route-output-properties-skip-certificate-verification.md))

## user\_created

If true, the route is flagged as manually created by a user

`user_created`

* is optional

* Type: `boolean` ([User created route flag](get-route-output-properties-user-created-route-flag.md))

* cannot be null

* defined in: [get-route output](get-route-output-properties-user-created-route-flag.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/user_created")

### user\_created Type

`boolean` ([User created route flag](get-route-output-properties-user-created-route-flag.md))

## ip\_allowlist

List of allowed client ip addresses, in CIDR format

`ip_allowlist`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [get-route output](get-route-output-properties-ip_allowlist.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/ip_allowlist")

### ip\_allowlist Type

`string[]`

## headers

Headers to add or remove from an HTTP's request or response

`headers`

* is optional

* Type: `object` ([Headers list](get-route-output-properties-headers-list.md))

* cannot be null

* defined in: [get-route output](get-route-output-properties-headers-list.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/headers")

### headers Type

`object` ([Headers list](get-route-output-properties-headers-list.md))

## forward\_auth

If set enabled forwardAuth prop on traefik

`forward_auth`

* is optional

* Type: `object` ([Forward Auth configuration](get-route-output-properties-forward-auth-configuration.md))

* cannot be null

* defined in: [get-route output](get-route-output-properties-forward-auth-configuration.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/forward_auth")

### forward\_auth Type

`object` ([Forward Auth configuration](get-route-output-properties-forward-auth-configuration.md))
