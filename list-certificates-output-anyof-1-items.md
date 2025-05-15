# Untitled object in list-certificates output Schema

```txt
http://schema.nethserver.org/traefik/list-certificates-output.json#/anyOf/1/items
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                      |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [list-certificates-output.json\*](traefik/list-certificates-output.json "open original schema") |

## items Type

`object` ([Details](list-certificates-output-anyof-1-items.md))

# items Properties

| Property              | Type      | Required | Nullable       | Defined by                                                                                                                                                                                        |
| :-------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [fqdn](#fqdn)         | `string`  | Required | cannot be null | [list-certificates output](list-certificates-output-anyof-1-items-properties-fqdn.md "http://schema.nethserver.org/traefik/list-certificates-output.json#/anyOf/1/items/properties/fqdn")         |
| [type](#type)         | `string`  | Required | cannot be null | [list-certificates output](list-certificates-output-anyof-1-items-properties-type.md "http://schema.nethserver.org/traefik/list-certificates-output.json#/anyOf/1/items/properties/type")         |
| [obtained](#obtained) | `boolean` | Required | cannot be null | [list-certificates output](list-certificates-output-anyof-1-items-properties-obtained.md "http://schema.nethserver.org/traefik/list-certificates-output.json#/anyOf/1/items/properties/obtained") |

## fqdn



`fqdn`

* is required

* Type: `string`

* cannot be null

* defined in: [list-certificates output](list-certificates-output-anyof-1-items-properties-fqdn.md "http://schema.nethserver.org/traefik/list-certificates-output.json#/anyOf/1/items/properties/fqdn")

### fqdn Type

`string`

### fqdn Constraints

**(international) hostname**: the string must be an (IDN) hostname, according to [RFC 5890, section 2.3.2.3](https://tools.ietf.org/html/rfc5890 "check the specification")

## type



`type`

* is required

* Type: `string`

* cannot be null

* defined in: [list-certificates output](list-certificates-output-anyof-1-items-properties-type.md "http://schema.nethserver.org/traefik/list-certificates-output.json#/anyOf/1/items/properties/type")

### type Type

`string`

### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | :---------- |
| `"internal"` |             |
| `"custom"`   |             |
| `"route"`    |             |

## obtained



`obtained`

* is required

* Type: `boolean`

* cannot be null

* defined in: [list-certificates output](list-certificates-output-anyof-1-items-properties-obtained.md "http://schema.nethserver.org/traefik/list-certificates-output.json#/anyOf/1/items/properties/obtained")

### obtained Type

`boolean`
