# set-acme-server input Schema

```txt
http://schema.nethserver.org/traefik/set-acme-server-input.json
```

Set ACME configuration

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                              |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [set-acme-server-input.json](traefik/set-acme-server-input.json "open original schema") |

## set-acme-server input Type

`object` ([set-acme-server input](set-acme-server-input.md))

## set-acme-server input Examples

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

# set-acme-server input Properties

| Property                | Type     | Required | Nullable       | Defined by                                                                                                                                                            |
| :---------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [email](#email)         | Merged   | Optional | cannot be null | [set-acme-server input](set-acme-server-input-properties-email.md "http://schema.nethserver.org/traefik/set-acme-server-input.json#/properties/email")                |
| [challenge](#challenge) | `string` | Optional | cannot be null | [set-acme-server input](set-acme-server-input-properties-challenge.md "http://schema.nethserver.org/traefik/set-acme-server-input.json#/properties/challenge")        |
| [url](#url)             | `string` | Required | cannot be null | [set-acme-server input](set-acme-server-input-properties-url-of-the-acme-server.md "http://schema.nethserver.org/traefik/set-acme-server-input.json#/properties/url") |

## email



`email`

* is optional

* Type: merged type ([Details](set-acme-server-input-properties-email.md))

* cannot be null

* defined in: [set-acme-server input](set-acme-server-input-properties-email.md "http://schema.nethserver.org/traefik/set-acme-server-input.json#/properties/email")

### email Type

merged type ([Details](set-acme-server-input-properties-email.md))

one (and only one) of

* [Untitled string in set-acme-server input](set-acme-server-input-properties-email-oneof-0.md "check type definition")

* [Untitled undefined type in set-acme-server input](set-acme-server-input-properties-email-oneof-1.md "check type definition")

## challenge



`challenge`

* is optional

* Type: `string`

* cannot be null

* defined in: [set-acme-server input](set-acme-server-input-properties-challenge.md "http://schema.nethserver.org/traefik/set-acme-server-input.json#/properties/challenge")

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

* Type: `string` ([Url of the ACME server](set-acme-server-input-properties-url-of-the-acme-server.md))

* cannot be null

* defined in: [set-acme-server input](set-acme-server-input-properties-url-of-the-acme-server.md "http://schema.nethserver.org/traefik/set-acme-server-input.json#/properties/url")

### url Type

`string` ([Url of the ACME server](set-acme-server-input-properties-url-of-the-acme-server.md))

### url Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc3986 "check the specification")

### url Examples

```json
"https://acme-staging-v02.api.letsencrypt.org/directory"
```
