# Backend URL Schema

```txt
http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/url
```

The backend target URL.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [list-routes-output.json\*](samba/list-routes-output.json "open original schema") |

## url Type

`string` ([Backend URL](list-routes-output-1-items-oneof-a-route-expanded-properties-backend-url.md))

## url Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc3986 "check the specification")
