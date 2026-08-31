# Untitled object in list-certificates-v2 output Schema

```txt
http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert
```

TLS certificate object

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                            |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [list-certificates-v2-output.json\*](traefik/list-certificates-v2-output.json "open original schema") |

## tlscert Type

`object` ([Details](list-certificates-v2-output-defs-tlscert.md))

# tlscert Properties

| Property                   | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                    |
| :------------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [type](#type)              | `string`      | Required | cannot be null | [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-type.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/type")             |
| [default](#default)        | `boolean`     | Optional | cannot be null | [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-default.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/default")       |
| [automatic](#automatic)    | `boolean`     | Optional | cannot be null | [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-automatic.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/automatic")   |
| [obsolete](#obsolete)      | `boolean`     | Optional | cannot be null | [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-obsolete.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/obsolete")     |
| [names](#names)            | `array`       | Required | cannot be null | [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-names.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/names")           |
| [validity](#validity)      | Not specified | Optional | cannot be null | [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-validity.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/validity")     |
| [subject](#subject)        | `string`      | Optional | cannot be null | [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-subject.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/subject")       |
| [issuer](#issuer)          | `string`      | Optional | cannot be null | [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-issuer.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/issuer")         |
| [valid\_from](#valid_from) | `string`      | Optional | cannot be null | [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-valid_from.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/valid_from") |
| [valid\_to](#valid_to)     | `string`      | Optional | cannot be null | [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-valid_to.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/valid_to")     |
| [path](#path)              | `string`      | Optional | cannot be null | [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-path.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/path")             |
| [serial](#serial)          | `string`      | Optional | cannot be null | [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-serial.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/serial")         |

## type

Possible values: internal (acme.json), custom (uploaded)

`type`

* is required

* Type: `string`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-type.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/type")

### type Type

`string`

### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | :---------- |
| `"internal"` |             |
| `"custom"`   |             |

## default

True, if the certificate names satisfy the default certificate configuration

`default`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-default.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/default")

### default Type

`boolean`

## automatic

True, if the internal certificate is referenced by at least one HTTP route Let's Encrypt configuration

`automatic`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-automatic.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/automatic")

### automatic Type

`boolean`

## obsolete

True, if the certificate is not referenced/used by current Traefik configuration

`obsolete`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-obsolete.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/obsolete")

### obsolete Type

`boolean`

## names



`names`

* is required

* Type: `string[]`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-names.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/names")

### names Type

`string[]`

## validity



`validity`

* is optional

* Type: unknown

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-validity.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/validity")

### validity Type

unknown

### validity Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | :---------- |
| `"valid"`    |             |
| `"expiring"` |             |
| `"expired"`  |             |

## subject



`subject`

* is optional

* Type: `string`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-subject.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/subject")

### subject Type

`string`

## issuer



`issuer`

* is optional

* Type: `string`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-issuer.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/issuer")

### issuer Type

`string`

## valid\_from



`valid_from`

* is optional

* Type: `string`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-valid_from.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/valid_from")

### valid\_from Type

`string`

## valid\_to



`valid_to`

* is optional

* Type: `string`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-valid_to.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/valid_to")

### valid\_to Type

`string`

## path

Filesystem path of the custom certificate. Other certificate types do not have this attribute.

`path`

* is optional

* Type: `string`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-path.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/path")

### path Type

`string`

## serial



`serial`

* is optional

* Type: `string`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-serial.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/serial")

### serial Type

`string`
