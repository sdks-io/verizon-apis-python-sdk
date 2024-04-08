
# Firmware Upgrade Change Result

Upgrade information.

## Structure

`FirmwareUpgradeChangeResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Account identifier in "##########-#####". |
| `id` | `str` | Optional | The unique identifier for this upgrade. |
| `device_list` | [`List[V1DeviceListItem]`](../../doc/models/v1-device-list-item.md) | Optional | A JSON object for each device that was included in the request, showing the device IMEI, the status of the addition or removal, and additional information about the status. |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "id": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
  "deviceList": [
    {
      "deviceId": "15-digit IMEI",
      "status": "AddDeviceSucceed",
      "Reason": "Device added Successfully"
    },
    {
      "deviceId": "15-digit IMEI",
      "status": "AddDeviceSucceed",
      "Reason": "Device added Successfully"
    }
  ]
}
```

