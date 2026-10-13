# The server address Schema

```txt
http://schema.nethserver.org/traefik/get-route-output.json#/properties/forward_auth/properties/address
```

The address option defines the authentication server address

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                      |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [get-route-output.json\*](traefik/get-route-output.json "open original schema") |

## address Type

`string` ([The server address](get-route-output-properties-forward-auth-configuration-properties-the-server-address.md))

## address Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc3986 "check the specification")
