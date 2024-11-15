
# Device Group Update Request

Make changes to a device group, including changing the name and description, and adding or removing devices.

## Structure

`DeviceGroupUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices_to_add` | [`List[DeviceId]`](../../doc/models/device-id.md) | Optional | Zero or more devices to add to the device group, specified by device ID. The devices will be removed from their current device groups. You can use POST /devices/actions/list to get a list of all devices in the account. |
| `devices_to_remove` | [`List[DeviceId]`](../../doc/models/device-id.md) | Optional | Zero or more devices to remove from the device group, specified by device ID. The devices will be added to the default device group. |
| `new_group_description` | `str` | Optional | A new description for the device group. Do not include this parameter to leave the group description unchanged. |
| `new_group_name` | `str` | Optional | A new name for the device group. Do not include this parameter if you want to leave the group name unchanged. |

## Example (as JSON)

```json
{
  "newGroupName": "Western region tanks",
  "newGroupDescription": "All western region tank level monitors.",
  "devicesToAdd": [
    {
      "kind": "imei",
      "id": "990003420535537"
    }
  ],
  "devicesToRemove": [
    {
      "id": "id0",
      "kind": "kind8"
    },
    {
      "id": "id0",
      "kind": "kind8"
    }
  ]
}
```

