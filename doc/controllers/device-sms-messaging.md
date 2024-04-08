# Device SMS Messaging

```python
device_sms_messaging_controller = client.device_sms_messaging
```

## Class Name

`DeviceSMSMessagingController`

## Methods

* [Send an Sms Message](../../doc/controllers/device-sms-messaging.md#send-an-sms-message)
* [Get Sms Messages](../../doc/controllers/device-sms-messaging.md#get-sms-messages)
* [Start Sms Message Delivery](../../doc/controllers/device-sms-messaging.md#start-sms-message-delivery)
* [List Sms Message History](../../doc/controllers/device-sms-messaging.md#list-sms-message-history)


# Send an Sms Message

Sends an SMS message to one device. Messages are queued on the M2M MC Platform and sent as soon as possible, but they may be delayed due to traffic and routing considerations.

```python
def send_an_sms_message(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GIOSMSSendRequest`](../../doc/models/giosms-send-request.md) | Body, Required | SMS message to an indiividual device. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`GIORequestResponse`](../../doc/models/gio-request-response.md).

## Example Usage

```python
body = GIOSMSSendRequest(
    device_ids=[
        GIODeviceId(
            kind='eid',
            id='12345678901234567890123456789012'
        )
    ],
    sms_message='A text message'
)

result = device_sms_messaging_controller.send_an_sms_message(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |


# Get Sms Messages

Retrieves queued SMS messages sent by all M2M MC devices associated with an account.

```python
def get_sms_messages(self,
                    account_name,
                    next=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Template, Required | Numeric account name |
| `next` | `str` | Query, Optional | Continue the previous query from the pageUrl in Location Header |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`SmsMessagesResponse`](../../doc/models/sms-messages-response.md).

## Example Usage

```python
account_name = '0000123456-00001'

next = 'TheURLForTheNextQuery'

result = device_sms_messaging_controller.get_sms_messages(
    account_name,
    next=next
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |


# Start Sms Message Delivery

Starts delivery of SMS messages for the specified account.

```python
def start_sms_message_delivery(self,
                              account_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Template, Required | Numeric account name |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`SuccessResponse`](../../doc/models/success-response.md).

## Example Usage

```python
account_name = '0000123456-00001'

result = device_sms_messaging_controller.start_sms_message_delivery(account_name)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |


# List Sms Message History

Returns a list of sms history for a given device during a specified time frame.

```python
def list_sms_message_history(self,
                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SMSEventHistoryRequest`](../../doc/models/sms-event-history-request.md) | Body, Required | Device Query |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`GIORequestResponse`](../../doc/models/gio-request-response.md).

## Example Usage

```python
body = SMSEventHistoryRequest(
    device_id=GIODeviceId(
        kind='eid',
        id='12345678901234567890123456789012'
    )
)

result = device_sms_messaging_controller.list_sms_message_history(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |

