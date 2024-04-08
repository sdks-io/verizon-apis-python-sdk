
# Notification

The notification details of the trigger.

## Structure

`Notification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notification_type` | `str` | Optional | The type of notification, i.e. 'DailySummary'. |
| `callback` | `bool` | Optional | Whether or not the notification should be sent via callback.<br />true<br />false. |
| `email_notification` | `bool` | Optional | Whether or not the notification should be sent via e-mail.<br />true<br />false. |
| `notification_group_name` | `str` | Optional | Name for the notification group. |
| `notification_frequency_factor` | `int` | Optional | Frequency factor for notification. |
| `notification_frequency_interval` | `str` | Optional | Frequency interval for notification. |
| `external_email_recipients` | `str` | Optional | E-mail address(es) where the notification should be delivered. |
| `sms_notification` | `bool` | Optional | SMS notification. |
| `sms_numbers` | [`List[SMSNumber]`](../../doc/models/sms-number.md) | Optional | List of SMS numbers.<br>**Constraints**: *Maximum Items*: `10` |
| `reminder` | `bool` | Optional | - |
| `severity` | `str` | Optional | Severity level associated with the notification. Examples would be:<br />Major<br />Minor<br />Critical<br />NotApplicable. |

## Example (as JSON)

```json
{
  "notificationType": "DailySummary",
  "callback": true,
  "emailNotification": false,
  "notificationGroupName": "Anomaly Test API",
  "notificationFrequencyFactor": 3,
  "notificationFrequencyInterval": "Hourly",
  "externalEmailRecipients": "placeholder@verizon.com",
  "smsNotification": true,
  "smsNumbers": [
    {
      "carrier": "US Cellular",
      "number": "9299280711"
    }
  ],
  "reminder": true,
  "severity": "Critical"
}
```

