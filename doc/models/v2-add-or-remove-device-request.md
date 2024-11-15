
# V2 Add or Remove Device Request

Add or remove device to existing software upgrade information.

## Structure

`V2AddOrRemoveDeviceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required | Operation either 'append' or 'remove'. |
| `device_list` | `List[str]` | Required | Device IMEI list. |

## Example (as JSON)

```json
{
  "Type": "remove",
  "deviceList": [
    "990013907884259",
    "990013907835573",
    "990013907833575"
  ]
}
```

