# Untitled array in set-default-certificate input Schema

```txt
http://schema.nethserver.org/traefik/set-default-certificate.json#/properties/names
```



| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [set-default-certificate.json\*](traefik/set-default-certificate.json "open original schema") |

## names Type

`string[]` ([Details](set-default-certificate-properties-names-items.md))

## names Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## names Examples

```json
[
  "www.nethserver.org",
  "*.nethserver.com"
]
```
