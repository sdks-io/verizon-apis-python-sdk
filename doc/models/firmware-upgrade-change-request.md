
# Firmware Upgrade Change Request

List of devices to add or remove.

## Structure

`FirmwareUpgradeChangeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`FirmwareTypeListEnum`](../../doc/models/firmware-type-list-enum.md) | Required | Possible values are `append` or `remove` |
| `device_list` | `List[str]` | Required | The IMEIs of the devices. |

## Example (as JSON)

```json
{
  "type": "append",
  "deviceList": [
    "15-digit IMEI",
    "15-digit IMEI"
  ]
}
```

