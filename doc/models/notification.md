
# Notification

## Structure

`Notification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notification_type` | `str` | Optional | - |
| `callback` | `bool` | Optional | - |
| `email_notification` | `bool` | Optional | - |
| `notification_group_name` | `str` | Optional | - |
| `notification_frequency_factor` | `int` | Optional | - |
| `notification_frequency_interval` | `str` | Optional | - |
| `external_email_recipients` | `str` | Optional | - |
| `sms_notification` | `bool` | Optional | - |
| `sms_numbers` | [`List[SmsNumbers]`](../../doc/models/sms-numbers.md) | Optional | - |
| `reminder` | `bool` | Optional | - |
| `severity` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "notificationType": "notificationType2",
  "callback": false,
  "emailNotification": false,
  "notificationGroupName": "notificationGroupName2",
  "notificationFrequencyFactor": 214
}
```

