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
  "sync": true
}
```

```json
{
  "fqdn": "example.com",
  "sync": true,
  "sync_timeout": 300
}
```

# set-certificate input Properties

| Property                       | Type      | Required | Nullable       | Defined by                                                                                                                                                                    |
| :----------------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [fqdn](#fqdn)                  | `string`  | Required | cannot be null | [set-certificate input](set-certificate-input-properties-a-fully-qualified-domain-name.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/fqdn") |
| [sync](#sync)                  | `boolean` | Optional | cannot be null | [set-certificate input](set-certificate-input-properties-sync.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/sync")                          |
| [sync\_timeout](#sync_timeout) | `integer` | Optional | cannot be null | [set-certificate input](set-certificate-input-properties-sync_timeout.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/sync_timeout")          |

## fqdn



`fqdn`

*   is required

*   Type: `string` ([A fully qualified domain name](set-certificate-input-properties-a-fully-qualified-domain-name.md))

*   cannot be null

*   defined in: [set-certificate input](set-certificate-input-properties-a-fully-qualified-domain-name.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/fqdn")

### fqdn Type

`string` ([A fully qualified domain name](set-certificate-input-properties-a-fully-qualified-domain-name.md))

### fqdn Constraints

**hostname**: the string must be a hostname, according to [RFC 1123, section 2.1](https://tools.ietf.org/html/rfc1123 "check the specification")

## sync

Wait for the certificate to be obtained before return

`sync`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [set-certificate input](set-certificate-input-properties-sync.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/sync")

### sync Type

`boolean`

## sync\_timeout

Max number of seconds to wait for the certificate to be obtained

`sync_timeout`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [set-certificate input](set-certificate-input-properties-sync_timeout.md "http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/sync_timeout")

### sync\_timeout Type

`integer`

### sync\_timeout Constraints

**minimum**: the value of this number must greater than or equal to: `1`

### sync\_timeout Default Value

The default value is:

```json
120
```
