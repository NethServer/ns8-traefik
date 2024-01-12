# Forward Auth configuration Schema

```txt
http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/forward_auth
```

If set enabled forwardAuth prop on traefik

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [list-routes-output.json\*](samba/list-routes-output.json "open original schema") |

## forward\_auth Type

`object` ([Forward Auth configuration](list-routes-output-1-items-oneof-a-route-expanded-properties-forward-auth-configuration.md))

# forward\_auth Properties

| Property                              | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                 |
| :------------------------------------ | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [address](#address)                   | `string`  | Required | cannot be null | [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-forward-auth-configuration-properties-the-server-address.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/forward_auth/properties/address")      |
| [skip\_tls\_verify](#skip_tls_verify) | `boolean` | Optional | cannot be null | [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-forward-auth-configuration-properties-skip-tls-verify.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/forward_auth/properties/skip_tls_verify") |

## address

The address option defines the authentication server address

`address`

*   is required

*   Type: `string` ([The server address](list-routes-output-1-items-oneof-a-route-expanded-properties-forward-auth-configuration-properties-the-server-address.md))

*   cannot be null

*   defined in: [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-forward-auth-configuration-properties-the-server-address.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/forward_auth/properties/address")

### address Type

`string` ([The server address](list-routes-output-1-items-oneof-a-route-expanded-properties-forward-auth-configuration-properties-the-server-address.md))

### address Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc3986 "check the specification")

## skip\_tls\_verify

If insecureskipCertVerify is true, the TLS connection to the authentication server accepts any certificate presented by the server regardless of the hostnames it covers

`skip_tls_verify`

*   is optional

*   Type: `boolean` ([Skip TLS verify](list-routes-output-1-items-oneof-a-route-expanded-properties-forward-auth-configuration-properties-skip-tls-verify.md))

*   cannot be null

*   defined in: [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-forward-auth-configuration-properties-skip-tls-verify.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/forward_auth/properties/skip_tls_verify")

### skip\_tls\_verify Type

`boolean` ([Skip TLS verify](list-routes-output-1-items-oneof-a-route-expanded-properties-forward-auth-configuration-properties-skip-tls-verify.md))