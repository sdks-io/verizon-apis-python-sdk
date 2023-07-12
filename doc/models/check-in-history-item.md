
# Check in History Item

Check-in history for a device.

## Structure

`CheckInHistoryItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `string` | Required | Device IMEI. |
| `client_type` | `string` | Required | Type of client. |
| `result` | `string` | Required | - |
| `failure_type` | `string` | Required | - |
| `time_completed` | `datetime` | Required | - |

## Example (as JSON)

```json
{
  "deviceId": "990013907835573",
  "clientType": "clientType2",
  "result": "result6",
  "failureType": "failureType6",
  "timeCompleted": "10/22/2020 19:35:07"
}
```

