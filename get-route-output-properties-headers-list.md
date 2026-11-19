# Headers list Schema

```txt
http://schema.nethserver.org/traefik/get-route-output.json#/properties/headers
```

Headers to add or remove from an HTTP's request or response

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                      |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [get-route-output.json\*](traefik/get-route-output.json "open original schema") |

## headers Type

`object` ([Headers list](get-route-output-properties-headers-list.md))

# headers Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                               |
| :-------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [request](#request)   | `object` | Optional | cannot be null | [get-route output](get-route-output-properties-headers-list-properties-request.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/headers/properties/request")   |
| [response](#response) | `object` | Optional | cannot be null | [get-route output](get-route-output-properties-headers-list-properties-response.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/headers/properties/response") |

## request



`request`

* is optional

* Type: `object` ([Details](get-route-output-properties-headers-list-properties-request.md))

* cannot be null

* defined in: [get-route output](get-route-output-properties-headers-list-properties-request.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/headers/properties/request")

### request Type

`object` ([Details](get-route-output-properties-headers-list-properties-request.md))

## response



`response`

* is optional

* Type: `object` ([Details](get-route-output-properties-headers-list-properties-response.md))

* cannot be null

* defined in: [get-route output](get-route-output-properties-headers-list-properties-response.md "http://schema.nethserver.org/traefik/get-route-output.json#/properties/headers/properties/response")

### response Type

`object` ([Details](get-route-output-properties-headers-list-properties-response.md))
