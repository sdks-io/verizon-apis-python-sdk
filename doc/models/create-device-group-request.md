
# Create Device Group Request

Create request for a new device group and optionally add devices to the group.

## Structure

`CreateDeviceGroupRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | The Verizon billing account that the device group will belong to. An account name is usually numeric, and must include any leading zeros. |
| `group_description` | `str` | Required | A description for the device group. |
| `group_name` | `str` | Required | The name for the new device group. This name must be unique within the specified account. |
| `devices_to_add` | [`List[DeviceId]`](../../doc/models/device-id.md) | Optional | Zero or more devices to add to the device group. You can use POST /devices/actions/list to get a list of all devices in the account. |

## Example (as JSON)

```json
{
  "accountName": "10001234-0001",
  "groupName": "NV tanks",
  "groupDescription": "Nevada tank level monitors.",
  "devicesToAdd": [
    {
      "kind": "imei",
      "id": "990003420535537"
    }
  ]
}
```

