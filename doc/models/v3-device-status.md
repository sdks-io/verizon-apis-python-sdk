
# V3 Device Status

Device status.

## Structure

`V3DeviceStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Required | Device IMEI. |
| `status` | `str` | Required | Success or failure. |
| `result_reason` | `str` | Optional | Result reason. |
| `updated_time` | `datetime` | Optional | Updated Time. |
| `recent_attempt_time` | `datetime` | Optional | The most recent attempt time. |
| `next_attempt_time` | `datetime` | Optional | Next attempt time. |

## Example (as JSON)

```json
{
  "deviceId": "15-digit IMEI",
  "status": "UpgradePending",
  "resultReason": "Upgrade pending, the device upgrade is estimated to be scheduled for 06 Oct 22 18:05 UTC",
  "updatedTime": "2022-08-05T21:05:27.129Z",
  "recentAttemptTime": "2022-10-05T21:05:01.19Z",
  "nextAttemptTime": "2022-10-06T18:35:00Z"
}
```

