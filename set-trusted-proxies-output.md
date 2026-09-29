# set-trusted-proxies output Schema

```txt
http://schema.nethserver.org/traefik/set-trusted-proxies-output.json
```

Get the IP addresses that are trusted as front-end proxies

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [set-trusted-proxies-output.json](traefik/set-trusted-proxies-output.json "open original schema") |

## set-trusted-proxies output Type

`object` ([set-trusted-proxies output](set-trusted-proxies-output.md))

## set-trusted-proxies output Examples

```json
{
  "proxies": [
    "192.168.1.1",
    "192.168.1.2"
  ]
}
```

# set-trusted-proxies output Properties

| Property            | Type      | Required | Nullable       | Defined by                                                                                                                                                                |
| :------------------ | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [depth](#depth)     | `integer` | Optional | cannot be null | [set-trusted-proxies output](set-trusted-proxies-output-properties-depth.md "http://schema.nethserver.org/traefik/set-trusted-proxies-output.json#/properties/depth")     |
| [proxies](#proxies) | `array`   | Required | cannot be null | [set-trusted-proxies output](set-trusted-proxies-output-properties-proxies.md "http://schema.nethserver.org/traefik/set-trusted-proxies-output.json#/properties/proxies") |

## depth



`depth`

* is optional

* Type: `integer`

* cannot be null

* defined in: [set-trusted-proxies output](set-trusted-proxies-output-properties-depth.md "http://schema.nethserver.org/traefik/set-trusted-proxies-output.json#/properties/depth")

### depth Type

`integer`

### depth Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## proxies



`proxies`

* is required

* Type: `string[]`

* cannot be null

* defined in: [set-trusted-proxies output](set-trusted-proxies-output-properties-proxies.md "http://schema.nethserver.org/traefik/set-trusted-proxies-output.json#/properties/proxies")

### proxies Type

`string[]`
