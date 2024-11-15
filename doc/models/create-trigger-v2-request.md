
# Create Trigger V2 Request

Create Trigger Request

## Structure

`CreateTriggerV2Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_name` | `str` | Optional | - |
| `ecpd_id` | `str` | Optional | - |
| `device_group_name` | `str` | Optional | - |
| `trigger_category` | `str` | Optional | - |
| `price_plan_trigger` | [`PricePlanTrigger`](../../doc/models/price-plan-trigger.md) | Optional | - |
| `notification` | [`Notification`](../../doc/models/notification.md) | Optional | - |
| `active` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "triggerName": "triggerName4",
  "ecpdId": "ecpdId0",
  "deviceGroupName": "deviceGroupName4",
  "triggerCategory": "triggerCategory8",
  "pricePlanTrigger": {
    "accountGroupShare": {
      "accountGroupShareIndividual": {
        "filterCriteria": {
          "ratePlanGroupId": 202
        },
        "condition": {
          "action": "action6"
        },
        "action": {
          "changePlan": {
            "triggerDate": "triggerDate6",
            "sharePlan": [
              {
                "fromCarrierCode": "fromCarrierCode6",
                "toCarrierCode": "toCarrierCode8",
                "criteriaPercentage": 170
              },
              {
                "fromCarrierCode": "fromCarrierCode6",
                "toCarrierCode": "toCarrierCode8",
                "criteriaPercentage": 170
              },
              {
                "fromCarrierCode": "fromCarrierCode6",
                "toCarrierCode": "toCarrierCode8",
                "criteriaPercentage": 170
              }
            ]
          }
        }
      }
    }
  }
}
```

