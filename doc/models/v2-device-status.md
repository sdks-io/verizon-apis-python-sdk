
# V2 Device Status

Device with id in IMEI.

## Structure

`V2DeviceStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Required | Device IMEI. |
| `status` | `str` | Required | Success or failure. |
| `result_reason` | `str` | Optional | Result reason. |

## Example (as JSON)

```json
{
  "deviceId": "990000473475967",
  "status": "Failure",
  "resultReason": "Device does not exist."
}
```

