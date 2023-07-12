
# Device Upload Request

## Structure

`DeviceUploadRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Required | - |
| `devices` | [`List of DeviceList`](../../doc/models/device-list.md) | Required | - |
| `email_address` | `string` | Required | - |
| `device_sku` | `string` | Required | - |
| `upload_type` | `string` | Required | - |

## Example (as JSON)

```json
{
  "accountName": "1223334444-00001",
  "devices": [
    {
      "deviceIds": [
        {
          "id": "id6",
          "kind": "imei"
        },
        {
          "id": "id7",
          "kind": "eid"
        },
        {
          "id": "id8",
          "kind": "esn"
        }
      ]
    }
  ],
  "emailAddress": "bob@mycompany.com",
  "deviceSku": "VZW123456",
  "uploadType": "IMEI"
}
```

