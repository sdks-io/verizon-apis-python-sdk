
# Service Plan Update Request

Request to update service plan.

## Structure

`ServicePlanUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_plan` | `str` | Required | The service plan code that you want to assign to all specified devices. |
| `account_name` | `str` | Optional | The name of a billing account. |
| `current_service_plan` | `str` | Optional | The name of a service plan, if you want to only include devices that have that service plan. |
| `custom_fields` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | Custom field names and values, if you want to only include devices that have matching values. |
| `devices` | [`List[AccountDeviceList]`](../../doc/models/account-device-list.md) | Optional | A list of the devices that you want to change, specified by device identifier. |
| `group_name` | `str` | Optional | The name of a device group, if you want to restore service for all devices in that group. |
| `carrier_ip_pool_name` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `take_effect` | `datetime` | Optional | - |

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
      ],
      "ipAddress": "ipAddress4"
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
      "key": "key0",
      "value": "value2"
    }
  ],
  "groupName": "groupName0"
}
```

