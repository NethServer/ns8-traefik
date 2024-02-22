# Untitled object in get-certificate output Schema

```txt
http://schema.nethserver.org/traefik/get-certificate-output.json#/oneOf/0
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [get-certificate-output.json\*](traefik/get-certificate-output.json "open original schema") |

## 0 Type

`object` ([Details](get-certificate-output-oneof-0.md))

# 0 Properties

| Property              | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                            |
| :-------------------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [fqdn](#fqdn)         | `string`  | Required | cannot be null | [get-certificate output](get-certificate-output-oneof-0-properties-a-fully-qualified-domain-name.md "http://schema.nethserver.org/traefik/get-certificate-output.json#/oneOf/0/properties/fqdn")                      |
| [type](#type)         | `string`  | Required | cannot be null | [get-certificate output](get-certificate-output-oneof-0-properties-must-be-route-internal-or-custom.md "http://schema.nethserver.org/traefik/get-certificate-output.json#/oneOf/0/properties/type")                   |
| [obtained](#obtained) | `boolean` | Required | cannot be null | [get-certificate output](get-certificate-output-oneof-0-properties-true-if-the-certificate-was-obtained-correctly.md "http://schema.nethserver.org/traefik/get-certificate-output.json#/oneOf/0/properties/obtained") |

## fqdn



`fqdn`

*   is required

*   Type: `string` ([A fully qualified domain name](get-certificate-output-oneof-0-properties-a-fully-qualified-domain-name.md))

*   cannot be null

*   defined in: [get-certificate output](get-certificate-output-oneof-0-properties-a-fully-qualified-domain-name.md "http://schema.nethserver.org/traefik/get-certificate-output.json#/oneOf/0/properties/fqdn")

### fqdn Type

`string` ([A fully qualified domain name](get-certificate-output-oneof-0-properties-a-fully-qualified-domain-name.md))

### fqdn Constraints

**hostname**: the string must be a hostname, according to [RFC 1123, section 2.1](https://tools.ietf.org/html/rfc1123 "check the specification")

## type



`type`

*   is required

*   Type: `string` ([must be route, internal or custom](get-certificate-output-oneof-0-properties-must-be-route-internal-or-custom.md))

*   cannot be null

*   defined in: [get-certificate output](get-certificate-output-oneof-0-properties-must-be-route-internal-or-custom.md "http://schema.nethserver.org/traefik/get-certificate-output.json#/oneOf/0/properties/type")

### type Type

`string` ([must be route, internal or custom](get-certificate-output-oneof-0-properties-must-be-route-internal-or-custom.md))

### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | :---------- |
| `"internal"` |             |
| `"custom"`   |             |
| `"route"`    |             |

## obtained



`obtained`

*   is required

*   Type: `boolean` ([true if the certificate was obtained correctly](get-certificate-output-oneof-0-properties-true-if-the-certificate-was-obtained-correctly.md))

*   cannot be null

*   defined in: [get-certificate output](get-certificate-output-oneof-0-properties-true-if-the-certificate-was-obtained-correctly.md "http://schema.nethserver.org/traefik/get-certificate-output.json#/oneOf/0/properties/obtained")

### obtained Type

`boolean` ([true if the certificate was obtained correctly](get-certificate-output-oneof-0-properties-true-if-the-certificate-was-obtained-correctly.md))
