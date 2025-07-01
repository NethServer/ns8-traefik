# delete-certificate input Schema

```txt
http://schema.nethserver.org/traefik/set-certificate-input.json
```

Delete a configured TLS certificate

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                              |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [set-certificate-input.json](traefik/set-certificate-input.json "open original schema") |

## delete-certificate input Type

`object` ([delete-certificate input](set-certificate-input.md))

## delete-certificate input Examples

```json
{
  "fqdn": "example.com",
  "type": "internal"
}
```

```json
{
  "fqdn": "blog.example.net",
  "type": "custom"
}
```

# delete-certificate input Properties

| Property      | Type     | Required | Nullable       | Defined by                                                                                                                                              |
| :------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [type](#type) | `string` | Required | cannot be null | [delete-certificate input](set-certificate-input-properties-type.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/type") |
| [fqdn](#fqdn) | Merged   | Required | cannot be null | [delete-certificate input](set-certificate-input-properties-fqdn.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/fqdn") |

## type



`type`

* is required

* Type: `string`

* cannot be null

* defined in: [delete-certificate input](set-certificate-input-properties-type.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/type")

### type Type

`string`

### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | :---------- |
| `"custom"`   |             |
| `"internal"` |             |

## fqdn

A fully qualified domain name

`fqdn`

* is required

* Type: `string` ([Details](set-certificate-input-properties-fqdn.md))

* cannot be null

* defined in: [delete-certificate input](set-certificate-input-properties-fqdn.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/fqdn")

### fqdn Type

`string` ([Details](set-certificate-input-properties-fqdn.md))

one (and only one) of

* [Untitled undefined type in delete-certificate input](set-certificate-input-properties-fqdn-oneof-0.md "check type definition")

* [Untitled undefined type in delete-certificate input](set-certificate-input-properties-fqdn-oneof-1.md "check type definition")
