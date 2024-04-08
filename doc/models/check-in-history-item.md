
# Check in History Item

Check-in history for a device.

## Structure

`CheckInHistoryItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Required | Device IMEI. |
| `client_type` | `str` | Required | Type of client. |
| `result` | `str` | Required | - |
| `failure_type` | `str` | Required | - |
| `time_completed` | `datetime` | Required | - |

## Example (as JSON)

```json
{
  "deviceId": "990013907835573",
  "clientType": "clientType6",
  "result": "result8",
  "failureType": "failureType8",
  "timeCompleted": "10/22/2020 19:35:07"
}
```

