# set-certificate output Schema

```txt
http://schema.nethserver.org/traefik/set-certificate-output.json
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [set-certificate-output.json](traefik/set-certificate-output.json "open original schema") |

## set-certificate output Type

`object` ([set-certificate output](set-certificate-output.md))

# set-certificate output Properties

| Property              | Type          | Required | Nullable       | Defined by                                                                                                                                                      |
| :-------------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [obtained](#obtained) | Not specified | Optional | cannot be null | [set-certificate output](set-certificate-output-properties-obtained.md "http://schema.nethserver.org/traefik/set-certificate-output.json#/properties/obtained") |

## obtained

Const value for backward compatibility. It can be ignored.

`obtained`

* is optional

* Type: unknown

* cannot be null

* defined in: [set-certificate output](set-certificate-output-properties-obtained.md "http://schema.nethserver.org/traefik/set-certificate-output.json#/properties/obtained")

### obtained Type

unknown

### obtained Constraints

**constant**: the value of this property must be equal to:

```json
true
```
