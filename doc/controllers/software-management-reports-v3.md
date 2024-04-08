# Software Management Reports V3

```python
software_management_reports_v3_controller = client.software_management_reports_v3
```

## Class Name

`SoftwareManagementReportsV3Controller`

## Methods

* [Get Campaign History by Status](../../doc/controllers/software-management-reports-v3.md#get-campaign-history-by-status)
* [Get Device Firmware Upgrade History](../../doc/controllers/software-management-reports-v3.md#get-device-firmware-upgrade-history)
* [Get Campaign Device Status](../../doc/controllers/software-management-reports-v3.md#get-campaign-device-status)


# Get Campaign History by Status

Retrieve a list of campaigns for an account that have a specified campaign status.

```python
def get_campaign_history_by_status(self,
                                  acc,
                                  campaign_status,
                                  last_seen_campaign_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `str` | Template, Required | Account identifier. |
| `campaign_status` | [`CampaignStatusEnum`](../../doc/models/campaign-status-enum.md) | Query, Required | Campaign status. |
| `last_seen_campaign_id` | `str` | Query, Optional | Last seen campaign Id. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`V3CampaignHistory`](../../doc/models/v3-campaign-history.md).

## Example Usage

```python
acc = '0000123456-00001'

campaign_status = CampaignStatusEnum.CAMPAIGNREQUESTPENDING

last_seen_campaign_id = '60b5d639-ccdc-4db8-8824-069bd94c95bf'

result = software_management_reports_v3_controller.get_campaign_history_by_status(
    acc,
    campaign_status,
    last_seen_campaign_id=last_seen_campaign_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "hasMoreData": true,
  "lastSeenCampaignId": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
  "campaignList": [
    {
      "accountName": "0000123456-00001",
      "id": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
      "campaignName": "FOTA_Verizon_Upgrade",
      "firmwareName": "FOTA_Verizon_Model-A_02To03_HF",
      "firmwareFrom": "FOTA_Verizon_Model-A_00To01_HF",
      "firmwareTo": "FOTA_Verizon_Model-A_02To03_HF",
      "make": "Verizon",
      "model": "Model-A",
      "status": "CampaignEnded",
      "startDate": "2020-08-21",
      "endDate": "2020-08-22",
      "campaignTimeWindowList": [
        {
          "startTime": 20,
          "endTime": 21
        }
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV3ResultException`](../../doc/models/fota-v3-result-exception.md) |


# Get Device Firmware Upgrade History

Retrieve campaign history for a specific device.

```python
def get_device_firmware_upgrade_history(self,
                                       acc,
                                       device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `str` | Template, Required | Account identifier. |
| `device_id` | `str` | Template, Required | Device IMEI identifier. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[DeviceFirmwareUpgrade]`](../../doc/models/device-firmware-upgrade.md).

## Example Usage

```python
acc = '0000123456-00001'

device_id = '15-digit IMEI'

result = software_management_reports_v3_controller.get_device_firmware_upgrade_history(
    acc,
    device_id
)
print(result)
```

## Example Response *(as JSON)*

```json
[
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
  },
  {
    "deviceId": "15-digit IMEI",
    "campaignId": "8f5e9a4a-6ce2-11ec-ace7-3ea293843397",
    "accountName": "0000123456-00001",
    "firmwareName": "SEQUANSCommunications_GM01Q_SR1.2.0.0-10512_SR1.2.0.0-10657",
    "firmwareFrom": "SR1.2.0.0-10512",
    "firmwareTo": "SR1.2.0.0-10657",
    "startDate": "2022-01-03",
    "reportUpdatedTime": "2022-01-04 02:45:00.67 +0000 UTC",
    "status": "UpgradeSuccess",
    "reason": "Upgrade completed successfully"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV3ResultException`](../../doc/models/fota-v3-result-exception.md) |


# Get Campaign Device Status

Retrieve a list of all devices in a campaign and the status of each device.

```python
def get_campaign_device_status(self,
                              acc,
                              campaign_id,
                              last_seen_device_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `str` | Template, Required | Account identifier. |
| `campaign_id` | `str` | Template, Required | Campaign identifier. |
| `last_seen_device_id` | `str` | Query, Optional | Last seen device identifier. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`V3CampaignDevice`](../../doc/models/v3-campaign-device.md).

## Example Usage

```python
acc = '0000123456-00001'

campaign_id = 'f858b8c4-2153-11ec-8c44-aeb16d1aa652'

last_seen_device_id = '15-digit IMEI'

result = software_management_reports_v3_controller.get_campaign_device_status(
    acc,
    campaign_id,
    last_seen_device_id=last_seen_device_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "totalDevice": 2689,
  "hasMoreData": true,
  "lastSeenDeviceId": "15-digit IMEI",
  "maxPageSize": 1000,
  "deviceList": [
    {
      "deviceId": "15-digit IMEI",
      "status": "UpgradePending",
      "resultReason": "Upgrade pending, the device upgrade is estimated to be scheduled for 06 Oct 22 18:05 UTC",
      "updatedTime": "2022-08-05T21:05:27.129Z",
      "recentAttemptTime": "2022-10-05T21:05:01.19Z",
      "nextAttemptTime": "2022-10-06T18:35:00Z"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV3ResultException`](../../doc/models/fota-v3-result-exception.md) |

