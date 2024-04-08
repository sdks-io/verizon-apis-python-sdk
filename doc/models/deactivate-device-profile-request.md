
# Deactivate Device Profile Request

## Structure

`DeactivateDeviceProfileRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | - |
| `reason_code` | `str` | Required | - |
| `devices` | [`List[DeactivateDeviceList]`](../../doc/models/deactivate-device-list.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `carrier_name` | `str` | Optional | - |
| `etf_waiver` | `bool` | Optional | **Default**: `True` |
| `check_fallback_profile` | `bool` | Optional | **Default**: `False` |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "reasonCode": "a short code for the reason action was taken",
  "carrierName": "the name of the mobile service provider",
  "etfWaiver": true,
  "checkFallbackProfile": false,
  "devices": [
    {
      "ids": [
        {
          "id": "id4",
          "kind": "kind2"
        },
        {
          "id": "id4",
          "kind": "kind2"
        },
        {
          "id": "id4",
          "kind": "kind2"
        }
      ]
    },
    {
      "ids": [
        {
          "id": "id4",
          "kind": "kind2"
        },
        {
          "id": "id4",
          "kind": "kind2"
        },
        {
          "id": "id4",
          "kind": "kind2"
        }
      ]
    },
    {
      "ids": [
        {
          "id": "id4",
          "kind": "kind2"
        },
        {
          "id": "id4",
          "kind": "kind2"
        },
        {
          "id": "id4",
          "kind": "kind2"
        }
      ]
    }
  ]
}
```

