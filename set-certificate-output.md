# set-certificate output Schema

```txt
http://schema.nethserver.org/traefik/set-certificate-output.json
```

State of the requested certificate

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [set-certificate-output.json](traefik/set-certificate-output.json "open original schema") |

## set-certificate output Type

`object` ([set-certificate output](set-certificate-output.md))

## set-certificate output Examples

```json
{
  "obtained": true
}
```

```json
{
  "obtained": false
}
```

# set-certificate output Properties

| Property              | Type      | Required | Nullable       | Defined by                                                                                                                                                                                            |
| :-------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [obtained](#obtained) | `boolean` | Required | cannot be null | [set-certificate output](set-certificate-output-properties-true-if-the-certificate-was-obtained-correctly.md "http://schema.nethserver.org/traefik/set-certificate-output.json#/properties/obtained") |

## obtained



`obtained`

* is required

* Type: `boolean` ([true if the certificate was obtained correctly](set-certificate-output-properties-true-if-the-certificate-was-obtained-correctly.md))

* cannot be null

* defined in: [set-certificate output](set-certificate-output-properties-true-if-the-certificate-was-obtained-correctly.md "http://schema.nethserver.org/traefik/set-certificate-output.json#/properties/obtained")

### obtained Type

`boolean` ([true if the certificate was obtained correctly](set-certificate-output-properties-true-if-the-certificate-was-obtained-correctly.md))
