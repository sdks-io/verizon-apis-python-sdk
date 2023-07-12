# Service Launch Requests

```python
service_launch_requests_controller = client.service_launch_requests
```

## Class Name

`ServiceLaunchRequestsController`

## Methods

* [Get Service Launch Request](../../doc/controllers/service-launch-requests.md#get-service-launch-request)
* [Create Service Launch Request](../../doc/controllers/service-launch-requests.md#create-service-launch-request)
* [Submit Service Launch Request](../../doc/controllers/service-launch-requests.md#submit-service-launch-request)


# Get Service Launch Request

Get information related to a service launch request.

```python
def get_service_launch_request(self,
                              account_name,
                              user_name,
                              id=None,
                              correlation_id=None,
                              name=None,
                              offset=None,
                              limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `user_name` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `id` | `uuid\|string` | Query, Optional | Service launch request Id. |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `name` | `string` | Query, Optional | Service request name.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `offset` | `long\|int` | Query, Optional | **Constraints**: `>= 0`, `<= 1024` |
| `limit` | `long\|int` | Query, Optional | **Constraints**: `>= 0`, `<= 1024` |

## Response Type

[`ServiceLaunchRequestsResult`](../../doc/models/service-launch-requests-result.md)

## Example Usage

```python
account_name = 'test_account1'

user_name = 'acme-user'

id = 'eda2cb4e-50ef-4ae8-b304-7d2f0f7a21c1'

correlation_id = 'eda2cb4e-50ef-4ae8-b304-7d2f0f7a21c1'

name = 'MdpTest3'

offset = 15

limit = 16

result = service_launch_requests_controller.get_service_launch_request(
    account_name,
    user_name,
    id,
    correlation_id,
    name,
    offset,
    limit
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 401 | Unauthorized. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 403 | Forbidden. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 404 | Not found. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 415 | Unsupported media type. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 429 | Too many requests. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| Default | Unexpected error. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |


# Create Service Launch Request

Create a request for launching a service.

```python
def create_service_launch_request(self,
                                 account_name,
                                 user_name,
                                 correlation_id=None,
                                 body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `user_name` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `body` | [`CreateServiceLaunchRequest`](../../doc/models/create-service-launch-request.md) | Body, Optional | Request for launching a service. |

## Response Type

[`ServiceLaunchRequestResult`](../../doc/models/service-launch-request-result.md)

## Example Usage

```python
account_name = 'test_account1'

user_name = 'acme-user'

correlation_id = 'eda2cb4e-50ef-4ae8-b304-7d2f0f7a21c1'

body = CreateServiceLaunchRequest(
    name='MdpTest3',
    csp_profile_id='6789409c-12c3-4fc9-b64f-71d1611c4f09',
    service_profile_id='6789409c-12c3-4fc9-b64f-71d1611c4f09',
    service_name='mongodbdemo0710',
    service_version='2.5.6'
)

result = service_launch_requests_controller.create_service_launch_request(
    account_name,
    user_name,
    correlation_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 401 | HTTP 401 Unauthorized. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 404 | HTTP 404 Not found. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| Default | HTTP 500 Internal Server Error. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |


# Submit Service Launch Request

This endpoint allows the user to submit a service request that describes the resource requirements of a service. This API submit an object of the service request and moves it to STATE from “DRAFT”  to “INSTANTIATED” and triggers the launch flow.

```python
def submit_service_launch_request(self,
                                 id,
                                 account_name,
                                 user_name,
                                 correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Template, Required | A unique Id assigned to the request by system calling API. |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9]` |
| `user_name` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9]` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |

## Response Type

[`ServiceLaunchRequestResult`](../../doc/models/service-launch-request-result.md)

## Example Usage

```python
id = 'eda2cb4e-50ef-4ae8-b304-7d2f0f7a21c1'

account_name = 'test_account1'

user_name = 'acme-user'

correlation_id = 'eda2cb4e-50ef-4ae8-b304-7d2f0f7a21c1'

result = service_launch_requests_controller.submit_service_launch_request(
    id,
    account_name,
    user_name,
    correlation_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 401 | HTTP 401 Unauthorized. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 412 | Precondition Failed. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| Default | HTTP 500 Internal Server Error. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |

