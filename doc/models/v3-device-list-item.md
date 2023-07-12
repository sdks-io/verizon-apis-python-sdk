
# V3 Device List Item

Device changed.

## Structure

`V3DeviceListItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `string` | Optional | Device IMEI. |
| `status` | `string` | Optional | Success or failure. |
| `reason` | `string` | Optional | Result reason. |

## Example (as JSON)

```json
{
  "deviceId": "15-digit IMEI",
  "status": "AddDeviceSucceed",
  "Reason": "Device added Successfully"
}
```

