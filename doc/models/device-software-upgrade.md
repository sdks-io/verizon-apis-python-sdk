
# Device Software Upgrade

Array of software upgrade objects with the specified status.

## Structure

`DeviceSoftwareUpgrade`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `string` | Required | Device identifier. |
| `id` | `string` | Required | Upgrade identifier. |
| `account_name` | `string` | Required | Account identifier. |
| `software_name` | `string` | Optional | Software name. |
| `start_date` | `date` | Required | Software upgrade start date. |
| `status` | `string` | Required | Software upgrade status. |
| `reason` | `string` | Required | Software upgrade result reason. |

## Example (as JSON)

```json
{
  "deviceId": "990013907835573",
  "id": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
  "accountName": "0402196254-00001",
  "softwareName": "FOTA_Verizon_Model-A_02To03_HF",
  "startDate": "2018-03-05",
  "status": "UpgradeSuccess",
  "reason": "success"
}
```

