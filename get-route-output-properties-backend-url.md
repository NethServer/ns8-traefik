# Backend URL Schema

```txt
http://schema.nethserver.org/traefik/get-route-output.json#/properties/url
```

The backend target URL.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                      |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [get-route-output.json\*](traefik/get-route-output.json "open original schema") |

## url Type

`string` ([Backend URL](get-route-output-properties-backend-url.md))

## url Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc3986 "check the specification")
