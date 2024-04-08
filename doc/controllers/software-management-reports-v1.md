# Software Management Reports V1

```python
software_management_reports_v1_controller = client.software_management_reports_v1
```

## Class Name

`SoftwareManagementReportsV1Controller`

## Methods

* [List Account Devices](../../doc/controllers/software-management-reports-v1.md#list-account-devices)
* [List Upgrades for Specified Status](../../doc/controllers/software-management-reports-v1.md#list-upgrades-for-specified-status)
* [Get Device Firmware Upgrade History](../../doc/controllers/software-management-reports-v1.md#get-device-firmware-upgrade-history)


# List Account Devices

Returns an array of all devices in the specified account. Each device object includes information needed for managing firmware, including the device make and model, MDN and IMEI, and current firmware version.

```python
def list_account_devices(self,
                        account,
                        start_index)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier in "##########-#####". |
| `start_index` | `str` | Template, Required | Only return devices with IMEIs larger than this value. Use 0 for the first request. If `hasMoreData`=true in the response, use the `lastSeenDeviceId` value from the response as the startIndex in the next request. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceListQueryResult`](../../doc/models/device-list-query-result.md).

## Example Usage

```python
account = '0242078689-00001'

start_index = 'startIndex4'

result = software_management_reports_v1_controller.list_account_devices(
    account,
    start_index
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0242078698-00001",
  "hasMoreData": true,
  "lastSeenDeviceId": 900000000001000,
  "deviceList": [
    {
      "deviceId": "900000000000001",
      "mdn": "0000040881",
      "model": "Model-A",
      "make": "Verizon",
      "firmware": "VerizonFirmwareVersion-01",
      "fotaEligible": true,
      "licenseAssigned": true,
      "upgradeTime": "2021-06-03 00:03:56.079 +0000 UTC"
    },
    {
      "deviceId": "900000000000999",
      "mdn": "0000041879",
      "model": "Model-A",
      "make": "Verizon",
      "firmware": "VerizonFirmwareVersion-01",
      "fotaEligible": true,
      "licenseAssigned": true,
      "upgradeTime": "2021-06-03 00:03:56.079 +0000 UTC"
    },
    {
      "deviceId": "900000000001000",
      "mdn": "0000041880",
      "model": "Model-A",
      "make": "Verizon",
      "firmware": "VerizonFirmwareVersion-01",
      "fotaEligible": true,
      "licenseAssigned": true,
      "upgradeTime": "2021-06-03 00:03:56.079 +0000 UTC"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV1ResultException`](../../doc/models/fota-v1-result-exception.md) |


# List Upgrades for Specified Status

Returns a list of all upgrades with a specified status.

```python
def list_upgrades_for_specified_status(self,
                                      account,
                                      upgrade_status,
                                      start_index)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier in "##########-#####". |
| `upgrade_status` | [`UpgradeStatusEnum`](../../doc/models/upgrade-status-enum.md) | Template, Required | The status of the upgrades that you want to retrieve. |
| `start_index` | `str` | Template, Required | The zero-based number of the first record to return. Set startIndex=0 for the first request. If `hasMoreFlag`=true in the response, use the `lastSeenUpgradeId` value from the response as the startIndex in the next request. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`UpgradeListQueryResult`](../../doc/models/upgrade-list-query-result.md).

## Example Usage

```python
account = '0242078689-00001'

upgrade_status = UpgradeStatusEnum.REQUESTPENDING

start_index = 'startIndex4'

result = software_management_reports_v1_controller.list_upgrades_for_specified_status(
    account,
    upgrade_status,
    start_index
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV1ResultException`](../../doc/models/fota-v1-result-exception.md) |


# Get Device Firmware Upgrade History

Returns the upgrade history of the specified device from the previous six months.

```python
def get_device_firmware_upgrade_history(self,
                                       account,
                                       device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier in "##########-#####". |
| `device_id` | `str` | Template, Required | The IMEI of the device. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[DeviceUpgradeHistory]`](../../doc/models/device-upgrade-history.md).

## Example Usage

```python
account = '0242078689-00001'

device_id = '900000000000001'

result = software_management_reports_v1_controller.get_device_firmware_upgrade_history(
    account,
    device_id
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "deviceId": "900000000000001",
    "id": "f574fbb8-b291-4cc7-bf22-4e3f27977558",
    "accountName": "0242078689-00001",
    "firmwareFrom": "VerizonFirmwareVersion-02",
    "firmwareTo": "VerizonFirmwareVersion-03",
    "startDate": "2018-03-05",
    "upgradeStartTime": "2018-03-05T19:07:21Z",
    "status": "UpgradeSuccess",
    "reason": "success"
  },
  {
    "deviceId": "900000000000001",
    "id": "5edade25-c06c-4b13-ba2a-fbb9ada93579",
    "accountName": "0242078689-00001",
    "firmwareFrom": "VerizonFirmwareVersion-01",
    "firmwareTo": "VerizonFirmwareVersion-02",
    "startDate": "2018-02-20",
    "upgradeStartTime": "2018-02-20T00:03:19Z",
    "status": "UpgradeSuccess",
    "reason": "success"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV1ResultException`](../../doc/models/fota-v1-result-exception.md) |

