# Untitled string in get-acme-server output Schema

```txt
http://schema.nethserver.org/traefik/get-acme-eserver-output.json#/properties/challenge
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [get-acme-eserver-output.json\*](traefik/get-acme-eserver-output.json "open original schema") |

## challenge Type

`string`

## challenge Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation |
| :-------------- | :---------- |
| `"TLS-ALPN-01"` |             |
| `"HTTP-01"`     |             |
