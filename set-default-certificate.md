# set-default-certificate input Schema

```txt
http://schema.nethserver.org/traefik/set-default-certificate.json
```

Change Traefik's configuration to obtain and enable a new default certificate with the required names

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [set-default-certificate.json](traefik/set-default-certificate.json "open original schema") |

## set-default-certificate input Type

`object` ([set-default-certificate input](set-default-certificate.md))

# set-default-certificate input Properties

| Property                       | Type      | Required | Nullable       | Defined by                                                                                                                                                                       |
| :----------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [check\_routes](#check_routes) | `boolean` | Optional | cannot be null | [set-default-certificate input](set-default-certificate-properties-check_routes.md "http://schema.nethserver.org/traefik/set-default-certificate.json#/properties/check_routes") |
| [sync\_timeout](#sync_timeout) | `integer` | Optional | cannot be null | [set-default-certificate input](set-default-certificate-properties-sync_timeout.md "http://schema.nethserver.org/traefik/set-default-certificate.json#/properties/sync_timeout") |
| [merge](#merge)                | `boolean` | Optional | cannot be null | [set-default-certificate input](set-default-certificate-properties-merge.md "http://schema.nethserver.org/traefik/set-default-certificate.json#/properties/merge")               |
| [names](#names)                | `array`   | Required | cannot be null | [set-default-certificate input](set-default-certificate-properties-names.md "http://schema.nethserver.org/traefik/set-default-certificate.json#/properties/names")               |

## check\_routes

Check if requested names are already used by HTTP routes

`check_routes`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [set-default-certificate input](set-default-certificate-properties-check_routes.md "http://schema.nethserver.org/traefik/set-default-certificate.json#/properties/check_routes")

### check\_routes Type

`boolean`

### check\_routes Default Value

The default value is:

```json
true
```

## sync\_timeout

Max number of seconds to wait for an ACME certificate response

`sync_timeout`

* is optional

* Type: `integer`

* cannot be null

* defined in: [set-default-certificate input](set-default-certificate-properties-sync_timeout.md "http://schema.nethserver.org/traefik/set-default-certificate.json#/properties/sync_timeout")

### sync\_timeout Type

`integer`

### sync\_timeout Default Value

The default value is:

```json
60
```

## merge

If true, the resulting certificate names will be the union of the current certificate names with the requested names.

`merge`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [set-default-certificate input](set-default-certificate-properties-merge.md "http://schema.nethserver.org/traefik/set-default-certificate.json#/properties/merge")

### merge Type

`boolean`

### merge Default Value

The default value is:

```json
false
```

## names



`names`

* is required

* Type: `string[]` ([Details](set-default-certificate-properties-names-items.md))

* cannot be null

* defined in: [set-default-certificate input](set-default-certificate-properties-names.md "http://schema.nethserver.org/traefik/set-default-certificate.json#/properties/names")

### names Type

`string[]` ([Details](set-default-certificate-properties-names-items.md))

### names Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

### names Examples

```json
[
  "www.nethserver.org",
  "*.nethserver.com"
]
```
