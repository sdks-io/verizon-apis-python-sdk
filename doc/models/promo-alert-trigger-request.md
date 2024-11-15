
# Promo Alert Trigger Request

## Structure

`PromoAlertTriggerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data_percentage_50` | `bool` | Optional | - |
| `data_percentage_75` | `bool` | Optional | - |
| `data_percentage_90` | `bool` | Optional | - |
| `no_of_days_b_4_promo_exp` | `int` | Optional | **Constraints**: `>= 0`, `<= 180` |
| `sms_percentage_50` | `bool` | Optional | - |
| `sms_percentage_75` | `bool` | Optional | - |
| `sms_percentage_90` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "dataPercentage50": false,
  "dataPercentage75": false,
  "dataPercentage90": false,
  "noOfDaysB4PromoExp": 166,
  "smsPercentage50": false
}
```

