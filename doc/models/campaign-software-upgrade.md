
# Campaign Software Upgrade

Software upgrade information.

## Structure

`CampaignSoftwareUpgrade`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `campaign_name` | `string` | Optional | Campaign name. |
| `software_name` | `string` | Required | Software name to upgrade to. |
| `software_from` | `string` | Required | Old software name. |
| `software_to` | `string` | Required | New software name. |
| `distribution_type` | `string` | Required | OMA or HTTP. |
| `start_date` | `date` | Required | Campaign start date. |
| `end_date` | `date` | Required | Campaign end date. |
| `download_after_date` | `date` | Optional | Specifies starting date client should download package. If null, client will download as soon as possible. |
| `download_time_window_list` | [`List of V2TimeWindow`](../../doc/models/v2-time-window.md) | Optional | List of allowed download time windows. |
| `install_after_date` | `date` | Optional | Client will install package after date. If null, client will install as soon as possible. |
| `install_time_window_list` | [`List of V2TimeWindow`](../../doc/models/v2-time-window.md) | Optional | List of allowed install time windows. |
| `device_list` | `List of string` | Required | Device IMEI list. |

## Example (as JSON)

```json
{
  "campaignName": "FOTA_Verizon_Upgrade",
  "softwareName": "FOTA_Verizon_Model-A_02To03_HF",
  "softwareFrom": "FOTA_Verizon_Model-A_00To01_HF",
  "softwareTo": "FOTA_Verizon_Model-A_02To03_HF",
  "distributionType": "HTTP",
  "startDate": "2020-08-21",
  "endDate": "2020-08-22",
  "downloadAfterDate": "2020-08-21",
  "downloadTimeWindowList": [
    {
      "startTime": 20,
      "endTime": 21
    }
  ],
  "installAfterDate": "2020-08-21",
  "installTimeWindowList": [
    {
      "startTime": 22,
      "endTime": 23
    }
  ],
  "deviceList": [
    "990013907835573",
    "990013907884259"
  ]
}
```

