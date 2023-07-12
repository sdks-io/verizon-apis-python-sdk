
# Device Upgrade History

Firmware upgrade information.

## Structure

`DeviceUpgradeHistory`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `string` | Optional | Device IMEI. |
| `id` | `string` | Optional | The unique identifier for the upgrade. |
| `account_name` | `string` | Optional | The name (number) of the billing account that the device belongs to. |
| `firmware_from` | `string` | Optional | The firmware version that was on the device before the upgrade. |
| `firmware_to` | `string` | Optional | The name of the firmware version that was on the device after the upgrade. |
| `start_date` | `string` | Optional | The date of the upgrade. |
| `upgrade_start_time` | `string` | Optional | The date and time that the upgrade actually started for this device. |
| `status` | `string` | Optional | The status of the upgrade for this device. |
| `reason` | `string` | Optional | More information about the status. |

## Example (as JSON)

```json
{
  "deviceId": "900000000000001",
  "id": "f574fbb8-b291-4cc7-bf22-4e3f27977558",
  "accountName": "0242078689-00001",
  "firmwareFrom": "VerizonFirmwareVersion-02",
  "firmwareTo": "VerizonFirmwareVersion-03",
  "startDate": "2018-03-05",
  "upgradeStartTime": "2018-03-05T19:07:21Z",
  "status": "UpgradeSuccess",
  "reason": "success"
}
```

