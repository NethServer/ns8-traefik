# Untitled string in set-acme-server input Schema

```txt
http://schema.nethserver.org/traefik/set-acme-server-input.json#/properties/challenge
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [set-acme-server-input.json\*](traefik/set-acme-server-input.json "open original schema") |

## challenge Type

`string`

## challenge Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation |
| :-------------- | :---------- |
| `"TLS-ALPN-01"` |             |
| `"HTTP-01"`     |             |
