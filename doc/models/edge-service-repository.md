
# Edge Service Repository

## Structure

`EdgeServiceRepository`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Required | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `description` | `string` | Optional | **Constraints**: *Maximum Length*: `250`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-\s]{1,250}$` |
| `revision` | [`Revision`](../../doc/models/revision.md) | Optional | - |
| `vendor_information` | [`VendorInformation`](../../doc/models/vendor-information.md) | Optional | - |
| `mtype` | [`RepositoryResTypeEnum`](../../doc/models/repository-res-type-enum.md) | Required | **Constraints**: *Maximum Length*: `20` |
| `tag` | `string` | Optional | **Constraints**: *Maximum Length*: `50` |
| `endpoint` | `string` | Required | **Constraints**: *Maximum Length*: `50`, *Pattern*: `([a-z0-9-]+\:\/+)([^\/\s]+)([a-z0-9\-@\^=%&;\/~\+]*)[\?]?([^ \#\r\n]*)#?([^ \#\r\n]*)` |
| `reacheability` | [`ReacheabilityEnum`](../../doc/models/reacheability-enum.md) | Required | - |
| `ca_certificate` | `string` | Optional | Required if your repository uses a private certificate authencation.Please provide ur CA certificat in PEM format. |
| `agents` | `List of string` | Optional | **Constraints**: *Maximum Items*: `100` |
| `ssl_disabled` | `bool` | Optional | - |
| `credentials_type` | [`CredentialsTypeEnum`](../../doc/models/credentials-type-enum.md) | Optional | - |
| `credentials` | [`Credential`](../../doc/models/credential.md) | Optional | - |
| `ssh_key` | `string` | Optional | SSH Private Key in PEM format. |

## Example (as JSON)

```json
{
  "endpoint": "https://charts.bitnami.com/bitnami",
  "name": "example-repo",
  "reacheability": "Internet",
  "type": "Git",
  "description": "description0",
  "revision": {
    "version": "version2",
    "additionalParams": [
      {
        "key": "key3",
        "value": "value5"
      },
      {
        "key": "key4",
        "value": "value6"
      }
    ]
  },
  "vendorInformation": {
    "id": "id0",
    "name": "name0",
    "primaryEmail": "primaryEmail8",
    "secondaryEmail": "secondaryEmail6",
    "contactNumber": "contactNumber4"
  },
  "tag": "tag6",
  "CACertificate": "CACertificate8"
}
```

