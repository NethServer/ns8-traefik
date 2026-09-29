# set-trusted-proxies input Schema

```txt
http://schema.nethserver.org/traefik/set-trusted-proxies-input.json
```

Set the IP addresses that are trusted as front-end proxies

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                      |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [set-trusted-proxies-input.json](traefik/set-trusted-proxies-input.json "open original schema") |

## set-trusted-proxies input Type

`object` ([set-trusted-proxies input](set-trusted-proxies-input.md))

## set-trusted-proxies input Examples

```json
{
  "depth": 1,
  "proxies": [
    "192.168.1.1",
    "192.168.1.2"
  ]
}
```

# set-trusted-proxies input Properties

| Property            | Type      | Required | Nullable       | Defined by                                                                                                                                                             |
| :------------------ | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [depth](#depth)     | `integer` | Optional | cannot be null | [set-trusted-proxies input](set-trusted-proxies-input-properties-depth.md "http://schema.nethserver.org/traefik/set-trusted-proxies-input.json#/properties/depth")     |
| [proxies](#proxies) | `array`   | Required | cannot be null | [set-trusted-proxies input](set-trusted-proxies-input-properties-proxies.md "http://schema.nethserver.org/traefik/set-trusted-proxies-input.json#/properties/proxies") |

## depth



`depth`

* is optional

* Type: `integer`

* cannot be null

* defined in: [set-trusted-proxies input](set-trusted-proxies-input-properties-depth.md "http://schema.nethserver.org/traefik/set-trusted-proxies-input.json#/properties/depth")

### depth Type

`integer`

### depth Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## proxies



`proxies`

* is required

* Type: `string[]`

* cannot be null

* defined in: [set-trusted-proxies input](set-trusted-proxies-input-properties-proxies.md "http://schema.nethserver.org/traefik/set-trusted-proxies-input.json#/properties/proxies")

### proxies Type

`string[]`
