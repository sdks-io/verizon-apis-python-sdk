
# Anomaly Detection Request

Anomaly detection request.

## Structure

`AnomalyDetectionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The name of a billing account. An account name is usually numeric, and must include any leading zeros.<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32` |
| `request_type` | `str` | Optional | The type of request being made. anomaly is the request to activate anomaly detection. |
| `sensitivity_parameter` | [`SensitivityParameters`](../../doc/models/sensitivity-parameters.md) | Optional | Details for sensitivity parameters. |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "requestType": "anomaly",
  "sensitivityParameter": {
    "abnormalMaxValue": 1.1,
    "enableAbnormal": true,
    "enableVeryAbnormal": true,
    "veryAbnormalMaxValue": 0.55
  }
}
```

