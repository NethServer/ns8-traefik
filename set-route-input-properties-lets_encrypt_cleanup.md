# Untitled boolean in set-route input Schema

```txt
http://schema.nethserver.org/traefik/set-route-input.json#/properties/lets_encrypt_cleanup
```

If true and lets\_encrypt attribute is false, the Let's Encrypt certificate is removed and Traefik is restarted if needed.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                    |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [set-route-input.json\*](traefik/set-route-input.json "open original schema") |

## lets\_encrypt\_cleanup Type

`boolean`

## lets\_encrypt\_cleanup Default Value

The default value is:

```json
false
```
