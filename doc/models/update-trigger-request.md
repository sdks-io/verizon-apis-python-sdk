
# Update Trigger Request

## Structure

`UpdateTriggerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `active` | `bool` | Optional | - |
| `anomaly_trigger_request` | [`AnomalyTriggerRequest`](../../doc/models/anomaly-trigger-request.md) | Optional | The details of the UsageAnomaly trigger. |
| `cycle_type` | [`CycleTypeEnum`](../../doc/models/cycle-type-enum.md) | Optional | - |
| `data_trigger_request` | [`DataTriggerRequest`](../../doc/models/data-trigger-request.md) | Optional | - |
| `group_name` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `promo_alert_trigger_request` | [`PromoAlertTriggerRequest`](../../doc/models/promo-alert-trigger-request.md) | Optional | - |
| `session_trigger_request` | [`SessionTriggerRequest`](../../doc/models/session-trigger-request.md) | Optional | - |
| `sms_trigger_request` | [`SMSTriggerRequest`](../../doc/models/sms-trigger-request.md) | Optional | - |
| `trigger_category` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `trigger_id` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `trigger_name` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |

## Example (as JSON)

```json
{
  "anomalyTriggerRequest": {
    "accountNames": "0000123456-00001",
    "includeAbnormal": true,
    "includeVeryAbnormal": true,
    "includeUnderExpectedUsage": true,
    "includeOverExpectedUsage": true
  },
  "accountName": "accountName0",
  "active": false,
  "cycleType": "cycleone",
  "dataTriggerRequest": {
    "comparator": "comparator2",
    "threshold": 242,
    "thresholdUnit": "thresholdUnit6"
  }
}
```

