
# V3 Add or Remove Device Request

Devices to add or remove from existing software upgrade information.

## Structure

`V3AddOrRemoveDeviceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `string` | Required | Operation either 'append' or 'remove' |
| `device_list` | `List of string` | Required | Device IMEI list. |

## Example (as JSON)

```json
{
  "Type": "remove",
  "deviceList": [
    "15-digit IMEI"
  ]
}
```

