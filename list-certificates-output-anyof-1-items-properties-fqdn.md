# Untitled string in list-certificates output Schema

```txt
http://schema.nethserver.org/traefik/list-certificates-output.json#/anyOf/1/items/properties/fqdn
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                      |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [list-certificates-output.json\*](traefik/list-certificates-output.json "open original schema") |

## fqdn Type

`string`

## fqdn Constraints

**(international) hostname**: the string must be an (IDN) hostname, according to [RFC 5890, section 2.3.2.3](https://tools.ietf.org/html/rfc5890 "check the specification")
