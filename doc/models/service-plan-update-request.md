
# Service Plan Update Request

Request to update service plan.

## Structure

`ServicePlanUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Optional | The name of a billing account. |
| `current_service_plan` | `string` | Optional | The name of a service plan, if you want to only include devices that have that service plan. |
| `custom_fields` | [`List of CustomFields`](../../doc/models/custom-fields.md) | Optional | Custom field names and values, if you want to only include devices that have matching values. |
| `devices` | [`List of AccountDeviceList`](../../doc/models/account-device-list.md) | Optional | A list of the devices that you want to change, specified by device identifier. |
| `group_name` | `string` | Optional | The name of a device group, if you want to restore service for all devices in that group. |
| `service_plan` | `string` | Optional | The service plan code that you want to assign to all specified devices. |

## Example (as JSON)

```json
{
  "devices": [
    {
      "deviceIds": [
        {
          "id": "A100003685E561",
          "kind": "meid"
        }
      ]
    }
  ],
  "servicePlan": "new_service_plan_code",
  "accountName": "accountName4",
  "currentServicePlan": "currentServicePlan6",
  "customFields": [
    {
      "key": "key0",
      "value": "value2"
    },
    {
      "key": "key1",
      "value": "value3"
    },
    {
      "key": "key2",
      "value": "value4"
    }
  ],
  "groupName": "groupName0"
}
```

