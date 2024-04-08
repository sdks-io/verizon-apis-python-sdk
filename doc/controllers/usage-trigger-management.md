# Usage Trigger Management

```python
usage_trigger_management_controller = client.usage_trigger_management
```

## Class Name

`UsageTriggerManagementController`

## Methods

* [Create New Trigger](../../doc/controllers/usage-trigger-management.md#create-new-trigger)
* [Update Trigger](../../doc/controllers/usage-trigger-management.md#update-trigger)
* [Delete Trigger](../../doc/controllers/usage-trigger-management.md#delete-trigger)


# Create New Trigger

Create a new usage trigger, which will send an alert when the number of device location service transactions reaches a specified percentage of the monthly subscription amount.

```python
def create_new_trigger(self,
                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`UsageTriggerAddRequest`](../../doc/models/usage-trigger-add-request.md) | Body, Optional | License assignment. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`UsageTriggerResponse`](../../doc/models/usage-trigger-response.md).

## Example Usage

```python
body = UsageTriggerAddRequest(
    account_name='0212312345-00001',
    service_name=ServiceNameEnum.LOCATION,
    threshold_value='95',
    trigger_name='95% usage alert',
    allow_excess=True,
    send_sms_notification=True,
    sms_phone_numbers='5551231234',
    send_email_notification=True,
    email_addresses='you@theinternet.com'
)

result = usage_trigger_management_controller.create_new_trigger(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "triggerId": "595f5c44-c31c-4552-8670-020a1545a84d",
  "triggerName": "90 percent",
  "accountName": "1000012345-00001",
  "serviceName": "Location",
  "thresholdValue": "90",
  "allowExcess": true,
  "sendSmsNotification": true,
  "smsPhoneNumbers": "5558794321",
  "sendEmailNotification": false,
  "emailAddresses": "",
  "createDate": "2018-08-11",
  "updateDate": "2018-08-12"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |


# Update Trigger

Update an existing usage trigger

```python
def update_trigger(self,
                  trigger_id,
                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `str` | Template, Required | Usage trigger ID |
| `body` | [`UsageTriggerUpdateRequest`](../../doc/models/usage-trigger-update-request.md) | Body, Optional | New trigger values |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`UsageTriggerResponse`](../../doc/models/usage-trigger-response.md).

## Example Usage

```python
trigger_id = '595f5c44-c31c-4552-8670-020a1545a84d'

body = UsageTriggerUpdateRequest(
    account_name='1000012345-00001',
    threshold_value='95'
)

result = usage_trigger_management_controller.update_trigger(
    trigger_id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "triggerId": "595f5c44-c31c-4552-8670-020a1545a84d",
  "triggerName": "90 percent",
  "accountName": "1000012345-00001",
  "serviceName": "Location",
  "thresholdValue": "90",
  "allowExcess": true,
  "sendSmsNotification": true,
  "smsPhoneNumbers": "5558794321",
  "sendEmailNotification": false,
  "emailAddresses": "",
  "createDate": "2018-08-11",
  "updateDate": "2018-08-12"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |


# Delete Trigger

eletes the specified usage trigger from the given account

```python
def delete_trigger(self,
                  account_name,
                  trigger_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Template, Required | Account name |
| `trigger_id` | `str` | Template, Required | Usage trigger ID |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceLocationSuccessResult`](../../doc/models/device-location-success-result.md).

## Example Usage

```python
account_name = '0212312345-00001'

trigger_id = '595f5c44-c31c-4552-8670-020a1545a84d'

result = usage_trigger_management_controller.delete_trigger(
    account_name,
    trigger_id
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
| 400 | Unexpected error | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |

