# Headers list Schema

```txt
http://schema.nethserver.org/traefik/set-route-input.json#/properties/headers
```

Headers to add or remove from an HTTP's request or response

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                    |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [set-route-input.json\*](traefik/set-route-input.json "open original schema") |

## headers Type

`object` ([Headers list](set-route-input-properties-headers-list.md))

## headers Examples

```json
{
  "headers": {
    "request": {
      "X-foo-add": "foo",
      "X-bar-remove": ""
    },
    "response": {
      "X-bar-add": "bar",
      "X-foo-remove": ""
    }
  }
}
```

# headers Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                            |
| :-------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [request](#request)   | `object` | Optional | cannot be null | [set-route input](set-route-input-properties-headers-list-properties-request.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/headers/properties/request")   |
| [response](#response) | `object` | Optional | cannot be null | [set-route input](set-route-input-properties-headers-list-properties-response.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/headers/properties/response") |

## request



`request`

* is optional

* Type: `object` ([Details](set-route-input-properties-headers-list-properties-request.md))

* cannot be null

* defined in: [set-route input](set-route-input-properties-headers-list-properties-request.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/headers/properties/request")

### request Type

`object` ([Details](set-route-input-properties-headers-list-properties-request.md))

## response



`response`

* is optional

* Type: `object` ([Details](set-route-input-properties-headers-list-properties-response.md))

* cannot be null

* defined in: [set-route input](set-route-input-properties-headers-list-properties-response.md "http://schema.nethserver.org/traefik/set-route-input.json#/properties/headers/properties/response")

### response Type

`object` ([Details](set-route-input-properties-headers-list-properties-response.md))
