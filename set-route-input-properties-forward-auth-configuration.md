# Forward Auth configuration Schema

```txt
http://schema.nethserver.org/traefik/set-route-input.json#/properties/forward_auth
```

If set enabled forwardAuth prop on traefik. If null

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                    |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [set-route-input.json\*](traefik/set-route-input.json "open original schema") |

## forward\_auth Type

`object` ([Forward Auth configuration](set-route-input-properties-forward-auth-configuration.md))

# forward\_auth Properties

| Property                                          | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                         |
| :------------------------------------------------ | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [address](#address)                               | `string`  | Optional | cannot be null | [set-route input](set-route-input-properties-forward-auth-configuration-properties-the-server-address.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/forward_auth/properties/address")                  |
| [skip\_tls\_verify](#skip_tls_verify)             | `boolean` | Optional | cannot be null | [set-route input](set-route-input-properties-forward-auth-configuration-properties-skip-tls-verify.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/forward_auth/properties/skip_tls_verify")             |
| [auth\_response\_headers](#auth_response_headers) | `array`   | Optional | cannot be null | [set-route input](set-route-input-properties-forward-auth-configuration-properties-auth-response-headers.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/forward_auth/properties/auth_response_headers") |

## address

The address option defines the authentication server address

`address`

* is optional

* Type: `string` ([The server address](set-route-input-properties-forward-auth-configuration-properties-the-server-address.md))

* cannot be null

* defined in: [set-route input](set-route-input-properties-forward-auth-configuration-properties-the-server-address.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/forward_auth/properties/address")

### address Type

`string` ([The server address](set-route-input-properties-forward-auth-configuration-properties-the-server-address.md))

### address Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc3986 "check the specification")

## skip\_tls\_verify

If insecureSkipVerify is true, the TLS connection to the authentication server accepts any certificate presented by the server regardless of the hostnames it covers

`skip_tls_verify`

* is optional

* Type: `boolean` ([Skip TLS verify](set-route-input-properties-forward-auth-configuration-properties-skip-tls-verify.md))

* cannot be null

* defined in: [set-route input](set-route-input-properties-forward-auth-configuration-properties-skip-tls-verify.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/forward_auth/properties/skip_tls_verify")

### skip\_tls\_verify Type

`boolean` ([Skip TLS verify](set-route-input-properties-forward-auth-configuration-properties-skip-tls-verify.md))

## auth\_response\_headers

A list of headers to be copied from backend response to the client

`auth_response_headers`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [set-route input](set-route-input-properties-forward-auth-configuration-properties-auth-response-headers.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/forward_auth/properties/auth_response_headers")

### auth\_response\_headers Type

`string[]`
