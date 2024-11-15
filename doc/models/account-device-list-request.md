
# Account Device List Request

Request for listing account devices.

## Structure

`AccountDeviceListRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The billing account for which a list of devices is returned. If you don't specify an accountName, the list includes all devices to which you have access. |
| `device_id` | [`DeviceId`](../../doc/models/device-id.md) | Optional | An identifier for a single device. |
| `filter` | [`AccountDeviceListFilter`](../../doc/models/account-device-list-filter.md) | Optional | Filter for a list of devices. |
| `current_state` | `str` | Optional | The name of a device state, to only include devices in that state. |
| `custom_fields` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | Custom field names and values, if you want to only include devices that have matching values. |
| `earliest` | `str` | Optional | Only include devices that were added after this date and time. |
| `group_name` | `str` | Optional | Only include devices that are in this device group. |
| `latest` | `str` | Optional | Only include devices that were added before this date and time. |
| `service_plan` | `str` | Optional | Only include devices that have this service plan. |
| `max_number_of_devices` | `int` | Optional | **Constraints**: `>= 0`, `<= 100` |
| `largest_device_id_seen` | `long\|int` | Optional | **Constraints**: `>= 0`, `<= 100` |

## Example (as JSON)

```json
{
  "accountName": "0786890242-00001",
  "filter": {
    "deviceIdentifierFilters": [
      {
        "kind": "iccid",
        "contains": "4259",
        "startswith": "startswith8",
        "endswith": "endswith0"
      }
    ]
  },
  "deviceId": {
    "id": "id0",
    "kind": "kind8"
  },
  "currentState": "currentState0",
  "customFields": [
    {
      "key": "key0",
      "value": "value2"
    },
    {
      "key": "key0",
      "value": "value2"
    }
  ]
}
```

