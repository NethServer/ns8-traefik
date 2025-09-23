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

one (and only one) of

* [Untitled undefined type in delete-certificate input](set-certificate-input-oneof-0.md "check type definition")

* [Untitled undefined type in delete-certificate input](set-certificate-input-oneof-1.md "check type definition")

## delete-certificate input Examples

```json
{
  "path": "custom_certificates/mycert.crt",
  "type": "custom"
}
```

```json
{
  "serial": "548155130505306540286255320287329564948959",
  "type": "internal"
}
```

# delete-certificate input Properties

| Property          | Type     | Required | Nullable       | Defined by                                                                                                                                                  |
| :---------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type)     | `string` | Optional | cannot be null | [delete-certificate input](set-certificate-input-properties-type.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/type")     |
| [serial](#serial) | `string` | Optional | cannot be null | [delete-certificate input](set-certificate-input-properties-serial.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/serial") |
| [path](#path)     | `string` | Optional | cannot be null | [delete-certificate input](set-certificate-input-properties-path.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/path")     |

## type

Identify where the certificate is stored: internal (acme.json), custom (uploaded)

`type`

* is optional

* Type: `string`

* cannot be null

* defined in: [delete-certificate input](set-certificate-input-properties-type.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/type")

### type Type

`string`

## serial



`serial`

* is optional

* Type: `string`

* cannot be null

* defined in: [delete-certificate input](set-certificate-input-properties-serial.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/serial")

### serial Type

`string`

## path



`path`

* is optional

* Type: `string`

* cannot be null

* defined in: [delete-certificate input](set-certificate-input-properties-path.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/path")

### path Type

`string`
