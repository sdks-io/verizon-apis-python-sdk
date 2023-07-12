
# Device Firmware Version

Device and firmware information.

## Structure

`DeviceFirmwareVersion`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `string` | Optional | - |
| `reason` | `string` | Optional | - |
| `device_id` | `string` | Required | Device IMEI. |
| `firmware_version` | `string` | Required | Device Firmware Version. |
| `firmware_version_update_time` | `datetime` | Optional | - |

## Example (as JSON)

```json
{
  "deviceId": "15-digit IMEI",
  "status": "FirmwareVersionUpdateSuccess",
  "firmwareVersion": "SR1.2.0.0-10657",
  "reason": "reason4",
  "firmwareVersionUpdateTime": "2016-03-13T12:52:32.123Z"
}
```

