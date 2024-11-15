
# V2 List of Licenses to Remove

A list of license cancellation candidate devices.

## Structure

`V2ListOfLicensesToRemove`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Required | Cancellation candidate devices count. |
| `has_more_data` | `bool` | Required | Flag to indicat more devices. |
| `update_time` | `str` | Required | Last update time. |
| `device_list` | `List[str]` | Required | Device IMEI list. |

## Example (as JSON)

```json
{
  "count": 6,
  "hasMoreData": false,
  "updateTime": "2018-03-22 00:06:00.069 +0000 UTC",
  "deviceList": [
    "990003425730535",
    "990000473475989",
    "990005733420535",
    "990000347475989",
    "990007303425535",
    "990007590473489"
  ]
}
```

