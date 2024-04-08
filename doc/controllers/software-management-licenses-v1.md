# Software Management Licenses V1

```python
software_management_licenses_v1_controller = client.software_management_licenses_v1
```

## Class Name

`SoftwareManagementLicensesV1Controller`

## Methods

* [Assign Licenses to Devices](../../doc/controllers/software-management-licenses-v1.md#assign-licenses-to-devices)
* [Remove Licenses From Devices](../../doc/controllers/software-management-licenses-v1.md#remove-licenses-from-devices)
* [Create List of Licenses to Remove](../../doc/controllers/software-management-licenses-v1.md#create-list-of-licenses-to-remove)
* [Delete List of Licenses to Remove](../../doc/controllers/software-management-licenses-v1.md#delete-list-of-licenses-to-remove)
* [List Licenses to Remove](../../doc/controllers/software-management-licenses-v1.md#list-licenses-to-remove)


# Assign Licenses to Devices

**This endpoint is deprecated.**

Assigns licenses to a specified list of devices so that firmware upgrades can be scheduled for those devices.

```python
def assign_licenses_to_devices(self,
                              account,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier in "##########-#####". |
| `body` | [`V1LicensesAssignedRemovedRequest`](../../doc/models/v1-licenses-assigned-removed-request.md) | Body, Required | IMEIs of the devices to assign licenses to. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`V1LicensesAssignedRemovedResult`](../../doc/models/v1-licenses-assigned-removed-result.md).

## Example Usage

```python
account = '0242078689-00001'

body = V1LicensesAssignedRemovedRequest(
    device_list=[
        '990003425730535',
        '990000473475989'
    ]
)

result = software_management_licenses_v1_controller.assign_licenses_to_devices(
    account,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0242078689-00001",
  "licCount": 9000,
  "licUsedCount": 1000,
  "deviceList": [
    {
      "deviceId": "900000000000001",
      "status": "LicenseAssignSuccess",
      "Reason": "Success"
    },
    {
      "deviceId": "900000000000999",
      "status": "LicenseAssignSuccess",
      "Reason": "Success"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV1ResultException`](../../doc/models/fota-v1-result-exception.md) |


# Remove Licenses From Devices

**This endpoint is deprecated.**

Remove unused licenses from device.

```python
def remove_licenses_from_devices(self,
                                account,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier in "##########-#####". |
| `body` | [`V1LicensesAssignedRemovedRequest`](../../doc/models/v1-licenses-assigned-removed-request.md) | Body, Required | IMEIs of the devices to remove licenses from. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`V1LicensesAssignedRemovedResult`](../../doc/models/v1-licenses-assigned-removed-result.md).

## Example Usage

```python
account = '0242078689-00001'

body = V1LicensesAssignedRemovedRequest(
    device_list=[
        '900000000000001',
        '900000000000998',
        '900000000000999'
    ]
)

result = software_management_licenses_v1_controller.remove_licenses_from_devices(
    account,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0242078689-00001",
  "licCount": 9000,
  "licUsedCount": 998,
  "deviceList": [
    {
      "deviceId": "900000000000001",
      "status": "LicenseRemoveSuccess",
      "Reason": "Success"
    },
    {
      "deviceId": "900000000000998",
      "status": "LicenseRemoveSuccess",
      "Reason": "Success"
    },
    {
      "deviceId": "900000000000999",
      "status": "LicenseRemoveFailed",
      "Reason": "No license attached to device"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV1ResultException`](../../doc/models/fota-v1-result-exception.md) |


# Create List of Licenses to Remove

**This endpoint is deprecated.**

Creates a list of devices from which licenses will be removed if the number of MRC licenses becomes less than the number of assigned licenses.

```python
def create_list_of_licenses_to_remove(self,
                                     account,
                                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier in "##########-#####". |
| `body` | [`V1ListOfLicensesToRemoveRequest`](../../doc/models/v1-list-of-licenses-to-remove-request.md) | Body, Required | Cancellation candidate device list. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`V1ListOfLicensesToRemoveResult`](../../doc/models/v1-list-of-licenses-to-remove-result.md).

## Example Usage

```python
account = '0242078689-00001'

body = V1ListOfLicensesToRemoveRequest(
    device_list=[
        '990003425730535',
        '990000473475989'
    ],
    mtype='append'
)

result = software_management_licenses_v1_controller.create_list_of_licenses_to_remove(
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
    "900000000000001",
    "900000000000999"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV1ResultException`](../../doc/models/fota-v1-result-exception.md) |


# Delete List of Licenses to Remove

**This endpoint is deprecated.**

Deletes the entire list of cancellation candidate devices.

```python
def delete_list_of_licenses_to_remove(self,
                                     account)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier in "##########-#####". |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`FotaV1SuccessResult`](../../doc/models/fota-v1-success-result.md).

## Example Usage

```python
account = '0242078689-00001'

result = software_management_licenses_v1_controller.delete_list_of_licenses_to_remove(account)
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
| 400 | Unexpected error. | [`FotaV1ResultException`](../../doc/models/fota-v1-result-exception.md) |


# List Licenses to Remove

**This endpoint is deprecated.**

Returns a list of devices from which licenses will be removed if the number of MRC licenses becomes less than the number of assigned licenses.

```python
def list_licenses_to_remove(self,
                           account,
                           start_index)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier in "##########-#####". |
| `start_index` | `str` | Template, Required | The zero-based number of the first record to return. Set startIndex=0 for the first request. If there are more than 1,000 devices in the response, set startIndex=1000 for the second request, 2000 for the third request, etc. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`V1ListOfLicensesToRemove`](../../doc/models/v1-list-of-licenses-to-remove.md).

## Example Usage

```python
account = '0242078689-00001'

start_index = 'startIndex4'

result = software_management_licenses_v1_controller.list_licenses_to_remove(
    account,
    start_index
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "count": 6,
  "hasMoreData": false,
  "updateTime": "2018-03-22T12:06:06.000Z",
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
| 400 | Unexpected error. | [`FotaV1ResultException`](../../doc/models/fota-v1-result-exception.md) |

