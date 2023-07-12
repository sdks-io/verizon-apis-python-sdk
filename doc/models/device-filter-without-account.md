
# Device Filter Without Account

Filter for devices without account.

## Structure

`DeviceFilterWithoutAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `group_name` | `string` | Optional | Only include devices that are in this device group. |
| `service_plan` | `string` | Optional | Only include devices that have this service plan. |
| `custom_fields` | [`List of CustomFields`](../../doc/models/custom-fields.md) | Optional | Custom field names and values, if you want to only include devices that have matching values. |

## Example (as JSON)

```json
{
  "groupName": "suspended devices",
  "servicePlan": "servicePlan0",
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
  ]
}
```

