# Untitled string in get-certificate output Schema

```txt
http://schema.nethserver.org/traefik/get-certificate-output.json#/properties/type
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                  |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [get-certificate-output.json\*](traefik/get-certificate-output.json "open original schema") |

## type Type

`string`

## type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | :---------- |
| `"internal"`   |             |
| `"custom"`     |             |
| `"selfsigned"` |             |
