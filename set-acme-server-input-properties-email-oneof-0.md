# Untitled string in set-acme-server input Schema

```txt
http://schema.nethserver.org/traefik/set-acme-server-input.json#/properties/email/oneOf/0
```

Address for expiration notifications

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [set-acme-server-input.json\*](traefik/set-acme-server-input.json "open original schema") |

## 0 Type

`string`

## 0 Constraints

**email**: the string must be an email address, according to [RFC 5322, section 3.4.1](https://tools.ietf.org/html/rfc5322 "check the specification")
