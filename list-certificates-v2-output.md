# list-certificates-v2 output Schema

```txt
http://schema.nethserver.org/traefik/list-certificates-v2-output.json
```

List the TLS certificates obtained by ACME or manually uploaded, with detailed attributes

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                          |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [list-certificates-v2-output.json](traefik/list-certificates-v2-output.json "open original schema") |

## list-certificates-v2 output Type

`object` ([list-certificates-v2 output](list-certificates-v2-output.md))

## list-certificates-v2 output Examples

```json
{
  "certificates": [
    {
      "names": [
        "mail.dp.nethserver.net"
      ],
      "subject": "mail.dp.nethserver.net",
      "issuer": "Custom Intermediate CA",
      "serial": "603545327999770137768033575467090432240151056165",
      "valid_to": "2026-02-07T14:19:38+00:00",
      "valid_from": "2025-02-07T14:19:38+00:00",
      "path": "custom_certificates/mail.dp.nethserver.net.crt",
      "validity": "valid",
      "type": "custom"
    },
    {
      "names": [
        "dokuwiki1.dp.nethserver.net"
      ],
      "subject": "dokuwiki1.dp.nethserver.net",
      "issuer": "(STAGING) Tenuous Tomato R13",
      "serial": "3918504633558580209040851109284865639469365",
      "valid_to": "2025-12-02T09:56:55+00:00",
      "valid_from": "2025-09-03T09:56:56+00:00",
      "validity": "valid",
      "type": "internal",
      "automatic": true
    },
    {
      "names": [
        "manual.dp.nethserver.net"
      ],
      "subject": "manual.dp.nethserver.net",
      "issuer": "(STAGING) Riddling Rhubarb R12",
      "serial": "3853031702502281198931684732356056127155675",
      "valid_to": "2025-12-02T10:06:40+00:00",
      "valid_from": "2025-09-03T10:06:41+00:00",
      "validity": "valid",
      "type": "internal"
    },
    {
      "names": [
        "rl1.dp.nethserver.net",
        "mail.dp.nethserver.net"
      ],
      "subject": "rl1.dp.nethserver.net",
      "issuer": "(STAGING) Riddling Rhubarb R12",
      "serial": "3865367987766600338566272990214152225581583",
      "valid_to": "2025-12-02T13:38:13+00:00",
      "valid_from": "2025-09-03T13:38:14+00:00",
      "validity": "valid",
      "type": "internal",
      "default": true
    }
  ]
}
```

# list-certificates-v2 output Properties

| Property                      | Type    | Required | Nullable       | Defined by                                                                                                                                                                             |
| :---------------------------- | :------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [certificates](#certificates) | `array` | Optional | cannot be null | [list-certificates-v2 output](list-certificates-v2-output-properties-certificates.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/properties/certificates") |

## certificates



`certificates`

* is optional

* Type: `object[]` ([Details](list-certificates-v2-output-defs-tlscert.md))

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-properties-certificates.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/properties/certificates")

### certificates Type

`object[]` ([Details](list-certificates-v2-output-defs-tlscert.md))

# list-certificates-v2 output Definitions

## Definitions group tlscert

Reference this group by using

```json
{"$ref":"http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert"}
```

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

### type

Possible values: internal (acme.json), custom (uploaded)

`type`

* is required

* Type: `string`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-type.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/type")

#### type Type

`string`

#### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | :---------- |
| `"internal"` |             |
| `"custom"`   |             |

### default

True, if the certificate names satisfy the default certificate configuration

`default`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-default.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/default")

#### default Type

`boolean`

### automatic

True, if the internal certificate is referenced by at least one HTTP route Let's Encrypt configuration

`automatic`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-automatic.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/automatic")

#### automatic Type

`boolean`

### obsolete

True, if the certificate is not referenced/used by current Traefik configuration

`obsolete`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-obsolete.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/obsolete")

#### obsolete Type

`boolean`

### names



`names`

* is required

* Type: `string[]`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-names.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/names")

#### names Type

`string[]`

### validity



`validity`

* is optional

* Type: unknown

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-validity.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/validity")

#### validity Type

unknown

#### validity Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | :---------- |
| `"valid"`    |             |
| `"expiring"` |             |
| `"expired"`  |             |

### subject



`subject`

* is optional

* Type: `string`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-subject.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/subject")

#### subject Type

`string`

### issuer



`issuer`

* is optional

* Type: `string`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-issuer.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/issuer")

#### issuer Type

`string`

### valid\_from



`valid_from`

* is optional

* Type: `string`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-valid_from.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/valid_from")

#### valid\_from Type

`string`

### valid\_to



`valid_to`

* is optional

* Type: `string`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-valid_to.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/valid_to")

#### valid\_to Type

`string`

### path

Filesystem path of the custom certificate. Other certificate types do not have this attribute.

`path`

* is optional

* Type: `string`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-path.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/path")

#### path Type

`string`

### serial



`serial`

* is optional

* Type: `string`

* cannot be null

* defined in: [list-certificates-v2 output](list-certificates-v2-output-defs-tlscert-properties-serial.md "http://schema.nethserver.org/traefik/list-certificates-v2-output.json#/$defs/tlscert/properties/serial")

#### serial Type

`string`
