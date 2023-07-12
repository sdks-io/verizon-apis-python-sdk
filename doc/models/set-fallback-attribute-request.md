
# Set Fallback Attribute Request

## Structure

`SetFallbackAttributeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List of DeviceList`](../../doc/models/device-list.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `account_name` | `string` | Optional | - |
| `carrier_name` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "carrierName": "the name of the mobile service provider",
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
    },
    {
      "deviceIds": [
        {
          "id": "id7",
          "kind": "eid"
        }
      ]
    }
  ]
}
```

