
# Usage Trigger Add Request

## Structure

`UsageTriggerAddRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_name` | `str` | Optional | Usage trigger name |
| `account_name` | `str` | Required | Account name |
| `service_name` | [`ServiceNameEnum`](../../doc/models/service-name-enum.md) | Required | Service name<br>**Default**: `'Location'` |
| `threshold_value` | `str` | Required | The percent of subscribed usage required to activate the trigger, such as 90 or 100. |
| `allow_excess` | `bool` | Optional | Allow additional requests after thresholdValue is reached. (currently not functional) |
| `send_sms_notification` | `bool` | Optional | Send SMS (text) alerts when the thresholdValue is reached. |
| `sms_phone_numbers` | `str` | Optional | Comma-separated list of phone numbers to send SMS alerts to. Digits only; no dashes or parentheses, etc. |
| `send_email_notification` | `bool` | Optional | Send email alerts when the thresholdValue is reached. |
| `email_addresses` | `str` | Optional | Comma-separated list of email addresses to send alerts to. |

## Example (as JSON)

```json
{
  "triggerName": "95% usage alert",
  "accountName": "0212312345-00001",
  "serviceName": "Location",
  "thresholdValue": "95",
  "smsPhoneNumbers": "5551231234",
  "emailAddresses": "you@theinternet.com",
  "allowExcess": false,
  "sendSmsNotification": false,
  "sendEmailNotification": false
}
```

