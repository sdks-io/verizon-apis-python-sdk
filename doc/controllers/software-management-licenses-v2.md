# Software Management Licenses V2

```python
software_management_licenses_v2_controller = client.software_management_licenses_v2
```

## Class Name

`SoftwareManagementLicensesV2Controller`

## Methods

* [Get Account License Status](../../doc/controllers/software-management-licenses-v2.md#get-account-license-status)
* [Assign Licenses to Devices](../../doc/controllers/software-management-licenses-v2.md#assign-licenses-to-devices)
* [Remove Licenses From Devices](../../doc/controllers/software-management-licenses-v2.md#remove-licenses-from-devices)
* [List Licenses to Remove](../../doc/controllers/software-management-licenses-v2.md#list-licenses-to-remove)
* [Create List of Licenses to Remove](../../doc/controllers/software-management-licenses-v2.md#create-list-of-licenses-to-remove)
* [Delete List of Licenses to Remove](../../doc/controllers/software-management-licenses-v2.md#delete-list-of-licenses-to-remove)


# Get Account License Status

The endpoint allows user to list license usage.

```python
def get_account_license_status(self,
                              account,
                              last_seen_device_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |
| `last_seen_device_id` | `str` | Query, Optional | Last seen device identifier. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`V2LicenseSummary`](../../doc/models/v2-license-summary.md).

## Example Usage

```python
account = '0000123456-00001'

last_seen_device_id = '15-digit IMEI'

result = software_management_licenses_v2_controller.get_account_license_status(
    account,
    last_seen_device_id=last_seen_device_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0402196254-00001",
  "totalLicense": 5000,
  "assignedLicenses": 4319,
  "hasMoreData": true,
  "lastSeenDeviceId": "1000",
  "maxPageSize": 10,
  "deviceList": [
    {
      "deviceId": "990003425730535",
      "assignmentTime": "2017-11-29T16:03:42.000Z"
    },
    {
      "deviceId": "990000473475989",
      "assignmentTime": "2017-11-29T16:03:42.000Z"
    },
    {
      "deviceId": "990000347475989",
      "assignmentTime": "2017-11-29T16:03:42.000Z"
    },
    {
      "deviceId": "990007303425535",
      "assignmentTime": "2017-11-29T16:03:42.000Z"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# Assign Licenses to Devices

**This endpoint is deprecated.**

This endpoint allows user to assign licenses to a list of devices.

```python
def assign_licenses_to_devices(self,
                              account,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |
| `body` | [`V2LicenseIMEI`](../../doc/models/v2-license-imei.md) | Body, Required | License assignment. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`V2LicensesAssignedRemovedResult`](../../doc/models/v2-licenses-assigned-removed-result.md).

## Example Usage

```python
account = '0242078689-00001'

body = V2LicenseIMEI(
    device_list=[
        '990003425730524',
        '990000473475967'
    ]
)

result = software_management_licenses_v2_controller.assign_licenses_to_devices(
    account,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0242078689-00001",
  "licTotalCount": 1000,
  "licUsedCount": 502,
  "deviceList": [
    {
      "deviceId": "990003425730524",
      "status": "Success",
      "resultReason": "Success"
    },
    {
      "deviceId": "990000473475967",
      "status": "Failure",
      "resultReason": "Device does not exist."
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# Remove Licenses From Devices

**This endpoint is deprecated.**

This endpoint allows user to remove licenses from a list of devices.

```python
def remove_licenses_from_devices(self,
                                account,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |
| `body` | [`V2LicenseIMEI`](../../doc/models/v2-license-imei.md) | Body, Required | License removal. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`V2LicensesAssignedRemovedResult`](../../doc/models/v2-licenses-assigned-removed-result.md).

## Example Usage

```python
account = '0242078689-00001'

body = V2LicenseIMEI(
    device_list=[
        '990003425730535',
        '990000473475989',
        '900000000000999'
    ]
)

result = software_management_licenses_v2_controller.remove_licenses_from_devices(
    account,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0242078689-00001",
  "licTotalCount": 1000,
  "licUsedCount": 998,
  "deviceList": [
    {
      "deviceId": "990003425730535",
      "status": "Success",
      "resultReason": "Success"
    },
    {
      "deviceId": "990000473475989",
      "status": "Success",
      "resultReason": "Success"
    },
    {
      "deviceId": "900000000000999",
      "status": "Failure",
      "resultReason": "No license attached to device"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# List Licenses to Remove

**This endpoint is deprecated.**

The license cancel endpoint allows user to list registered license cancellation candidate devices.

```python
def list_licenses_to_remove(self,
                           account,
                           start_index=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |
| `start_index` | `str` | Query, Optional | Start index to retrieve. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`V2ListOfLicensesToRemove`](../../doc/models/v2-list-of-licenses-to-remove.md).

## Example Usage

```python
account = '0242078689-00001'

result = software_management_licenses_v2_controller.list_licenses_to_remove(account)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "count": 6,
  "hasMoreData": false,
  "updateTime": "2018-03-22 00:06:00.069 +0000 UTC",
  "deviceList": [
    "990003425730535",
    "990000473475989",
    "990005733420535",
    "990000347475989",
    "990007303425535",
    "990007590473489"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# Create List of Licenses to Remove

**This endpoint is deprecated.**

The license cancel endpoint allows user to create a list of license cancellation candidate devices.

```python
def create_list_of_licenses_to_remove(self,
                                     account,
                                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |
| `body` | [`V2ListOfLicensesToRemoveRequest`](../../doc/models/v2-list-of-licenses-to-remove-request.md) | Body, Required | List of licensess to remove. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`V2ListOfLicensesToRemoveResult`](../../doc/models/v2-list-of-licenses-to-remove-result.md).

## Example Usage

```python
account = '0242078689-00001'

body = V2ListOfLicensesToRemoveRequest(
    device_list=[
        '990003425730535',
        '990000473475989'
    ],
    mtype='append',
    count=2
)

result = software_management_licenses_v2_controller.create_list_of_licenses_to_remove(
    account,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "count": 2,
  "deviceList": [
    "990003425730535",
    "990000473475989"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# Delete List of Licenses to Remove

**This endpoint is deprecated.**

This endpoint allows user to delete a created cancel candidate device list.

```python
def delete_list_of_licenses_to_remove(self,
                                     account)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`FotaV2SuccessResult`](../../doc/models/fota-v2-success-result.md).

## Example Usage

```python
account = '0242078689-00001'

result = software_management_licenses_v2_controller.delete_list_of_licenses_to_remove(account)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "success": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |

