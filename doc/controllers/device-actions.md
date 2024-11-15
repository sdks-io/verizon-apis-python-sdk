# Device Actions

```python
device_actions_controller = client.device_actions
```

## Class Name

`DeviceActionsController`

## Methods

* [Aggregate Usage](../../doc/controllers/device-actions.md#aggregate-usage)
* [Daily Usage](../../doc/controllers/device-actions.md#daily-usage)
* [Service Plan List](../../doc/controllers/device-actions.md#service-plan-list)
* [Account Information](../../doc/controllers/device-actions.md#account-information)
* [Retrieve the Global Device List](../../doc/controllers/device-actions.md#retrieve-the-global-device-list)
* [Retrieve Device Provisioning History](../../doc/controllers/device-actions.md#retrieve-device-provisioning-history)
* [Get Asynchronous Request Status](../../doc/controllers/device-actions.md#get-asynchronous-request-status)


# Aggregate Usage

Retrieve the aggregate usage for a device or a number of devices.

```python
def aggregate_usage(self,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AggregateUsage`](../../doc/models/aggregate-usage.md) | Body, Required | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`GIORequestResponse`](../../doc/models/gio-request-response.md).

## Example Usage

```python
body = AggregateUsage()

result = device_actions_controller.aggregate_usage(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |


# Daily Usage

Retrieve the daily usage for a device, for a specified period of time, segmented by day

```python
def daily_usage(self,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DailyUsage`](../../doc/models/daily-usage.md) | Body, Required | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DailyUsageResponse`](../../doc/models/daily-usage-response.md).

## Example Usage

```python
body = DailyUsage()

result = device_actions_controller.daily_usage(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |


# Service Plan List

Retrieve all of the service plans, features and carriers associated with the account specified.

```python
def service_plan_list(self,
                     account_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Template, Required | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`AccountDetails`](../../doc/models/account-details.md).

## Example Usage

```python
account_name = 'accountName4'

result = device_actions_controller.service_plan_list(account_name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |


# Account Information

Retrieve all of the service plans, features and carriers associated with the account specified.

```python
def account_information(self,
                       account_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Template, Required | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`AccountDetails`](../../doc/models/account-details.md).

## Example Usage

```python
account_name = 'accountName4'

result = device_actions_controller.account_information(account_name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |


# Retrieve the Global Device List

Allows the profile to fetch the complete device list. This works with Verizon US and Global profiles.

```python
def retrieve_the_global_device_list(self,
                                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetDeviceListWithProfilesRequest`](../../doc/models/get-device-list-with-profiles-request.md) | Body, Required | Device Profile Query |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`GIORequestResponse`](../../doc/models/gio-request-response.md).

## Example Usage

```python
body = GetDeviceListWithProfilesRequest(
    account_name='0000123456-00001',
    provisioning_status_filter='ACTIVE',
    profile_status_filter='UNKNOWN'
)

result = device_actions_controller.retrieve_the_global_device_list(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |


# Retrieve Device Provisioning History

Retrieve the provisioning history of a specific device or devices.

```python
def retrieve_device_provisioning_history(self,
                                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ProvhistoryRequest`](../../doc/models/provhistory-request.md) | Body, Required | Device Provisioning History |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`GIORequestResponse`](../../doc/models/gio-request-response.md).

## Example Usage

```python
body = ProvhistoryRequest(
    account_name='0000123456-00001',
    earliest=dateutil.parser.parse('10/15/2021 04:49:35'),
    latest=dateutil.parser.parse('10/15/2021 04:49:49')
)

result = device_actions_controller.retrieve_device_provisioning_history(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |


# Get Asynchronous Request Status

Get the status of an asynchronous request made with the Device Actions.

```python
def get_asynchronous_request_status(self,
                                   account_name,
                                   request_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Template, Required | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9\-]{3,32}$` |
| `request_id` | `str` | Template, Required | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9\-]{3,64}$` |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`StatusResponse`](../../doc/models/status-response.md).

## Example Usage

```python
account_name = '0000123456-00001'

request_id = 'd1f08526-5443-4054-9a29-4456490ea9f8'

result = device_actions_controller.get_asynchronous_request_status(
    account_name,
    request_id
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |

