
# Device Log

Device logging information.

## Structure

`DeviceLog`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Required | Device IMEI. |
| `log_time` | `datetime` | Required | Time of log. |
| `log_type` | `str` | Required | Log type (one of SoftwareUpdate, Event, UserNotification, AgentService, Wireless, WirelessWeb, MobileBroadbandModem, WindowsMDM). |
| `event_log` | `str` | Required | Event log. |
| `binary_log_file_base_64` | `str` | Required | Base64-encoded contents of binary log file. |
| `binary_log_filename` | `str` | Required | File name of binary log file. |

## Example (as JSON)

```json
{
  "deviceId": "990013907835573",
  "logTime": "10/22/2020 19:29:50",
  "logType": "logType6",
  "eventLog": "eventLog0",
  "binaryLogFileBase64": "binaryLogFileBase644",
  "binaryLogFilename": "binaryLogFilename0"
}
```

