# list-routes output Schema

```txt
http://schema.nethserver.org/samba/list-routes-output.json
```

Return a list of configured routes

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                      |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [list-routes-output.json](samba/list-routes-output.json "open original schema") |

## list-routes output Type

an array of merged types ([Details](list-routes-output-1-items.md))

## list-routes output Examples

```json
[
  {
    "instance": "module1",
    "skip_cert_verify": false,
    "host": "host.domain.com",
    "path": "/Path",
    "url": "http://192.168.1.100",
    "lets_encrypt": false,
    "http2https": true,
    "user_created": true
  }
]
```

```json
[
  "module1"
]
```

```json
[]
```
