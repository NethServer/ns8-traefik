# Virtualhost Schema

```txt
http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/host
```

A fully qualified domain name as virtualhost.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [list-routes-output.json\*](samba/list-routes-output.json "open original schema") |

## host Type

`string` ([Virtualhost](list-routes-output-1-items-oneof-a-route-expanded-properties-virtualhost.md))

## host Constraints

**hostname**: the string must be a hostname, according to [RFC 1123, section 2.1](https://tools.ietf.org/html/rfc1123 "check the specification")
