# list-certificates input Schema

```txt
http://schema.nethserver.org/traefik/list-certificates-output.json
```

Get a list of requested certificates

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [list-certificates-output.json](traefik/list-certificates-output.json "open original schema") |

## list-certificates input Type

merged type ([list-certificates input](list-certificates-output.md))

one (and only one) of

* [Untitled object in list-certificates input](list-certificates-output-oneof-0.md "check type definition")

* [Untitled null in list-certificates input](list-certificates-output-oneof-1.md "check type definition")

## list-certificates input Examples

```json
{
  "expand_list": true
}
```
