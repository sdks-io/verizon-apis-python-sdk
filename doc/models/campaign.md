
# Campaign

Firmware upgrade information.

## Structure

`Campaign`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Upgrade identifier. |
| `account_name` | `str` | Required | Account identifier. |
| `campaign_name` | `str` | Optional | Campaign name. |
| `firmware_name` | `str` | Optional | Name of firmware. |
| `firmware_from` | `str` | Optional | Old firmware version. |
| `firmware_to` | `str` | Optional | New firmware version. |
| `protocol` | `str` | Required | The protocol of the firmware distribution. Default: LWM2M.<br>**Default**: `'LWM2M'` |
| `make` | `str` | Required | Applicable make. |
| `model` | `str` | Required | Applicable model. |
| `start_date` | `date` | Required | Campaign start date. |
| `end_date` | `date` | Required | Campaign end date. |
| `campaign_time_window_list` | [`List[V3TimeWindow]`](../../doc/models/v3-time-window.md) | Optional | List of allowed campaign time windows. |
| `status` | `str` | Required | Firmware upgrade status. |

## Example (as JSON)

```json
{
  "id": "f858b8c4-2153-11ec-8c44-aeb16d1aa652",
  "accountName": "0642233522-00001",
  "campaignName": "Smart FOTA - test 4",
  "protocol": "LWM2M",
  "make": "SEQUANS Communications",
  "model": "GM01Q",
  "status": "CampaignPreScheduled",
  "startDate": "2021-09-29",
  "endDate": "2021-10-01",
  "firmwareName": "SEQUANSCommunications_GM01Q_SR1.2.0.0-10512_SR1.2.0.0-10657",
  "firmwareFrom": "SR1.2.0.0-10512",
  "firmwareTo": "SR1.2.0.0-10657",
  "campaignTimeWindowList": [
    {
      "startTime": 18,
      "endTime": 22
    }
  ]
}
```

