# Request path prefix Schema

```txt
http://schema.nethserver.org/traefik/get-route-output.json#/properties/path
```

A path prefix, the matching evaluation will be performed whit and without the trailing slash, eg /foo will match `/foo and `/foo/*, also `/foo/` will match /foo and /foo/*

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                      |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [get-route-output.json\*](traefik/get-route-output.json "open original schema") |

## path Type

`string` ([Request path prefix](get-route-output-properties-request-path-prefix.md))

## path Examples

```json
"/foo"
```

```json
"/foo/"
```
