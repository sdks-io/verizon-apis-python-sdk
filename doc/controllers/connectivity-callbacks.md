# Connectivity Callbacks

```python
connectivity_callbacks_controller = client.connectivity_callbacks
```

## Class Name

`ConnectivityCallbacksController`

## Methods

* [List Registered Callbacks](../../doc/controllers/connectivity-callbacks.md#list-registered-callbacks)
* [Register Callback](../../doc/controllers/connectivity-callbacks.md#register-callback)
* [Deregister Callback](../../doc/controllers/connectivity-callbacks.md#deregister-callback)


# List Registered Callbacks

Returns the name and endpoint URL of the callback listening services registered for a given account.

```python
def list_registered_callbacks(self,
                             aname)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `str` | Template, Required | Account name. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[ConnectivityManagementCallback]`](../../doc/models/connectivity-management-callback.md).

## Example Usage

```python
aname = '0252012345-00001'

result = connectivity_callbacks_controller.list_registered_callbacks(aname)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "accountName": "0252012345-00001",
    "serviceName": "CarrierService",
    "url": "http://10.120.102.147:50569/CallbackListener/Carrier.asmx"
  },
  {
    "accountName": "0252012345-00001",
    "password": "drowssap",
    "serviceName": "DeviceUsage",
    "url": "http://10.120.102.147:50569/CallbackListener/Usage.asmx",
    "username": "zaffod"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# Register Callback

You are responsible for creating and running a listening process on your server at that URL.

```python
def register_callback(self,
                     aname,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `str` | Template, Required | Account name. |
| `body` | [`RegisterCallbackRequest`](../../doc/models/register-callback-request.md) | Body, Required | Request to register a callback. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`CallbackActionResult`](../../doc/models/callback-action-result.md).

## Example Usage

```python
aname = 'TestAccount-2'

body = RegisterCallbackRequest(
    name='CarrierService',
    url='https://mock.thingspace.verizon.com/webhook'
)

result = connectivity_callbacks_controller.register_callback(
    aname,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "122333444-00002",
  "serviceName": "CarrierService"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# Deregister Callback

Stops ThingSpace from sending callback messages for the specified account and service.

```python
def deregister_callback(self,
                       aname,
                       sname)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `str` | Template, Required | Account name. |
| `sname` | `str` | Template, Required | Service name. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`CallbackActionResult`](../../doc/models/callback-action-result.md).

## Example Usage

```python
aname = '1223334444-00001'

sname = 'CarrierService'

result = connectivity_callbacks_controller.deregister_callback(
    aname,
    sname
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "1223334444-00001",
  "serviceName": "CarrierService"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |

