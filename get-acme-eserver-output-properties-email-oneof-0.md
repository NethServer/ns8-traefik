# Untitled string in get-acme-server output Schema

```txt
http://schema.nethserver.org/traefik/get-acme-eserver-output.json#/properties/email/oneOf/0
```

Address for expiration notifications

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [get-acme-eserver-output.json\*](traefik/get-acme-eserver-output.json "open original schema") |

## 0 Type

`string`

## 0 Constraints

**email**: the string must be an email address, according to [RFC 5322, section 3.4.1](https://tools.ietf.org/html/rfc5322 "check the specification")
