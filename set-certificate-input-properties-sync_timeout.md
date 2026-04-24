# Untitled integer in set-certificate input Schema

```txt
http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/sync_timeout
```

Max number of seconds to wait for the certificate to be obtained

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [set-certificate-input.json\*](traefik/set-certificate-input.json "open original schema") |

## sync\_timeout Type

`integer`

## sync\_timeout Constraints

**minimum**: the value of this number must greater than or equal to: `1`

## sync\_timeout Default Value

The default value is:

```json
60
```
