
# Anomaly Detection Settings

Settings for anomaly detection.

## Structure

`AnomalyDetectionSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Indicates if the account name used has anomaly detection.<br />Success - The account has anomaly detection.<br />Failure - The account does not have anomaly detection. |
| `sensitivity_parameter` | [`SensitivityParameters`](../../doc/models/sensitivity-parameters.md) | Optional | Details for sensitivity parameters. |
| `status` | `str` | Optional | Indicates if anomaly detection is active on the account<br />Active - Anomaly detection is active<br />Disabled- Anomaly detection is not active. |

## Example (as JSON)

```json
{
  "accountName": "Success",
  "sensitivityParameter": {
    "abnormalMaxValue": 1.1,
    "enableAbnormal": true,
    "enableVeryAbnormal": true,
    "veryAbnormalMaxValue": 0.55
  },
  "status": "Active"
}
```

