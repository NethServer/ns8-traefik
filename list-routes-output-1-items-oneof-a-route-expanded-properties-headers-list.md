# Headers list Schema

```txt
http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/headers
```

Headers to add or remove from an HTTP's request or response

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [list-routes-output.json\*](samba/list-routes-output.json "open original schema") |

## headers Type

`object` ([Headers list](list-routes-output-1-items-oneof-a-route-expanded-properties-headers-list.md))

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

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                |
| :-------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [request](#request)   | `object` | Optional | cannot be null | [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-headers-list-properties-request.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/headers/properties/request")   |
| [response](#response) | `object` | Optional | cannot be null | [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-headers-list-properties-response.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/headers/properties/response") |

## request



`request`

* is optional

* Type: `object` ([Details](list-routes-output-1-items-oneof-a-route-expanded-properties-headers-list-properties-request.md))

* cannot be null

* defined in: [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-headers-list-properties-request.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/headers/properties/request")

### request Type

`object` ([Details](list-routes-output-1-items-oneof-a-route-expanded-properties-headers-list-properties-request.md))

## response



`response`

* is optional

* Type: `object` ([Details](list-routes-output-1-items-oneof-a-route-expanded-properties-headers-list-properties-response.md))

* cannot be null

* defined in: [list-routes output](list-routes-output-1-items-oneof-a-route-expanded-properties-headers-list-properties-response.md "http://schema.nethserver.org/samba/list-routes-output.json#/items/oneOf/0/properties/headers/properties/response")

### response Type

`object` ([Details](list-routes-output-1-items-oneof-a-route-expanded-properties-headers-list-properties-response.md))
