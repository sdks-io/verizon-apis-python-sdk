# V2 Triggers

Helps to create and manage promo alert triggers

```python
m_v2_triggers_controller = client.m_v2_triggers
```

## Class Name

`MV2TriggersController`

## Methods

* [Create Trigger](../../doc/controllers/v2-triggers.md#create-trigger)
* [Update Trigger](../../doc/controllers/v2-triggers.md#update-trigger)


# Create Trigger

This creates an individual change plan for account group share.

```python
def create_trigger(self,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateTriggerV2Request`](../../doc/models/create-trigger-v2-request.md) | Body, Required | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`TriggerV2Response`](../../doc/models/trigger-v2-response.md).

## Example Usage

```python
body = CreateTriggerV2Request()

result = m_v2_triggers_controller.create_trigger(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RulesEngineRestErrorResponseException`](../../doc/models/rules-engine-rest-error-response-exception.md) |


# Update Trigger

This updates an individual change plan for account group share.

```python
def update_trigger(self,
                  vz_m2m_token,
                  body,
                  x_request_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vz_m2m_token` | `str` | Header, Required | M2M-MC Session Token |
| `body` | [`UpdateTriggerV2Request`](../../doc/models/update-trigger-v2-request.md) | Body, Required | - |
| `x_request_id` | `str` | Header, Optional | Transaction Id |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`TriggerV2Response`](../../doc/models/trigger-v2-response.md).

## Example Usage

```python
vz_m2m_token = 'VZ-M2M-Token2'

body = UpdateTriggerV2Request()

result = m_v2_triggers_controller.update_trigger(
    vz_m2m_token,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RulesEngineRestErrorResponseException`](../../doc/models/rules-engine-rest-error-response-exception.md) |

