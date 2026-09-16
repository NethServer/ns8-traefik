# get-certificate input Schema

```txt
http://schema.nethserver.org/traefik/get-certificate-input.json
```

Get certificates matching the fqdn parameter

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

| Property      | Type   | Required | Nullable       | Defined by                                                                                                                                           |
| :------------ | :----- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| [fqdn](#fqdn) | Merged | Required | cannot be null | [get-certificate input](get-certificate-input-properties-fqdn.md "http://schema.nethserver.org/traefik/get-certificate-input.json#/properties/fqdn") |

## fqdn

A fully qualified domain name

`fqdn`

* is required

* Type: `string` ([Details](get-certificate-input-properties-fqdn.md))

* cannot be null

* defined in: [get-certificate input](get-certificate-input-properties-fqdn.md "http://schema.nethserver.org/traefik/get-certificate-input.json#/properties/fqdn")

### fqdn Type

`string` ([Details](get-certificate-input-properties-fqdn.md))

one (and only one) of

* [Untitled undefined type in get-certificate input](get-certificate-input-properties-fqdn-oneof-0.md "check type definition")

* [Untitled undefined type in get-certificate input](get-certificate-input-properties-fqdn-oneof-1.md "check type definition")
