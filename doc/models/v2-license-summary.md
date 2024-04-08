
# V2 License Summary

Summary of license assignment.

## Structure

`V2LicenseSummary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account identifier. |
| `total_license` | `int` | Optional | Total FOTA license count. |
| `assigned_licenses` | `int` | Required | Assigned FOTA license count. |
| `has_more_data` | `bool` | Required | True if there are more devices to retrieve. |
| `last_seen_device_id` | `str` | Optional | Last seen device identifier. |
| `max_page_size` | `int` | Required | Maximum page size. |
| `device_list` | [`List[V2LicenseDevice]`](../../doc/models/v2-license-device.md) | Optional | Device IMEI list. |

## Example (as JSON)

```json
{
  "accountName": "0402196254-00001",
  "totalLicense": 5000,
  "assignedLicenses": 4319,
  "hasMoreData": true,
  "lastSeenDeviceId": "1000",
  "maxPageSize": 10,
  "deviceList": [
    {
      "deviceId": "990003425730535",
      "assignmentTime": "2017-11-29T16:03:42.000Z"
    },
    {
      "deviceId": "990000473475989",
      "assignmentTime": "2017-11-29T16:03:42.000Z"
    },
    {
      "deviceId": "990000347475989",
      "assignmentTime": "2017-11-29T16:03:42.000Z"
    },
    {
      "deviceId": "990007303425535",
      "assignmentTime": "2017-11-29T16:03:42.000Z"
    }
  ]
}
```

