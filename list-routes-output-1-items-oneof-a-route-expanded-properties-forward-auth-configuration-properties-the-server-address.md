# The server address Schema

```txt
http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/forward_auth/properties/address
```

The address option defines the authentication server address

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [list-routes-output.json\*](samba/list-routes-output.json "open original schema") |

## address Type

`string` ([The server address](list-routes-output-1-items-oneof-a-route-expanded-properties-forward-auth-configuration-properties-the-server-address.md))

## address Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc3986 "check the specification")
