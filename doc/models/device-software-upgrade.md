
# Device Software Upgrade

Array of software upgrade objects with the specified status.

## Structure

`DeviceSoftwareUpgrade`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Required | Device identifier. |
| `id` | `str` | Required | Upgrade identifier. |
| `account_name` | `str` | Required | Account identifier. |
| `software_name` | `str` | Optional | Software name. |
| `start_date` | `date` | Required | Software upgrade start date. |
| `status` | `str` | Required | Software upgrade status. |
| `reason` | `str` | Required | Software upgrade result reason. |

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

