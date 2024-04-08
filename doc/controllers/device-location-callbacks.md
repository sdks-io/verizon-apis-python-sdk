# Device Location Callbacks

```python
device_location_callbacks_controller = client.device_location_callbacks
```

## Class Name

`DeviceLocationCallbacksController`

## Methods

* [List Registered Callbacks](../../doc/controllers/device-location-callbacks.md#list-registered-callbacks)
* [Register Callback](../../doc/controllers/device-location-callbacks.md#register-callback)
* [Deregister Callback](../../doc/controllers/device-location-callbacks.md#deregister-callback)


# List Registered Callbacks

Returns a list of all registered callback URLs for the account.

```python
def list_registered_callbacks(self,
                             account)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account number. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[DeviceLocationCallback]`](../../doc/models/device-location-callback.md).

## Example Usage

```python
account = '0252012345-00001'

result = device_location_callbacks_controller.list_registered_callbacks(account)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "name": "Location",
    "url": "http://10.120.102.147:50569/CallbackListener/Location.asmx"
  },
  {
    "name": "Location",
    "url": "http://10.120.102.147:50569/CallbackListener/DeviceLocation.asmx"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |


# Register Callback

Provide a URL to receive messages from a ThingSpace callback service.

```python
def register_callback(self,
                     account,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account number. |
| `body` | [`DeviceLocationCallback`](../../doc/models/device-location-callback.md) | Body, Required | Request to register a callback. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`CallbackRegistrationResult`](../../doc/models/callback-registration-result.md).

## Example Usage

```python
account = '0252012345-00001'

body = DeviceLocationCallback(
    name=CallbackServiceNameEnum.LOCATION,
    url='http://10.120.102.183:50559/CallbackListener/LocationServiceMessages.asmx'
)

result = device_location_callbacks_controller.register_callback(
    account,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "account": "0212312345-00001",
  "name": "Location"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |


# Deregister Callback

Deregister a URL to stop receiving callback messages.

```python
def deregister_callback(self,
                       account,
                       service)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account number. |
| `service` | [`CallbackServiceNameEnum`](../../doc/models/callback-service-name-enum.md) | Template, Required | Callback service name. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceLocationSuccessResult`](../../doc/models/device-location-success-result.md).

## Example Usage

```python
account = '0252012345-00001'

service = CallbackServiceNameEnum.LOCATION

result = device_location_callbacks_controller.deregister_callback(
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
| 400 | Error response. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |

