# Request path prefix Schema

```txt
http://schema.nethserver.org/traefik/set-route-input.json#/properties/path
```

A path prefix, the matching evaluation will be performed whit and without the trailing slash, eg /foo will match `/foo and `/foo/*, also `/foo/` will match /foo and /foo/*

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                    |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [set-route-input.json\*](traefik/set-route-input.json "open original schema") |

## path Type

`string` ([Request path prefix](set-route-input-properties-request-path-prefix.md))

## path Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^/.*$
```

[try pattern](https://regexr.com/?expression=%5E%2F.*%24 "try regular expression with regexr.com")

## path Examples

```json
"/foo"
```

```json
"/foo/"
```
