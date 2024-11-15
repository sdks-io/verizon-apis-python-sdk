
# GIO Deactivate Device Profile Request

## Structure

`GIODeactivateDeviceProfileRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List[GIODeviceList]`](../../doc/models/gio-device-list.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `account_name` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9\-]{3,32}$` |
| `service_plan` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9 ]{3,32}$` |
| `etf_waiver` | `bool` | Optional | **Default**: `False` |
| `reason_code` | `str` | Optional | **Constraints**: *Minimum Length*: `2`, *Maximum Length*: `32`, *Pattern*: `^[0-9A-Z]{2,32}$` |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "servicePlan": "service plan name",
  "etfWaiver": false,
  "reasonCode": "FF",
  "devices": [
    {
      "deviceIds": [
        {
          "kind": "kind8",
          "id": "id0"
        }
      ]
    }
  ]
}
```

