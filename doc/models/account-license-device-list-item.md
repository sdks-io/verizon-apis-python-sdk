
# Account License Device List Item

The list of devices that have licenses assigned, including the date and time of when each license was assigned.

## Structure

`AccountLicenseDeviceListItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Optional | Device IMEI. |
| `assignment_time` | `datetime` | Optional | Timestamp of when a license was assigned to the device. |

## Example (as JSON)

```json
{
  "deviceId": "990003425730535",
  "assignmentTime": "2017-11-29T16:03:42.000Z"
}
```

