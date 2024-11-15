
# V2 List of Licenses to Remove Result

List of created license cancellation devices.

## Structure

`V2ListOfLicensesToRemoveResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Required | The number of devices. |
| `device_list` | `List[str]` | Required | Device IMEI list. |

## Example (as JSON)

```json
{
  "count": 2,
  "deviceList": [
    "990003425730535",
    "990000473475989"
  ]
}
```

