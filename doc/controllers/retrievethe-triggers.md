# Retrievethe Triggers

```python
retrievethe_triggers_controller = client.retrievethe_triggers
```

## Class Name

`RetrievetheTriggersController`

## Methods

* [Get All Available Triggers](../../doc/controllers/retrievethe-triggers.md#get-all-available-triggers)
* [Get All Triggers by Account Name](../../doc/controllers/retrievethe-triggers.md#get-all-triggers-by-account-name)
* [Get All Triggers by Trigger Category](../../doc/controllers/retrievethe-triggers.md#get-all-triggers-by-trigger-category)
* [Get Triggers by Id](../../doc/controllers/retrievethe-triggers.md#get-triggers-by-id)


# Get All Available Triggers

Retrieves all of the available triggers for pseudo-MDN.

```python
def get_all_available_triggers(self)
```

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`TriggerValueResponse`](../../doc/models/trigger-value-response.md).

## Example Usage

```python
result = retrieve_the_triggers_controller.get_all_available_triggers()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ReadySimRestErrorResponseException`](../../doc/models/ready-sim-rest-error-response-exception.md) |


# Get All Triggers by Account Name

Retrieve the triggers associated with an account name.

```python
def get_all_triggers_by_account_name(self,
                                    account_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Template, Required | The account name |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`TriggerValueResponse`](../../doc/models/trigger-value-response.md).

## Example Usage

```python
account_name = '0000123456-000001'

result = retrieve_the_triggers_controller.get_all_triggers_by_account_name(account_name)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ReadySimRestErrorResponseException`](../../doc/models/ready-sim-rest-error-response-exception.md) |


# Get All Triggers by Trigger Category

Retrieves all of the triggers for the specified account associated with the PromoAlert category

```python
def get_all_triggers_by_trigger_category(self)
```

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`TriggerValueResponse2`](../../doc/models/trigger-value-response-2.md).

## Example Usage

```python
result = retrieve_the_triggers_controller.get_all_triggers_by_trigger_category()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ReadySimRestErrorResponseException`](../../doc/models/ready-sim-rest-error-response-exception.md) |


# Get Triggers by Id

Retrives a specific trigger by its ID.

```python
def get_triggers_by_id(self,
                      trigger_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `str` | Template, Required | The ID of a specific trigger |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`TriggerValueResponse2`](../../doc/models/trigger-value-response-2.md).

## Example Usage

```python
trigger_id = '2874DEC7-26CF-4797-9C6A-B5A2AC72D526'

result = retrieve_the_triggers_controller.get_triggers_by_id(trigger_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ReadySimRestErrorResponseException`](../../doc/models/ready-sim-rest-error-response-exception.md) |

