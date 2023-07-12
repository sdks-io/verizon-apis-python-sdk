
# Firmware Campaign

Firmware upgrade information.

## Structure

`FirmwareCampaign`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Required | Upgrade identifier. |
| `account_name` | `string` | Required | Account identifier. |
| `campaign_name` | `string` | Optional | Campaign name. |
| `firmware_name` | `string` | Optional | Firmware name (for firmware upgrade only). |
| `firmware_from` | `string` | Required | Old firmware version (for firmware upgrade only). |
| `firmware_to` | `string` | Required | New firmware version (for firmware upgrade only). |
| `protocol` | `string` | Required | Available values: LWM2M.<br>**Default**: `'LWM2M'` |
| `make` | `string` | Required | - |
| `model` | `string` | Required | - |
| `start_date` | `date` | Required | Campaign start date. |
| `end_date` | `date` | Required | Campaign end date. |
| `campaign_time_window_list` | [`List of V3TimeWindow`](../../doc/models/v3-time-window.md) | Optional | List of allowed campaign time windows. |
| `status` | `string` | Required | Campaign status. |

## Example (as JSON)

```json
{
  "id": "f858b8c4-2153-11ec-8c44-aeb16d1aa652",
  "accountName": "0000123456-00001",
  "campaignName": "Smart FOTA - test 4",
  "firmwareName": "SEQUANSCommunications_GM01Q_SR1.2.0.0-10512_SR1.2.0.0-10657",
  "protocol": "LWM2M",
  "firmwareFrom": "SR1.2.0.0-10512",
  "firmwareTo": "SR1.2.0.0-10657",
  "make": "SEQUANS Communications",
  "model": "GM01Q",
  "status": "CampaignRequestPending",
  "startDate": "2021-09-29",
  "endDate": "2021-10-01",
  "campaignTimeWindowList": [
    {
      "startTime": 18,
      "endTime": 22
    }
  ]
}
```

