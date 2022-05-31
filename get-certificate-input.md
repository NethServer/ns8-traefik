# get-certificate input Schema

```txt
http://schema.nethserver.org/traefik/get-certificate-input.json
```

Get status of a requested certificate

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                              |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [get-certificate-input.json](traefik/get-certificate-input.json "open original schema") |

## get-certificate input Type

`object` ([get-certificate input](get-certificate-input.md))

## get-certificate input Examples

```json
{
  "fqdn": "example.com"
}
```

# get-certificate input Properties

| Property      | Type     | Required | Nullable       | Defined by                                                                                                                                                                    |
| :------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [fqdn](#fqdn) | `string` | Required | cannot be null | [get-certificate input](get-certificate-input-properties-a-fully-qualified-domain-name.md "http://schema.nethserver.org/traefik/get-certificate-input.json#/properties/fqdn") |

## fqdn



`fqdn`

*   is required

*   Type: `string` ([A fully qualified domain name](get-certificate-input-properties-a-fully-qualified-domain-name.md))

*   cannot be null

*   defined in: [get-certificate input](get-certificate-input-properties-a-fully-qualified-domain-name.md "http://schema.nethserver.org/traefik/get-certificate-input.json#/properties/fqdn")

### fqdn Type

`string` ([A fully qualified domain name](get-certificate-input-properties-a-fully-qualified-domain-name.md))

### fqdn Constraints

**hostname**: the string must be a hostname, according to [RFC 1123, section 2.1](https://tools.ietf.org/html/rfc1123 "check the specification")
