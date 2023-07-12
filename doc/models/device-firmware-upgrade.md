
# Device Firmware Upgrade

Firmware upgrades information.

## Structure

`DeviceFirmwareUpgrade`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `string` | Required | Device identifier. |
| `campaign_id` | `string` | Required | Campaign identifier. |
| `account_name` | `string` | Required | Account identifier. |
| `firmware_name` | `string` | Optional | Firmware name. |
| `firmware_from` | `string` | Optional | Old firmware version. |
| `firmware_to` | `string` | Optional | New firmware version. |
| `start_date` | `date` | Required | Firmware upgrade start date. |
| `status` | `string` | Required | Firmware upgrade status. |
| `reason` | `string` | Required | Software upgrade result reason. |
| `report_updated_time` | `string` | Optional | Report updated time. |

## Example (as JSON)

```json
{
  "deviceId": "15-digit IMEI",
  "campaignId": "252d7ffc-7e35-11ec-931d-76f56843c393",
  "accountName": "0000123456-00001",
  "firmwareName": "SEQUANSCommunications_GM01Q_SR1.2.0.0-10657_SR1.2.0.0-10512",
  "firmwareFrom": "SR1.2.0.0-10657",
  "firmwareTo": "SR1.2.0.0-10512",
  "startDate": "2022-01-25",
  "reportUpdatedTime": "2022-01-26 03:45:01.608 +0000 UTC",
  "status": "UpgradeSuccess",
  "reason": "Upgrade completed successfully"
}
```

