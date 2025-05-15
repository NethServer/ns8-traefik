# list-certificates output Schema

```txt
http://schema.nethserver.org/traefik/list-certificates-output.json
```

Return a list of requested certificates fqdn

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [list-certificates-output.json](traefik/list-certificates-output.json "open original schema") |

## list-certificates output Type

`array` ([list-certificates output](list-certificates-output.md))

any of

* [Untitled undefined type in list-certificates output](list-certificates-output-anyof-0.md "check type definition")

* [Untitled undefined type in list-certificates output](list-certificates-output-anyof-1.md "check type definition")

## list-certificates output Examples

```json
[]
```

```json
[
  "foo.domain.com",
  "nextcloud.domain.com",
  "webserver2.domain.com"
]
```

```json
[
  {
    "fqdn": "foo.domain.com",
    "type": "internal",
    "obtained": true
  },
  {
    "fqdn": "nextcloud.domain.com",
    "type": "route",
    "obtained": true
  },
  {
    "fqdn": "webserver2.domain.com",
    "type": "custom",
    "obtained": true
  }
]
```
