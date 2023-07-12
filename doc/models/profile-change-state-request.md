
# Profile Change State Request

## Structure

`ProfileChangeStateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List of DeviceList`](../../doc/models/device-list.md) | Optional | - |
| `account_name` | `string` | Optional | - |
| `smsr_oid` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "accountName": "1223334444-00001",
  "smsrOid": "1.3.6.1.4.1.31746.1.500.200.101.5",
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

