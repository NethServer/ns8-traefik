# get-route input Schema

```txt
http://schema.nethserver.org/traefik/get-route-input.json
```

Get a configured route

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [get-route-input.json](traefik/get-route-input.json "open original schema") |

## get-route input Type

`object` ([get-route input](get-route-input.md))

## get-route input Examples

```json
{
  "instance": "module1"
}
```

# get-route input Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                          |
| :-------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| [instance](#instance) | `string` | Required | cannot be null | [get-route input](get-route-input-properties-name-of-the-route.md "http://schema.nethserver.org/traefik/get-route-input.json#/properties/instance") |

## instance



`instance`

*   is required

*   Type: `string` ([Name of the route](get-route-input-properties-name-of-the-route.md))

*   cannot be null

*   defined in: [get-route input](get-route-input-properties-name-of-the-route.md "http://schema.nethserver.org/traefik/get-route-input.json#/properties/instance")

### instance Type

`string` ([Name of the route](get-route-input-properties-name-of-the-route.md))
