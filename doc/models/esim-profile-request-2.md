
# ESIM Profile Request 2

## Structure

`ESIMProfileRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List[ESIMDeviceList]`](../../doc/models/esim-device-list.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `account_name` | `str` | Optional | - |
| `service_plan` | `str` | Optional | - |
| `mdn_zip_code` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "servicePlan": "The service plan name",
  "mdnZipCode": "five digit zip code",
  "devices": [
    {
      "deviceIds": [
        {
          "id": "id0",
          "kind": "kind8"
        }
      ]
    },
    {
      "deviceIds": [
        {
          "id": "id0",
          "kind": "kind8"
        }
      ]
    }
  ]
}
```

