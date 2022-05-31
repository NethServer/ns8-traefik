# get-certificate output Schema

```txt
http://schema.nethserver.org/traefik/get-certificate-output.json
```

Status of a requested certificate

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [get-certificate-output.json](traefik/get-certificate-output.json "open original schema") |

## get-certificate output Type

`object` ([get-certificate output](get-certificate-output.md))

one (and only one) of

*   [Untitled undefined type in get-certificate output](get-certificate-output-oneof-0.md "check type definition")

*   [Untitled undefined type in get-certificate output](get-certificate-output-oneof-1.md "check type definition")

## get-certificate output Examples

```json
{
  "fqdn": "example.com",
  "obtained": "true"
}
```

# get-certificate output Properties

| Property              | Type      | Required | Nullable       | Defined by                                                                                                                                                                                            |
| :-------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [fqdn](#fqdn)         | `string`  | Optional | cannot be null | [get-certificate output](get-certificate-output-properties-a-fully-qualified-domain-name.md "http://schema.nethserver.org/traefik/get-certificate-output.json#/properties/fqdn")                      |
| [obtained](#obtained) | `boolean` | Optional | cannot be null | [get-certificate output](get-certificate-output-properties-true-if-the-certificate-was-obtained-correctly.md "http://schema.nethserver.org/traefik/get-certificate-output.json#/properties/obtained") |

## fqdn



`fqdn`

*   is optional

*   Type: `string` ([A fully qualified domain name](get-certificate-output-properties-a-fully-qualified-domain-name.md))

*   cannot be null

*   defined in: [get-certificate output](get-certificate-output-properties-a-fully-qualified-domain-name.md "http://schema.nethserver.org/traefik/get-certificate-output.json#/properties/fqdn")

### fqdn Type

`string` ([A fully qualified domain name](get-certificate-output-properties-a-fully-qualified-domain-name.md))

### fqdn Constraints

**hostname**: the string must be a hostname, according to [RFC 1123, section 2.1](https://tools.ietf.org/html/rfc1123 "check the specification")

## obtained



`obtained`

*   is optional

*   Type: `boolean` ([true if the certificate was obtained correctly](get-certificate-output-properties-true-if-the-certificate-was-obtained-correctly.md))

*   cannot be null

*   defined in: [get-certificate output](get-certificate-output-properties-true-if-the-certificate-was-obtained-correctly.md "http://schema.nethserver.org/traefik/get-certificate-output.json#/properties/obtained")

### obtained Type

`boolean` ([true if the certificate was obtained correctly](get-certificate-output-properties-true-if-the-certificate-was-obtained-correctly.md))
