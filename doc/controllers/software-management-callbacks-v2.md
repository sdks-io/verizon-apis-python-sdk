# Software Management Callbacks V2

```python
software_management_callbacks_v2_controller = client.software_management_callbacks_v2
```

## Class Name

`SoftwareManagementCallbacksV2Controller`

## Methods

* [List Registered Callbacks](../../doc/controllers/software-management-callbacks-v2.md#list-registered-callbacks)
* [Update Callback](../../doc/controllers/software-management-callbacks-v2.md#update-callback)
* [Register Callback](../../doc/controllers/software-management-callbacks-v2.md#register-callback)
* [Deregister Callback](../../doc/controllers/software-management-callbacks-v2.md#deregister-callback)


# List Registered Callbacks

This endpoint allows user to get the registered callback information.

```python
def list_registered_callbacks(self,
                             account)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`CallbackSummary`](../../doc/models/callback-summary.md).

## Example Usage

```python
account = '0000123456-00001'

result = software_management_callbacks_v2_controller.list_registered_callbacks(account)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "url": "http://10.120.102.183:50559/CallbackListener/FirmwareServiceMessages.asmx"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# Update Callback

This endpoint allows user to update the HTTPS callback address.

```python
def update_callback(self,
                   account,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |
| `body` | [`FotaV2CallbackRegistrationRequest`](../../doc/models/fota-v2-callback-registration-request.md) | Body, Required | Callback URL registration. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`FotaV2CallbackRegistrationResult`](../../doc/models/fota-v2-callback-registration-result.md).

## Example Usage

```python
account = '0000123456-00001'

body = FotaV2CallbackRegistrationRequest(
    url='https://255.255.11.135:50559/CallbackListener/FirmwareServiceMessages.asmx'
)

result = software_management_callbacks_v2_controller.update_callback(
    account,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "url": "https://255.255.11.135:50559/CallbackListener/FirmwareServiceMessages.asmx"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# Register Callback

This endpoint allows user to create the HTTPS callback address.

```python
def register_callback(self,
                     account,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |
| `body` | [`FotaV2CallbackRegistrationRequest`](../../doc/models/fota-v2-callback-registration-request.md) | Body, Required | Callback URL registration. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`FotaV2CallbackRegistrationResult`](../../doc/models/fota-v2-callback-registration-result.md).

## Example Usage

```python
account = '0000123456-00001'

body = FotaV2CallbackRegistrationRequest(
    url='https://10.120.102.183:50559/CallbackListener/FirmwareServiceMessages.asmx'
)

result = software_management_callbacks_v2_controller.register_callback(
    account,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "url": "https://10.120.102.183:50559/CallbackListener/FirmwareServiceMessages.asmx"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# Deregister Callback

This endpoint allows user to delete a previously registered callback URL.

```python
def deregister_callback(self,
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
account = '0000123456-00001'

result = software_management_callbacks_v2_controller.deregister_callback(account)
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

