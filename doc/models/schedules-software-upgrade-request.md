
# Schedules Software Upgrade Request

## Structure

`SchedulesSoftwareUpgradeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `campaign_name` | `string` | Optional | The campaign name. |
| `software_name` | `string` | Optional | Software name. |
| `software_from` | `string` | Optional | Old software name. |
| `software_to` | `string` | Optional | New software name. |
| `distribution_type` | `string` | Optional | Valid values |
| `start_date` | `string` | Optional | Campaign start date. |
| `end_date` | `string` | Optional | Campaign end date. |
| `download_after_date` | `string` | Optional | Specifies the starting date the client should download the package. If null, client downloads as soon as possible. |
| `download_time_window_list` | [`List of DownloadTimeWindow`](../../doc/models/download-time-window.md) | Optional | List of allowed download time windows. |
| `install_after_date` | `string` | Optional | The date after which you install the package. If null, install as soon as possible. |
| `install_time_window_list` | [`List of DownloadTimeWindow`](../../doc/models/download-time-window.md) | Optional | List of allowed install time windows. |
| `device_list` | `List of string` | Optional | Device IMEI list. |

## Example (as JSON)

```json
{
  "campaignName": "FOTA_Verizon_Upgrade",
  "softwareName": "FOTA_Verizon_Model-A_02To03_HF",
  "softwareFrom": "FOTA_Verizon_Model-A_00To01_HF",
  "softwareTo": "FOTA_Verizon_Model-A_02To03_HF",
  "distributionType": "HTTP",
  "startDate": "2021-02-08",
  "endDate": "2021-02-08",
  "downloadAfterDate": "2021-02-08"
}
```

