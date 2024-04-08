# Update Triggers

```python
update_triggers_controller = client.update_triggers
```

## Class Name

`UpdateTriggersController`


# Update All Available Triggers

Updates the promotional triggers for pseudo-MDN.

```python
def update_all_available_triggers(self,
                                 body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`RequestTrigger`](../../doc/models/request-trigger.md) | Body, Optional | Update the triggers |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Success`](../../doc/models/success.md).

## Example Usage

```python
body = RequestTrigger(
    trigger_id='2874DEC7-26CF-4797-9C6A-B5A2AC72D526',
    trigger_name='PromoAlerts_0000000000-00001_23456789',
    account_name='0000123456-000001',
    organization_name='Optional group name',
    trigger_category='PromoAlerts'
)

result = update_triggers_controller.update_all_available_triggers(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "status": "Success"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ReadySimRestErrorResponseException`](../../doc/models/ready-sim-rest-error-response-exception.md) |

