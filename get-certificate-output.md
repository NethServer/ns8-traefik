# get-certificate output Schema

```txt
http://schema.nethserver.org/traefik/get-certificate-output.json
```

Get one or more certificates for the given FQDN.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [get-certificate-output.json](traefik/get-certificate-output.json "open original schema") |

## get-certificate output Type

`object` ([get-certificate output](get-certificate-output.md))

## get-certificate output Examples

```json
{
  "fqdn": "example.com",
  "obtained": true,
  "type": "internal",
  "certificates": [
    {
      "cert": "LS0tLS1CRUdJTiBDRVJUSUZJQ0F...",
      "key": "LS0tLS1CRUdJTiBQUklWQVRFIEt..."
    }
  ]
}
```

# get-certificate output Properties

| Property                      | Type      | Required | Nullable       | Defined by                                                                                                                                                                                            |
| :---------------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [fqdn](#fqdn)                 | `string`  | Required | cannot be null | [get-certificate output](get-certificate-output-properties-a-fully-qualified-domain-name.md "http://schema.nethserver.org/traefik/get-certificate-output.json#/properties/fqdn")                      |
| [type](#type)                 | `string`  | Required | cannot be null | [get-certificate output](get-certificate-output-properties-type.md "http://schema.nethserver.org/traefik/get-certificate-output.json#/properties/type")                                               |
| [certificates](#certificates) | `array`   | Required | cannot be null | [get-certificate output](get-certificate-output-properties-certificates.md "http://schema.nethserver.org/traefik/get-certificate-output.json#/properties/certificates")                               |
| [obtained](#obtained)         | `boolean` | Required | cannot be null | [get-certificate output](get-certificate-output-properties-true-if-the-certificate-was-obtained-correctly.md "http://schema.nethserver.org/traefik/get-certificate-output.json#/properties/obtained") |

## fqdn



`fqdn`

* is required

* Type: `string` ([A fully qualified domain name](get-certificate-output-properties-a-fully-qualified-domain-name.md))

* cannot be null

* defined in: [get-certificate output](get-certificate-output-properties-a-fully-qualified-domain-name.md "http://schema.nethserver.org/traefik/get-certificate-output.json#/properties/fqdn")

### fqdn Type

`string` ([A fully qualified domain name](get-certificate-output-properties-a-fully-qualified-domain-name.md))

## type



`type`

* is required

* Type: `string`

* cannot be null

* defined in: [get-certificate output](get-certificate-output-properties-type.md "http://schema.nethserver.org/traefik/get-certificate-output.json#/properties/type")

### type Type

`string`

### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | :---------- |
| `"internal"`   |             |
| `"custom"`     |             |
| `"selfsigned"` |             |

## certificates

List of certificates for FQDN, ordered by relevance (high first).

`certificates`

* is required

* Type: `object[]` ([Details](get-certificate-output-properties-certificates-items.md))

* cannot be null

* defined in: [get-certificate output](get-certificate-output-properties-certificates.md "http://schema.nethserver.org/traefik/get-certificate-output.json#/properties/certificates")

### certificates Type

`object[]` ([Details](get-certificate-output-properties-certificates-items.md))

## obtained



`obtained`

* is required

* Type: `boolean` ([true if the certificate was obtained correctly](get-certificate-output-properties-true-if-the-certificate-was-obtained-correctly.md))

* cannot be null

* defined in: [get-certificate output](get-certificate-output-properties-true-if-the-certificate-was-obtained-correctly.md "http://schema.nethserver.org/traefik/get-certificate-output.json#/properties/obtained")

### obtained Type

`boolean` ([true if the certificate was obtained correctly](get-certificate-output-properties-true-if-the-certificate-was-obtained-correctly.md))
