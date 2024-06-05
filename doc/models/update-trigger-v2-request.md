
# Update Trigger V2 Request

Update Trigger Request

## Structure

`UpdateTriggerV2Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `str` | Optional | - |
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
  "triggerId": "triggerId4",
  "triggerName": "triggerName6",
  "ecpdId": "ecpdId0",
  "deviceGroupName": "deviceGroupName4",
  "triggerCategory": "triggerCategory8"
}
```

