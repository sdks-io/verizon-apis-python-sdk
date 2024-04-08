# Software Management Callbacks V1

```python
software_management_callbacks_v1_controller = client.software_management_callbacks_v1
```

## Class Name

`SoftwareManagementCallbacksV1Controller`

## Methods

* [List Registered Callbacks](../../doc/controllers/software-management-callbacks-v1.md#list-registered-callbacks)
* [Register Callback](../../doc/controllers/software-management-callbacks-v1.md#register-callback)
* [Deregister Callback](../../doc/controllers/software-management-callbacks-v1.md#deregister-callback)


# List Registered Callbacks

Returns the name and endpoint URL of the callback listening services registered for a given account.

```python
def list_registered_callbacks(self,
                             account)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier in "##########-#####". |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[RegisteredCallbacks]`](../../doc/models/registered-callbacks.md).

## Example Usage

```python
account = '0242078689-00001'

result = software_management_callbacks_v1_controller.list_registered_callbacks(account)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "aname": "0252012345-00001",
    "name": "Fota",
    "url": "http://10.120.102.183:50559/CallbackListener/FirmwareServiceMessages.asmx"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV1ResultException`](../../doc/models/fota-v1-result-exception.md) |


# Register Callback

Registers a URL to receive RESTful messages from a callback service when new firmware versions are available and when upgrades start and finish.

```python
def register_callback(self,
                     account,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier in "##########-#####". |
| `body` | [`FotaV1CallbackRegistrationRequest`](../../doc/models/fota-v1-callback-registration-request.md) | Body, Required | Callback details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`FotaV1CallbackRegistrationResult`](../../doc/models/fota-v1-callback-registration-result.md).

## Example Usage

```python
account = '0242078689-00001'

body = FotaV1CallbackRegistrationRequest(
    name='Fota',
    url='https://10.120.102.183:50559/CallbackListener/FirmwareServiceMessages.asmx'
)

result = software_management_callbacks_v1_controller.register_callback(
    account,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0204563412-00001",
  "serviceName": "Fota"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV1ResultException`](../../doc/models/fota-v1-result-exception.md) |


# Deregister Callback

Deregisters the callback endpoint and stops ThingSpace from sending FOTA callback messages for the specified account.

```python
def deregister_callback(self,
                       account,
                       service)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier in "##########-#####". |
| `service` | [`CallbackServiceEnum`](../../doc/models/callback-service-enum.md) | Template, Required | Callback type. Must be 'Fota' for Software Management Services API. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`FotaV1SuccessResult`](../../doc/models/fota-v1-success-result.md).

## Example Usage

```python
account = '0242078689-00001'

service = CallbackServiceEnum.FOTA

result = software_management_callbacks_v1_controller.deregister_callback(
    account,
    service
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
| 400 | Unexpected error. | [`FotaV1ResultException`](../../doc/models/fota-v1-result-exception.md) |

