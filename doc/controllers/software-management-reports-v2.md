# Software Management Reports V2

```python
software_management_reports_v2_controller = client.software_management_reports_v2
```

## Class Name

`SoftwareManagementReportsV2Controller`

## Methods

* [List Available Software](../../doc/controllers/software-management-reports-v2.md#list-available-software)
* [List Account Devices](../../doc/controllers/software-management-reports-v2.md#list-account-devices)
* [Get Device Firmware Upgrade History](../../doc/controllers/software-management-reports-v2.md#get-device-firmware-upgrade-history)
* [Get Campaign History by Status](../../doc/controllers/software-management-reports-v2.md#get-campaign-history-by-status)
* [Get Campaign Device Status](../../doc/controllers/software-management-reports-v2.md#get-campaign-device-status)


# List Available Software

This endpoint allows user to list a certain type of software of an account.

```python
def list_available_software(self,
                           account,
                           distribution_type=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |
| `distribution_type` | `str` | Query, Optional | Filter distributionType to get specific type of software. Value is LWM2M, OMD-DM or HTTP. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[SoftwarePackage]`](../../doc/models/software-package.md).

## Example Usage

```python
account = '0000123456-00001'

distribution_type = 'HTTP'

result = software_management_reports_v2_controller.list_available_software(
    account,
    distribution_type=distribution_type
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "softwareName": "FOTA_Verizon_Model-A_02To03_HF",
    "launchDate": "2020-08-31",
    "releaseNote": "",
    "model": "Model-A",
    "make": "Verizon",
    "distributionType": "HTTP",
    "devicePlatformId": "IoT"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# List Account Devices

The device endpoint gets devices information of an account.

```python
def list_account_devices(self,
                        account,
                        last_seen_device_id=None,
                        distribution_type=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |
| `last_seen_device_id` | `str` | Query, Optional | Last seen device identifier. |
| `distribution_type` | `str` | Query, Optional | Filter distributionType to get specific type of devices. Values is LWM2M, OMD-DM or HTTP. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`V2AccountDeviceList`](../../doc/models/v2-account-device-list.md).

## Example Usage

```python
account = '0000123456-00001'

last_seen_device_id = '15-digit IMEI'

distribution_type = 'HTTP'

result = software_management_reports_v2_controller.list_account_devices(
    account,
    last_seen_device_id=last_seen_device_id,
    distribution_type=distribution_type
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0000123456-00001",
  "hasMoreData": true,
  "lastSeenDeviceId": "15-digit IMEI",
  "maxPageSize": 1000,
  "deviceList": [
    {
      "deviceId": "15-digit IMEI",
      "mdn": "10-digit MDN",
      "model": "Model-A",
      "make": "Verizon",
      "fotaEligible": true,
      "appFotaEligible": true,
      "licenseAssigned": true,
      "distributionType": "HTTP",
      "softwareList": [
        {
          "name": "FOTA_Verizon_Model-A_02To03_HF",
          "version": "3",
          "upgradeTime": "2020-09-08T19:00:51.541Z"
        }
      ],
      "createTime": "2021-06-03 00:03:56.079 +0000 UTC",
      "upgradeTime": "2021-06-03 00:03:56.079 +0000 UTC",
      "updateTime": "2021-06-03 00:03:56.079 +0000 UTC",
      "refreshTime": "2021-06-03 00:03:56.079 +0000 UTC"
    },
    {
      "deviceId": "15-digit IMEI",
      "mdn": "10-digit MDN",
      "model": "Model-A",
      "make": "Verizon",
      "fotaEligible": true,
      "appFotaEligible": true,
      "licenseAssigned": true,
      "distributionType": "HTTP",
      "softwareList": [
        {
          "name": "FOTA_Verizon_Model-A_02To03_HF",
          "version": "3",
          "upgradeTime": "2020-09-08T19:00:51.541Z"
        }
      ],
      "createTime": "2021-06-03 00:03:56.079 +0000 UTC",
      "upgradeTime": "2021-06-03 00:03:56.079 +0000 UTC",
      "updateTime": "2021-06-03 00:03:56.079 +0000 UTC",
      "refreshTime": "2021-06-03 00:03:56.079 +0000 UTC"
    },
    {
      "deviceId": "15-digit IMEI",
      "mdn": "10-digit MDN",
      "model": "Model-A",
      "make": "Verizon",
      "fotaEligible": true,
      "appFotaEligible": true,
      "licenseAssigned": true,
      "distributionType": "HTTP",
      "softwareList": [
        {
          "name": "FOTA_Verizon_Model-A_02To03_HF",
          "version": "3",
          "upgradeTime": "2020-09-08T19:00:51.541Z"
        }
      ],
      "createTime": "2021-06-03 00:03:56.079 +0000 UTC",
      "upgradeTime": "2021-06-03 00:03:56.079 +0000 UTC",
      "updateTime": "2021-06-03 00:03:56.079 +0000 UTC",
      "refreshTime": "2021-06-03 00:03:56.079 +0000 UTC"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# Get Device Firmware Upgrade History

The endpoint allows user to get software upgrade history of a device based on device IMEI.

```python
def get_device_firmware_upgrade_history(self,
                                       account,
                                       device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |
| `device_id` | `str` | Template, Required | Device IMEI identifier. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[DeviceSoftwareUpgrade]`](../../doc/models/device-software-upgrade.md).

## Example Usage

```python
account = '0000123456-00001'

device_id = '990013907835573'

result = software_management_reports_v2_controller.get_device_firmware_upgrade_history(
    account,
    device_id
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "deviceId": "990013907835573",
    "id": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
    "accountName": "0402196254-00001",
    "softwareName": "FOTA_Verizon_Model-A_02To03_HF",
    "startDate": "2018-03-05",
    "status": "UpgradeSuccess",
    "reason": "success"
  },
  {
    "deviceId": "990013907835573",
    "id": "50d5d639-aaca-3ca7-7713-958ac83b84ae",
    "accountName": "0402196254-00001",
    "softwareName": "VerizonSoftwareVersion-01",
    "startDate": "2018-02-20",
    "status": "UpgradeSuccess",
    "reason": "success"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# Get Campaign History by Status

The report endpoint allows user to get campaign history of an account for specified status.

```python
def get_campaign_history_by_status(self,
                                  account,
                                  campaign_status,
                                  last_seen_campaign_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |
| `campaign_status` | `str` | Query, Required | Status of the campaign. |
| `last_seen_campaign_id` | `str` | Query, Optional | Last seen campaign Id. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`V2CampaignHistory`](../../doc/models/v2-campaign-history.md).

## Example Usage

```python
account = '0000123456-00001'

campaign_status = 'campaignStatus6'

last_seen_campaign_id = '60b5d639-ccdc-4db8-8824-069bd94c95bf'

result = software_management_reports_v2_controller.get_campaign_history_by_status(
    account,
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
      "accountName": "0402196254-00001",
      "id": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
      "campaignName": "FOTA_Verizon_Upgrade",
      "softwareName": "FOTA_Verizon_Model-A_02To03_HF",
      "distributionType": "HTTP",
      "softwareFrom": "FOTA_Verizon_Model-A_00To01_HF",
      "softwareTo": "FOTA_Verizon_Model-A_02To03_HF",
      "make": "Verizon",
      "model": "Model-A",
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
      "status": "CampaignEnded"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# Get Campaign Device Status

The report endpoint allows user to get the full list of device of a campaign.

```python
def get_campaign_device_status(self,
                              account,
                              campaign_id,
                              last_seen_device_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |
| `campaign_id` | `str` | Template, Required | Campaign identifier. |
| `last_seen_device_id` | `str` | Query, Optional | Last seen device identifier. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`V2CampaignDevice`](../../doc/models/v2-campaign-device.md).

## Example Usage

```python
account = '0000123456-00001'

campaign_id = '60b5d639-ccdc-4db8-8824-069bd94c95bf'

last_seen_device_id = '15-digit IMEI'

result = software_management_reports_v2_controller.get_campaign_device_status(
    account,
    campaign_id,
    last_seen_device_id=last_seen_device_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "totalDevice": 1148,
  "hasMoreData": true,
  "lastSeenDeviceId": "15-digit IMEI",
  "maxPageSize": 1000,
  "deviceList": [
    {
      "deviceId": "15-digit IMEI",
      "status": "UpgradeSuccess",
      "resultReason": "DownloadInstallSucceeded"
    },
    {
      "deviceId": "15-digit IMEI",
      "status": "UpgradeSuccess",
      "resultReason": "DownloadInstallSucceeded"
    },
    {
      "deviceId": "15-digit IMEI",
      "status": "UpgradeSuccess",
      "resultReason": "DownloadInstallSucceeded"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |

