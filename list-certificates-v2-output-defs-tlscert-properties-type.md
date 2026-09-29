# Untitled string in list-certificates-v2 output Schema

```txt
http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/type
```

Possible values: internal (acme.json), custom (uploaded)

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                            |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [list-certificates-v2-output.json\*](traefik/list-certificates-v2-output.json "open original schema") |

## type Type

`string`

## type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | :---------- |
| `"internal"` |             |
| `"custom"`   |             |
