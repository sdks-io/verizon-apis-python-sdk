# Exclusions

Exclude devices from location services.

```python
exclusions_controller = client.exclusions
```

## Class Name

`ExclusionsController`

## Methods

* [Exclude Devices](../../doc/controllers/exclusions.md#exclude-devices)
* [Remove Devices From Exclusion List](../../doc/controllers/exclusions.md#remove-devices-from-exclusion-list)
* [List Excluded Devices](../../doc/controllers/exclusions.md#list-excluded-devices)


# Exclude Devices

This consents endpoint sets a new exclusion list.

```python
def exclude_devices(self,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ConsentRequest`](../../doc/models/consent-request.md) | Body, Required | Request to update account consent exclusion list. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceLocationSuccessResult`](../../doc/models/device-location-success-result.md).

## Example Usage

```python
body = ConsentRequest(
    account_name='1234567890-00001',
    all_device=False,
    mtype='replace',
    exclusion=[
        '980003420535573',
        '375535024300089',
        'A100003861E585'
    ]
)

result = exclusions_controller.exclude_devices(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |


# Remove Devices From Exclusion List

Removes devices from the exclusion list so that they can be located with Device Location Services requests.

```python
def remove_devices_from_exclusion_list(self,
                                      account_name,
                                      device_list)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Query, Required | The numeric name of the account. |
| `device_list` | `str` | Query, Required | A list of the device IDs to remove from the exclusion list. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceLocationSuccessResult`](../../doc/models/device-location-success-result.md).

## Example Usage

```python
account_name = '0000123456-00001'

device_list = 'IMEI'

result = exclusions_controller.remove_devices_from_exclusion_list(
    account_name,
    device_list
)
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
| 400 | Unexpected error. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |


# List Excluded Devices

This consents endpoint retrieves a list of excluded devices in an account.

```python
def list_excluded_devices(self,
                         account,
                         start_index)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier in "##########-#####". |
| `start_index` | `str` | Template, Required | Zero-based number of the first record to return. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DevicesConsentResult`](../../doc/models/devices-consent-result.md).

## Example Usage

```python
account = '0252012345-00001'

start_index = '0'

result = exclusions_controller.list_excluded_devices(
    account,
    start_index
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "2024009649-00001",
  "allDevice": false,
  "hasMoreData": false,
  "totalCount": 4,
  "updateTime": "2018-05-18 19:20:50.076 +0000 UTC",
  "exclusion": [
    "990003420535375",
    "420535399000375",
    "A100003861E585",
    "205353759900034"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |

