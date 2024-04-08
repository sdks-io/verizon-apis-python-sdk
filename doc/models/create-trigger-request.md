
# Create Trigger Request

## Structure

`CreateTriggerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `anomaly_trigger_request` | [`AnomalyTriggerRequest`](../../doc/models/anomaly-trigger-request.md) | Optional | The details of the UsageAnomaly trigger. |
| `data_trigger_request` | [`DataTriggerRequest`](../../doc/models/data-trigger-request.md) | Optional | - |
| `group_name` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `name` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `session_trigger_request` | [`SessionTriggerRequest`](../../doc/models/session-trigger-request.md) | Optional | - |
| `sms_trigger_request` | [`SMSTriggerRequest`](../../doc/models/sms-trigger-request.md) | Optional | - |
| `trigger_category` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `trigger_cycle` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |

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
  "accountName": "accountName6",
  "dataTriggerRequest": {
    "comparator": "comparator2",
    "threshold": 242,
    "thresholdUnit": "thresholdUnit6"
  },
  "groupName": "groupName2",
  "name": "name2"
}
```

