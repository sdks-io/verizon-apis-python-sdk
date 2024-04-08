
# Firmware Upgrade

Array of upgrade objects with the specified status.

## Structure

`FirmwareUpgrade`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique identifier for this upgrade. |
| `account_name` | `str` | Optional | Account identifier in "##########-#####". |
| `firmware_name` | `str` | Optional | The name of the firmware image that will be used for the upgrade. |
| `firmware_to` | `str` | Optional | The name of the firmware version that will be on the devices after a successful upgrade. |
| `start_date` | `str` | Optional | The intended start date for the upgrade. |
| `status` | `str` | Optional | The current status of the upgrade. |
| `device_list` | [`List[FirmwareUpgradeDeviceListItem]`](../../doc/models/firmware-upgrade-device-list-item.md) | Optional | A JSON object for each device that was included in the upgrade, showing the device IMEI, the status of the upgrade, and additional information about the status. |

## Example (as JSON)

```json
{
  "id": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
  "accountName": "0402196254-00001",
  "firmwareName": "FOTA_Verizon_Model-A_01To02_HF",
  "firmwareTo": "VerizonFirmwareVersion-02",
  "startDate": "2018-04-01",
  "status": "Queued",
  "deviceList": [
    {
      "deviceId": "900000000000002",
      "status": "Device Accepted",
      "resultReason": "success"
    },
    {
      "deviceId": "900000000000003",
      "status": "Device Accepted",
      "resultReason": "success"
    }
  ]
}
```

