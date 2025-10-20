# Untitled boolean in set-certificate input Schema

```txt
http://schema.nethserver.org/traefik/set-certificate-input.json#/properties/lets_encrypt
```

When true, request Let's Encrypt certificate; when false, remove the certificate from acme.json and restart Traefik if needed

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [set-certificate-input.json\*](traefik/set-certificate-input.json "open original schema") |

## lets\_encrypt Type

`boolean`

## lets\_encrypt Default Value

The default value is:

```json
true
```
