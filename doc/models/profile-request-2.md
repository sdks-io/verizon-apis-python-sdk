
# Profile Request 2

## Structure

`ProfileRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List of DeviceList2`](../../doc/models/device-list-2.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `account_name` | `string` | Optional | - |
| `carrier_name` | `string` | Optional | - |
| `reason_code` | `string` | Optional | - |
| `etf_waiver` | `bool` | Optional | **Default**: `True` |
| `check_fallback_profile` | `bool` | Optional | **Default**: `False` |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "carrierName": "the name of the mobile service provider",
  "reasonCode": "a short code for the reason action was taken",
  "etfWaiver": true,
  "checkFallbackProfile": false,
  "devices": [
    {
      "ids": [
        {
          "id": "id7",
          "kind": "iccid"
        },
        {
          "id": "id8",
          "kind": "imei"
        }
      ]
    },
    {
      "ids": [
        {
          "id": "id8",
          "kind": "imei"
        },
        {
          "id": "id9",
          "kind": "eid"
        },
        {
          "id": "id0",
          "kind": "esn"
        }
      ]
    }
  ]
}
```

