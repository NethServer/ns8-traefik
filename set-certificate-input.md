# set-certificate input Schema

```txt
http://schema.nethserver.org/traefik/set-certificate-input.json
```

Request a let's encrypt certificate

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                              |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [set-certificate-input.json](traefik/set-certificate-input.json "open original schema") |

## set-certificate input Type

`object` ([set-certificate input](set-certificate-input.md))

## set-certificate input Examples

```json
{
  "fqdn": "example.com"
}
```

```json
{
  "fqdn": "example.com",
  "sync_timeout": 10
}
```

# set-certificate input Properties

| Property                       | Type      | Required | Nullable       | Defined by                                                                                                                                                           |
| :----------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [fqdn](#fqdn)                  | Merged    | Required | cannot be null | [set-certificate input](set-certificate-input-properties-fqdn.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/fqdn")                 |
| [sync\_timeout](#sync_timeout) | `integer` | Optional | cannot be null | [set-certificate input](set-certificate-input-properties-sync_timeout.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/sync_timeout") |

## fqdn

A fully qualified domain name

`fqdn`

* is required

* Type: `string` ([Details](set-certificate-input-properties-fqdn.md))

* cannot be null

* defined in: [set-certificate input](set-certificate-input-properties-fqdn.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/fqdn")

### fqdn Type

`string` ([Details](set-certificate-input-properties-fqdn.md))

one (and only one) of

* [Untitled undefined type in set-certificate input](set-certificate-input-properties-fqdn-oneof-0.md "check type definition")

* [Untitled undefined type in set-certificate input](set-certificate-input-properties-fqdn-oneof-1.md "check type definition")

## sync\_timeout

Max number of seconds to wait for the certificate to be obtained

`sync_timeout`

* is optional

* Type: `integer`

* cannot be null

* defined in: [set-certificate input](set-certificate-input-properties-sync_timeout.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/sync_timeout")

### sync\_timeout Type

`integer`

### sync\_timeout Constraints

**minimum**: the value of this number must greater than or equal to: `1`

### sync\_timeout Default Value

The default value is:

```json
30
```
