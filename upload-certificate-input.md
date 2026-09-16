# upload-certificate input Schema

```txt
http://schema.nethserver.org/traefik/upload-certificate-input.json
```

Upload a certificate to be used by Traefik

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [upload-certificate-input.json](traefik/upload-certificate-input.json "open original schema") |

## upload-certificate input Type

`object` ([upload-certificate input](upload-certificate-input.md))

## upload-certificate input Examples

```json
{
  "certFile": "LS0tLS1CRUdJTiBDRVJUSUZJ...",
  "keyFile": "LS0tLS1CRUdJTiBSU0EgU..."
}
```

# upload-certificate input Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                            |
| :-------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [certFile](#certfile) | `string` | Required | cannot be null | [upload-certificate input](upload-certificate-input-properties-certfile.md "http://schema.nethserver.org/traefik/upload-certificate-input.json#/properties/certFile") |
| [keyFile](#keyfile)   | `string` | Required | cannot be null | [upload-certificate input](upload-certificate-input-properties-keyfile.md "http://schema.nethserver.org/traefik/upload-certificate-input.json#/properties/keyFile")   |

## certFile

Base64 Encode of the certificate.

`certFile`

* is required

* Type: `string`

* cannot be null

* defined in: [upload-certificate input](upload-certificate-input-properties-certfile.md "http://schema.nethserver.org/traefik/upload-certificate-input.json#/properties/certFile")

### certFile Type

`string`

## keyFile

Base64 Encode of the key file used to generate the certificate.

`keyFile`

* is required

* Type: `string`

* cannot be null

* defined in: [upload-certificate input](upload-certificate-input-properties-keyfile.md "http://schema.nethserver.org/traefik/upload-certificate-input.json#/properties/keyFile")

### keyFile Type

`string`
