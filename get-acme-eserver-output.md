# get-acme-server output Schema

```txt
http://schema.nethserver.org/traefik/get-acme-eserver-output.json
```

Get ACME configuration

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [get-acme-eserver-output.json](traefik/get-acme-eserver-output.json "open original schema") |

## get-acme-server output Type

`object` ([get-acme-server output](get-acme-eserver-output.md))

## get-acme-server output Examples

```json
{
  "challenge": "HTTP-01",
  "email": "certadmin@example.org",
  "url": "https://acme-staging-v02.api.letsencrypt.org/directory"
}
```

```json
{
  "url": "https://acme-staging-v02.api.letsencrypt.org/directory"
}
```

# get-acme-server output Properties

| Property                | Type     | Required | Nullable       | Defined by                                                                                                                                                                 |
| :---------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [email](#email)         | Merged   | Required | cannot be null | [get-acme-server output](get-acme-eserver-output-properties-email.md "http://schema.nethserver.org/traefik/get-acme-eserver-output.json#/properties/email")                |
| [challenge](#challenge) | `string` | Required | cannot be null | [get-acme-server output](get-acme-eserver-output-properties-challenge.md "http://schema.nethserver.org/traefik/get-acme-eserver-output.json#/properties/challenge")        |
| [url](#url)             | `string` | Required | cannot be null | [get-acme-server output](get-acme-eserver-output-properties-url-of-the-acme-server.md "http://schema.nethserver.org/traefik/get-acme-eserver-output.json#/properties/url") |

## email



`email`

* is required

* Type: merged type ([Details](get-acme-eserver-output-properties-email.md))

* cannot be null

* defined in: [get-acme-server output](get-acme-eserver-output-properties-email.md "http://schema.nethserver.org/traefik/get-acme-eserver-output.json#/properties/email")

### email Type

merged type ([Details](get-acme-eserver-output-properties-email.md))

one (and only one) of

* [Untitled string in get-acme-server output](get-acme-eserver-output-properties-email-oneof-0.md "check type definition")

* [Untitled undefined type in get-acme-server output](get-acme-eserver-output-properties-email-oneof-1.md "check type definition")

## challenge



`challenge`

* is required

* Type: `string`

* cannot be null

* defined in: [get-acme-server output](get-acme-eserver-output-properties-challenge.md "http://schema.nethserver.org/traefik/get-acme-eserver-output.json#/properties/challenge")

### challenge Type

`string`

### challenge Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation |
| :-------------- | :---------- |
| `"TLS-ALPN-01"` |             |
| `"HTTP-01"`     |             |

## url



`url`

* is required

* Type: `string` ([Url of the ACME server](get-acme-eserver-output-properties-url-of-the-acme-server.md))

* cannot be null

* defined in: [get-acme-server output](get-acme-eserver-output-properties-url-of-the-acme-server.md "http://schema.nethserver.org/traefik/get-acme-eserver-output.json#/properties/url")

### url Type

`string` ([Url of the ACME server](get-acme-eserver-output-properties-url-of-the-acme-server.md))

### url Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc3986 "check the specification")

### url Examples

```json
"https://acme-staging-v02.api.letsencrypt.org/directory"
```
