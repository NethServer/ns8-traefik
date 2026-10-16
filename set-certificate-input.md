# delete-certificate input Schema

```txt
http://schema.nethserver.org/traefik/set-certificate-input.json
```

Delete one or more TLS certificates matching the input

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                              |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [set-certificate-input.json](traefik/set-certificate-input.json "open original schema") |

## delete-certificate input Type

`object` ([delete-certificate input](set-certificate-input.md))

one (and only one) of

* [Untitled undefined type in delete-certificate input](set-certificate-input-oneof-0.md "check type definition")

* [Untitled undefined type in delete-certificate input](set-certificate-input-oneof-1.md "check type definition")

* [Untitled undefined type in delete-certificate input](set-certificate-input-oneof-2.md "check type definition")

## delete-certificate input Examples

```json
{
  "path": "custom_certificates/mycert.crt",
  "type": "custom"
}
```

```json
{
  "obsolete": true,
  "type": "internal"
}
```

```json
{
  "serial": "548155130505306540286255320287329564948959",
  "type": "internal"
}
```

# delete-certificate input Properties

| Property              | Type      | Required | Nullable       | Defined by                                                                                                                                                      |
| :-------------------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type)         | `string`  | Optional | cannot be null | [delete-certificate input](set-certificate-input-properties-type.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/type")         |
| [obsolete](#obsolete) | `boolean` | Optional | cannot be null | [delete-certificate input](set-certificate-input-properties-obsolete.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/obsolete") |
| [serial](#serial)     | `string`  | Optional | cannot be null | [delete-certificate input](set-certificate-input-properties-serial.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/serial")     |
| [path](#path)         | `string`  | Optional | cannot be null | [delete-certificate input](set-certificate-input-properties-path.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/path")         |

## type

Identify where the certificate is stored: internal (acme.json), custom (uploaded)

`type`

* is optional

* Type: `string`

* cannot be null

* defined in: [delete-certificate input](set-certificate-input-properties-type.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/type")

### type Type

`string`

## obsolete

Delete any internal certificate marked as obsolete

`obsolete`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [delete-certificate input](set-certificate-input-properties-obsolete.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/obsolete")

### obsolete Type

`boolean`

## serial

Delete the internal certificate with the given serial number

`serial`

* is optional

* Type: `string`

* cannot be null

* defined in: [delete-certificate input](set-certificate-input-properties-serial.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/serial")

### serial Type

`string`

## path

Delete the uploaded certificate with the given filesystem path

`path`

* is optional

* Type: `string`

* cannot be null

* defined in: [delete-certificate input](set-certificate-input-properties-path.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/path")

### path Type

`string`
