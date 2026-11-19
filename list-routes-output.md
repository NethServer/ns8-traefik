# list-routes input Schema

```txt
http://schema.nethserver.org/traefik/list-routes-output.json
```

Get a list of configured routes

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [list-routes-output.json](traefik/list-routes-output.json "open original schema") |

## list-routes input Type

merged type ([list-routes input](list-routes-output.md))

one (and only one) of

* [Untitled object in list-routes input](list-routes-output-oneof-0.md "check type definition")

* [Untitled null in list-routes input](list-routes-output-oneof-1.md "check type definition")

## list-routes input Examples

```json
{
  "expand_list": true
}
```
