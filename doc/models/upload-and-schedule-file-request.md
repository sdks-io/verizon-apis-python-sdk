
# Upload and Schedule File Request

## Structure

`UploadAndScheduleFileRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `campaign_name` | `str` | Optional | The campaign name. |
| `file_name` | `str` | Optional | The name of the file you are upgrading to. |
| `file_version` | `str` | Optional | The version of the file you are upgrading to. |
| `distribution_type` | `str` | Optional | Valid values |
| `start_date` | `str` | Optional | Campaign start date. |
| `end_date` | `str` | Optional | Campaign end date. |
| `download_after_date` | `str` | Optional | Specifies the starting date the client should download the package. If null, client downloads as soon as possible. |
| `download_time_window_list` | [`List[DownloadTimeWindow]`](../../doc/models/download-time-window.md) | Optional | List of allowed download time windows. |
| `install_after_date` | `str` | Optional | The date after which you install the package. If null, install as soon as possible. |
| `install_time_window_list` | [`List[DownloadTimeWindow]`](../../doc/models/download-time-window.md) | Optional | List of allowed install time windows. |
| `device_list` | `List[str]` | Optional | Device IMEI list. |

## Example (as JSON)

```json
{
  "campaignName": "FOTA_Verizon_Upgrade",
  "fileName": "configfile-Verizon_VZW1_hello-world.txt",
  "fileVersion": "1.0",
  "distributionType": "HTTP",
  "startDate": "2021-02-08",
  "endDate": "2021-02-08",
  "downloadAfterDate": "2021-02-08"
}
```

