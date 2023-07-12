
# Device Suspension Status Request

Request to return service suspension information about one or more devices.

## Structure

`DeviceSuspensionStatusRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | [`List of DeviceId`](../../doc/models/device-id.md) | Optional | The devices that you want to include in the request, specified by device identifier. You only need to provide one identifier per device. |
| `filter` | [`DeviceFilterWithoutAccount`](../../doc/models/device-filter-without-account.md) | Optional | Filter for devices without account. |
| `account_name` | `string` | Optional | The name of a billing account. |

## Example (as JSON)

```json
{
  "filter": {
    "groupName": "suspended devices",
    "servicePlan": "servicePlan6",
    "customFields": [
      {
        "key": "key4",
        "value": "value6"
      },
      {
        "key": "key5",
        "value": "value7"
      },
      {
        "key": "key6",
        "value": "value8"
      }
    ]
  },
  "accountName": "1223334444-00001",
  "deviceIds": [
    {
      "id": "id0",
      "kind": "kind8"
    },
    {
      "id": "id1",
      "kind": "kind9"
    },
    {
      "id": "id2",
      "kind": "kind0"
    }
  ]
}
```

