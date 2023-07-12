
# Upload and Schedule File Response

## Structure

`UploadAndScheduleFileResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | Updgrade identifier. |
| `account_name` | `string` | Optional | Account identifer. |
| `campaign_name` | `string` | Optional | The campaign name. |
| `software_name` | `string` | Optional | Software name. |
| `software_from` | `string` | Optional | Old software name. |
| `software_to` | `string` | Optional | New software name. |
| `file_name` | `string` | Optional | The name of the file you are upgrading to. |
| `file_version` | `string` | Optional | The version of the file you are upgrading to. |
| `distribution_type` | `string` | Optional | Valid values |
| `make` | `string` | Optional | Applicable make. |
| `model` | `string` | Optional | Applicable model. |
| `start_date` | `string` | Optional | Campaign start date. |
| `end_date` | `string` | Optional | Campaign end date. |
| `download_after_date` | `string` | Optional | Specifies the starting date the client should download the package. If null, client downloads as soon as possible. |
| `download_time_window_list` | [`List of DownloadTimeWindow`](../../doc/models/download-time-window.md) | Optional | List of allowed download time windows. |
| `install_after_date` | `string` | Optional | The date after which you install the package. If null, install as soon as possible. |
| `install_time_window_list` | [`List of DownloadTimeWindow`](../../doc/models/download-time-window.md) | Optional | List of allowed install time windows. |
| `device_list` | `List of string` | Optional | Device IMEI list. |
| `status` | `string` | Optional | Software update status. |

## Example (as JSON)

```json
{
  "id": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
  "accountName": "0242078689-00001",
  "campaignName": "FOTA_Verizon_Upgrade",
  "softwareName": "FOTA_Verizon_Model-A_02To03_HF",
  "softwareFrom": "FOTA_Verizon_Model-A_00To01_HF",
  "softwareTo": "FOTA_Verizon_Model-A_02To03_HF",
  "fileName": "configfile-Verizon_VZW1_hello-world.txt",
  "fileVersion": "1.0",
  "distributionType": "HTTP",
  "make": "Verizon",
  "model": "Model-A",
  "startDate": "2021-02-08",
  "endDate": "2021-02-08",
  "downloadAfterDate": "2021-02-08",
  "status": "pending"
}
```

