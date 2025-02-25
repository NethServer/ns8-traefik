# get-certificate output Schema

```txt
http://schema.nethserver.org/traefik/get-certificate-output.json
```

Status of a requested certificate

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [get-certificate-output.json](traefik/get-certificate-output.json "open original schema") |

## get-certificate output Type

`object` ([get-certificate output](get-certificate-output.md))

one (and only one) of

* [Untitled object in get-certificate output](get-certificate-output-oneof-0.md "check type definition")

* [Untitled object in get-certificate output](get-certificate-output-oneof-1.md "check type definition")

## get-certificate output Examples

```json
{
  "fqdn": "example.com",
  "obtained": true,
  "type": "internal"
}
```
