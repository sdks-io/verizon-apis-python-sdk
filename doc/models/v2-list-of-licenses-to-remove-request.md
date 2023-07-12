
# V2 List of Licenses to Remove Request

License cancellation candidate devices.

## Structure

`V2ListOfLicensesToRemoveRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `string` | Optional | List creation option. |
| `count` | `int` | Optional | The number of devices. |
| `device_list` | `List of string` | Required | Device IMEI list. |

## Example (as JSON)

```json
{
  "type": "append",
  "count": 2,
  "deviceList": [
    "990003425730535",
    "990000473475989"
  ]
}
```

