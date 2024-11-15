
# Device List Result

Device list information.

## Structure

`DeviceListResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account name. |
| `device_count` | `int` | Required | Total device count. |
| `device_list` | [`List[V3Device]`](../../doc/models/v3-device.md) | Required | List of devices with id in IMEI.<br>**Constraints**: *Maximum Items*: `1000` |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "deviceCount": 1,
  "deviceList": [
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
      "requestStatus": "requestStatus2",
      "resultReason": "resultReason2"
    }
  ]
}
```

