
# V3 License Assigned Removed Result

License assignment/removal response.

## Structure

`V3LicenseAssignedRemovedResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account name. |
| `lic_count` | `int` | Required | Total license count. |
| `lic_used_count` | `int` | Required | Assigned license count. |
| `device_list` | [`List[V3DeviceStatus]`](../../doc/models/v3-device-status.md) | Required | List of devices with id in IMEI. |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "licUsedCount": 2,
  "licCount": 1000,
  "deviceList": [
    {
      "deviceId": "15-digit IMEI",
      "status": "UpgradePending",
      "resultReason": "Upgrade pending, the device upgrade is estimated to be scheduled for 06 Oct 22 18:05 UTC",
      "updatedTime": "2022-08-05T21:05:27.129Z",
      "recentAttemptTime": "2022-10-05T21:05:01.19Z",
      "nextAttemptTime": "2022-10-06T18:35:00Z"
    }
  ]
}
```

