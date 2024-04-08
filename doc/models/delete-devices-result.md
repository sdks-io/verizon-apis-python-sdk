
# Delete Devices Result

Response for a request made to delete a device.

## Structure

`DeleteDevicesResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | `object` | Optional | One object per device to be deleted. Each object must contain a kind and id element identifying the device. |
| `status` | `str` | Optional | “Success” if the device was deleted, or “Failed” if there was a problem. |
| `message` | `str` | Optional | Not present if status=Success. One of these messages if status=Failed:The device is not in deactivate state.The user does not have access to delete the device. |

## Example (as JSON)

```json
{
  "deviceIds": {
    "key1": "val1",
    "key2": "val2"
  },
  "status": "Success",
  "message": "message6"
}
```

