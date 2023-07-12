
# Virtual Machine

## Structure

`VirtualMachine`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `repository` | [`EdgeServiceRepository`](../../doc/models/edge-service-repository.md) | Required | - |
| `revision` | [`Revision`](../../doc/models/revision.md) | Optional | - |
| `template_type` | [`TemplateTypeEnum`](../../doc/models/template-type-enum.md) | Required | Type of the template to be used for deployment.<br>**Default**: `'Terraform'` |
| `values` | [`EdgeServiceRepository`](../../doc/models/edge-service-repository.md) | Optional | - |
| `provider` | [`CloudProviderEnum`](../../doc/models/cloud-provider-enum.md) | Optional | Cloud provider where you plan to provision and operate your Kubernetes cluster. |

## Example (as JSON)

```json
{
  "repository": {
    "endpoint": "https://charts.bitnami.com/bitnami",
    "name": "example-repo",
    "reacheability": "Internet",
    "type": "Git",
    "description": "description0",
    "revision": {
      "version": "version6",
      "additionalParams": [
        {
          "key": "key7",
          "value": "value9"
        },
        {
          "key": "key8",
          "value": "value0"
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
  },
  "revision": {
    "additionalParams": [],
    "version": "2.3.4"
  },
  "templateType": "Terraform",
  "values": {
    "endpoint": "https://charts.bitnami.com/bitnami",
    "name": "example-repo",
    "reacheability": "Internet",
    "type": "Git",
    "description": "description0",
    "revision": {
      "version": "version4",
      "additionalParams": [
        {
          "key": "key3",
          "value": "value5"
        },
        {
          "key": "key2",
          "value": "value4"
        },
        {
          "key": "key1",
          "value": "value3"
        }
      ]
    },
    "vendorInformation": {
      "id": "id0",
      "name": "name0",
      "primaryEmail": "primaryEmail8",
      "secondaryEmail": "secondaryEmail4",
      "contactNumber": "contactNumber4"
    },
    "tag": "tag4",
    "CACertificate": "CACertificate8"
  },
  "provider": "AWS"
}
```

