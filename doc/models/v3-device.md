
# V3 Device

Device information.

## Structure

`V3Device`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `string` | Required | Device IMEI. |
| `request_status` | `string` | Optional | Success or failure. |
| `result_reason` | `string` | Optional | - |
| `mdn` | `string` | Optional | MDN. |
| `model` | `string` | Optional | Device model. |
| `make` | `string` | Optional | Device make. |
| `firmware` | `string` | Optional | Device firmware version. |
| `fota_eligible` | `bool` | Optional | Value=true if the device software can be upgraded over the air using the Software Management Services API. |
| `status` | `string` | Optional | Device status. |
| `license_assigned` | `bool` | Optional | License assigned device. |
| `protocol` | `string` | Optional | Firmware protocol. Valid values include: LWM2M, OMADM, HTTP or NONE. |
| `software_list` | [`List of V3SoftwareInfo`](../../doc/models/v3-software-info.md) | Optional | List of sofware.<br>**Constraints**: *Maximum Items*: `1000` |
| `file_list` | [`List of V3SoftwareInfo`](../../doc/models/v3-software-info.md) | Optional | List of files.<br>**Constraints**: *Maximum Items*: `1000` |
| `create_time` | `string` | Optional | The date and time of when the device is created. |
| `status_time` | `string` | Optional | The date and time of when the device firmware or software is updated. |
| `update_time` | `string` | Optional | The date and time of when the device is updated. |
| `refresh_time` | `string` | Optional | The date and time of when the device is refreshed. |
| `last_connection_time` | `datetime` | Optional | The date and time of when the device reachability is checked. |

## Example (as JSON)

```json
{
  "deviceId": "15-digit IMEI",
  "mdn": "10-digit MDN",
  "model": "GM01Q",
  "make": "SEQUANS COMMUNICATIONS",
  "firmware": "SR1.2.0.0-10657",
  "fotaEligible": true,
  "licenseAssigned": true,
  "status": "Active",
  "protocol": "LWM2M",
  "createTime": "2021-06-03 00:03:56.079 +0000 UTC",
  "statusTime": "2021-06-03 00:03:56.079 +0000 UTC",
  "refreshTime": "2021-06-03 00:03:56.079 +0000 UTC",
  "lastConnectionTime": "2012-04-23T18:25:43.511Z",
  "requestStatus": "requestStatus0",
  "resultReason": "resultReason0"
}
```

