
# V3 Add or Remove Device Result

Add or remove devices to existing upgrade information.

## Structure

`V3AddOrRemoveDeviceResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account identifier. |
| `campaign_id` | `str` | Required | Campaign identifier. |
| `device_list` | [`List[V3DeviceListItem]`](../../doc/models/v3-device-list-item.md) | Required | Array of devices changed. |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "campaignId": "f858b8c4-2153-11ec-8c44-aeb16d1aa652",
  "deviceList": [
    {
      "deviceId": "15-digit IMEI",
      "status": "AddDeviceSucceed",
      "Reason": "Device added Successfully"
    }
  ]
}
```

