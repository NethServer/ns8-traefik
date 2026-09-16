# A route expanded Schema

```txt
http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [list-routes-output.json\*](samba/list-routes-output.json "open original schema") |

## 0 Type

`object` ([A route expanded](list-routes-output-1-items-oneof-a-route-expanded.md))

any of

* [Untitled undefined type in list-routes output](list-routes-output-1-items-oneof-a-route-expanded-anyof-0.md "check type definition")

* [Untitled undefined type in list-routes output](list-routes-output-1-items-oneof-a-route-expanded-anyof-1.md "check type definition")

# 0 Properties

| Property                                      | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                  |
| :-------------------------------------------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [instance](#instance)                         | `string`  | Required | cannot be null | [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-instance-name.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/instance")                         |
| [url](#url)                                   | `string`  | Required | cannot be null | [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-backend-url.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/url")                                |
| [host](#host)                                 | `string`  | Optional | cannot be null | [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-virtualhost.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/host")                               |
| [path](#path)                                 | `string`  | Optional | cannot be null | [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-request-path-prefix.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/path")                       |
| [lets\_encrypt](#lets_encrypt)                | `boolean` | Optional | cannot be null | [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-lets-encrypt-certificate.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/lets_encrypt")          |
| [lets\_encrypt\_status](#lets_encrypt_status) | `string`  | Optional | cannot be null | [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-lets_encrypt_status.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/lets_encrypt_status")        |
| [http2https](#http2https)                     | `boolean` | Required | cannot be null | [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-http-to-https-redirection.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/http2https")           |
| [strip\_prefix](#strip_prefix)                | `boolean` | Optional | cannot be null | [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-strip-prefix-path.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/strip_prefix")                 |
| [skip\_cert\_verify](#skip_cert_verify)       | `boolean` | Optional | cannot be null | [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-skip-certificate-verification.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/skip_cert_verify") |
| [user\_created](#user_created)                | `boolean` | Required | cannot be null | [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-user-created-route-flag.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/user_created")           |
| [headers](#headers)                           | `object`  | Optional | cannot be null | [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-headers-list.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/headers")                           |
| [forward\_auth](#forward_auth)                | `object`  | Optional | cannot be null | [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-forward-auth-configuration.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/forward_auth")        |

## instance

The instance name, which is unique inside the cluster.

`instance`

* is required

* Type: `string` ([Instance name](list-routes-output-1-items-oneof-a-route-expanded-properties-instance-name.md))

* cannot be null

* defined in: [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-instance-name.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/instance")

### instance Type

`string` ([Instance name](list-routes-output-1-items-oneof-a-route-expanded-properties-instance-name.md))

### instance Examples

```json
"module1"
```

## url

The backend target URL.

`url`

* is required

* Type: `string` ([Backend URL](list-routes-output-1-items-oneof-a-route-expanded-properties-backend-url.md))

* cannot be null

* defined in: [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-backend-url.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/url")

### url Type

`string` ([Backend URL](list-routes-output-1-items-oneof-a-route-expanded-properties-backend-url.md))

### url Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc3986 "check the specification")

## host

A fully qualified domain name as virtualhost.

`host`

* is optional

* Type: `string` ([Virtualhost](list-routes-output-1-items-oneof-a-route-expanded-properties-virtualhost.md))

* cannot be null

* defined in: [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-virtualhost.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/host")

### host Type

`string` ([Virtualhost](list-routes-output-1-items-oneof-a-route-expanded-properties-virtualhost.md))

### host Constraints

**hostname**: the string must be a hostname, according to [RFC 1123, section 2.1](https://tools.ietf.org/html/rfc1123 "check the specification")

## path

A path prefix, the matching evaluation will be performed whit and without the trailing slash, eg /foo will match `/foo and `/foo/*, also `/foo/` will match /foo and /foo/*

`path`

* is optional

* Type: `string` ([Request path prefix](list-routes-output-1-items-oneof-a-route-expanded-properties-request-path-prefix.md))

* cannot be null

* defined in: [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-request-path-prefix.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/path")

### path Type

`string` ([Request path prefix](list-routes-output-1-items-oneof-a-route-expanded-properties-request-path-prefix.md))

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

* is optional

* Type: `boolean` ([Let's Encrypt certificate](list-routes-output-1-items-oneof-a-route-expanded-properties-lets-encrypt-certificate.md))

* cannot be null

* defined in: [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-lets-encrypt-certificate.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/lets_encrypt")

### lets\_encrypt Type

`boolean` ([Let's Encrypt certificate](list-routes-output-1-items-oneof-a-route-expanded-properties-lets-encrypt-certificate.md))

## lets\_encrypt\_status

If Let's Encrypt certificate is requested, report the current certificate status.

`lets_encrypt_status`

* is optional

* Type: `string`

* cannot be null

* defined in: [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-lets_encrypt_status.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/lets_encrypt_status")

### lets\_encrypt\_status Type

`string`

### lets\_encrypt\_status Examples

```json
"pending"
```

## http2https

Redirect all the HTTP requests to HTTPS

`http2https`

* is required

* Type: `boolean` ([HTTP to HTTPS redirection](list-routes-output-1-items-oneof-a-route-expanded-properties-http-to-https-redirection.md))

* cannot be null

* defined in: [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-http-to-https-redirection.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/http2https")

### http2https Type

`boolean` ([HTTP to HTTPS redirection](list-routes-output-1-items-oneof-a-route-expanded-properties-http-to-https-redirection.md))

## strip\_prefix

Strip the path prefix from the request

`strip_prefix`

* is optional

* Type: `boolean` ([Strip prefix path](list-routes-output-1-items-oneof-a-route-expanded-properties-strip-prefix-path.md))

* cannot be null

* defined in: [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-strip-prefix-path.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/strip_prefix")

### strip\_prefix Type

`boolean` ([Strip prefix path](list-routes-output-1-items-oneof-a-route-expanded-properties-strip-prefix-path.md))

## skip\_cert\_verify

Do not verify the backend's certificate

`skip_cert_verify`

* is optional

* Type: `boolean` ([Skip certificate verification](list-routes-output-1-items-oneof-a-route-expanded-properties-skip-certificate-verification.md))

* cannot be null

* defined in: [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-skip-certificate-verification.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/skip_cert_verify")

### skip\_cert\_verify Type

`boolean` ([Skip certificate verification](list-routes-output-1-items-oneof-a-route-expanded-properties-skip-certificate-verification.md))

## user\_created

If true, the route is flagged as manually created by a user

`user_created`

* is required

* Type: `boolean` ([User created route flag](list-routes-output-1-items-oneof-a-route-expanded-properties-user-created-route-flag.md))

* cannot be null

* defined in: [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-user-created-route-flag.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/user_created")

### user\_created Type

`boolean` ([User created route flag](list-routes-output-1-items-oneof-a-route-expanded-properties-user-created-route-flag.md))

## headers

Headers to add or remove from an HTTP's request or response

`headers`

* is optional

* Type: `object` ([Headers list](list-routes-output-1-items-oneof-a-route-expanded-properties-headers-list.md))

* cannot be null

* defined in: [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-headers-list.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/headers")

### headers Type

`object` ([Headers list](list-routes-output-1-items-oneof-a-route-expanded-properties-headers-list.md))

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

* is optional

* Type: `object` ([Forward Auth configuration](list-routes-output-1-items-oneof-a-route-expanded-properties-forward-auth-configuration.md))

* cannot be null

* defined in: [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-forward-auth-configuration.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/forward_auth")

### forward\_auth Type

`object` ([Forward Auth configuration](list-routes-output-1-items-oneof-a-route-expanded-properties-forward-auth-configuration.md))
