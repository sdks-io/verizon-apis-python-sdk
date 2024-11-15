
# V3 Account Device List

Array of devices.

## Structure

`V3AccountDeviceList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account name. |
| `has_more_data` | `bool` | Required | Has more device flag? |
| `last_seen_device_id` | `str` | Optional | Last seen device identifier. |
| `max_page_size` | `int` | Required | Maximum page size. |
| `device_list` | [`List[V3AccountDevice]`](../../doc/models/v3-account-device.md) | Required | Account device list. |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "hasMoreData": true,
  "lastSeenDeviceId": "15-digit IMEI",
  "maxPageSize": 1000,
  "deviceList": [
    {
      "deviceId": "15-digit device ID",
      "mdn": "10-digit MDN",
      "model": "BG96",
      "make": "QUECTEL",
      "firmware": "BG96MAR04A04M1G",
      "fotaEligible": false,
      "status": "Active",
      "licenseAssigned": true,
      "protocol": "LWM2M",
      "softwareList": [
        {
          "name": "VZ_MDM_IOT",
          "version": "0.14",
          "upgradeTime": "2012-04-23T18:25:43.511Z"
        }
      ],
      "fileList": [
        {
          "name": "VZ_MDM_IOT",
          "version": "0.14",
          "upgradeTime": "2012-04-23T18:25:43.511Z"
        }
      ],
      "createTime": "2021-06-03 00:03:56.079 +0000 UTC",
      "upgradeTime": "2021-06-03 00:03:56.079 +0000 UTC",
      "updateTime": "2021-06-03 00:03:56.079 +0000 UTC",
      "refreshTime": "2021-06-03 00:03:56.079 +0000 UTC"
    }
  ]
}
```

