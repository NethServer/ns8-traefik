# must be route, internal or custom Schema

```txt
http://schema.nethserver.org/traefik/get-certificate-output.json#/oneOf/0/properties/type
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                  |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [get-certificate-output.json\*](traefik/get-certificate-output.json "open original schema") |

## type Type

`string` ([must be route, internal or custom](get-certificate-output-oneof-0-properties-must-be-route-internal-or-custom.md))

## type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | :---------- |
| `"internal"` |             |
| `"custom"`   |             |
| `"route"`    |             |
