# Service Instance Operations

```python
service_instance_operations_controller = client.service_instance_operations
```

## Class Name

`ServiceInstanceOperationsController`

## Methods

* [Service Resume](../../doc/controllers/service-instance-operations.md#service-resume)
* [Service Suspend](../../doc/controllers/service-instance-operations.md#service-suspend)
* [Service Remove](../../doc/controllers/service-instance-operations.md#service-remove)
* [Service Upgrade](../../doc/controllers/service-instance-operations.md#service-upgrade)


# Service Resume

Resumes a suspended Service Instance

```python
def service_resume(self,
                  service_instance_id,
                  user_id,
                  request_id,
                  user_role,
                  customer_id,
                  correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_instance_id` | `string` | Template, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `user_id` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `request_id` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `user_role` | [`UserRoleEnum`](../../doc/models/user-role-enum.md) | Header, Required | **Constraints**: *Maximum Length*: `500` |
| `customer_id` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |

## Response Type

[`ServiceResumeResult`](../../doc/models/service-resume-result.md)

## Example Usage

```python
service_instance_id = 'serviceInstanceId2'

user_id = 'userId0'

request_id = 'requestId2'

user_role = UserRoleEnum.ORGADMIN

customer_id = 'customerId6'

result = service_instance_operations_controller.service_resume(
    service_instance_id,
    user_id,
    request_id,
    user_role,
    customer_id
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


# Service Suspend

Suspend a service Instance

```python
def service_suspend(self,
                   service_instance_id,
                   user_id,
                   request_id,
                   user_role,
                   customer_id,
                   correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_instance_id` | `string` | Template, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `user_id` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `request_id` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `user_role` | [`UserRoleEnum`](../../doc/models/user-role-enum.md) | Header, Required | **Constraints**: *Maximum Length*: `500` |
| `customer_id` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |

## Response Type

[`ServiceResumeResult`](../../doc/models/service-resume-result.md)

## Example Usage

```python
service_instance_id = 'serviceInstanceId2'

user_id = 'userId0'

request_id = 'requestId2'

user_role = UserRoleEnum.ORGADMIN

customer_id = 'customerId6'

result = service_instance_operations_controller.service_suspend(
    service_instance_id,
    user_id,
    request_id,
    user_role,
    customer_id
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


# Service Remove

remove a service Instance

```python
def service_remove(self,
                  service_instance_id,
                  user_id,
                  request_id,
                  user_role,
                  customer_id,
                  correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_instance_id` | `string` | Template, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `user_id` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `request_id` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `user_role` | [`UserRoleEnum`](../../doc/models/user-role-enum.md) | Header, Required | **Constraints**: *Maximum Length*: `500` |
| `customer_id` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |

## Response Type

[`ServiceResumeResult`](../../doc/models/service-resume-result.md)

## Example Usage

```python
service_instance_id = 'serviceInstanceId2'

user_id = 'userId0'

request_id = 'requestId2'

user_role = UserRoleEnum.ORGADMIN

customer_id = 'customerId6'

result = service_instance_operations_controller.service_remove(
    service_instance_id,
    user_id,
    request_id,
    user_role,
    customer_id
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


# Service Upgrade

upgrade a service Instance

```python
def service_upgrade(self,
                   service_instance_id,
                   user_id,
                   request_id,
                   user_role,
                   customer_id,
                   correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_instance_id` | `string` | Template, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `user_id` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `request_id` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `user_role` | [`UserRoleEnum`](../../doc/models/user-role-enum.md) | Header, Required | **Constraints**: *Maximum Length*: `500` |
| `customer_id` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |

## Response Type

[`ServiceResumeResult`](../../doc/models/service-resume-result.md)

## Example Usage

```python
service_instance_id = 'serviceInstanceId2'

user_id = 'userId0'

request_id = 'requestId2'

user_role = UserRoleEnum.ORGADMIN

customer_id = 'customerId6'

result = service_instance_operations_controller.service_upgrade(
    service_instance_id,
    user_id,
    request_id,
    user_role,
    customer_id
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

