
# Device Logging Status

Device logging status information.

## Structure

`DeviceLoggingStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Required | Device IMEI. |
| `expiry_date` | `date` | Required | The date when device logging expires. |

## Example (as JSON)

```json
{
  "deviceId": "990013907835573",
  "expiryDate": "2020-10-19"
}
```

