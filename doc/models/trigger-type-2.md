
# Trigger Type 2

Trigger details.

## Structure

`TriggerType2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `anomalyattributes` | [`UsageAnomalyAttributes`](../../doc/models/usage-anomaly-attributes.md) | Optional | The details of the UsageAnomaly trigger. |
| `notification` | [`Notification`](../../doc/models/notification.md) | Optional | The notification details of the trigger. |

## Example (as JSON)

```json
{
  "anomalyattributes": {
    "accountNames": "0000123456-00001",
    "deviceGroup": "User Group 1",
    "includeAbnormal": true,
    "includeVeryAbnormal": true,
    "includeUnderExpectedUsage": true,
    "includeOverExpectedUsage": true
  },
  "notification": {
    "notificationType": "DailySummary",
    "callback": true,
    "emailNotification": true,
    "notificationGroupName": "Anomaly Test API",
    "notificationFrequencyFactor": -2147483648,
    "externalEmailRecipients": "placeholder@verizon.com",
    "smsNotification": true,
    "smsNumbers": [
      {
        "carrier": "US Cellular",
        "number": "9299280711"
      }
    ],
    "reminder": false,
    "severity": "Critical"
  }
}
```

