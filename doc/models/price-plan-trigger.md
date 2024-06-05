
# Price Plan Trigger

## Structure

`PricePlanTrigger`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_group_share` | [`AccountGroupShare`](../../doc/models/account-group-share.md) | Optional | - |

## Example (as JSON)

```json
{
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
```

