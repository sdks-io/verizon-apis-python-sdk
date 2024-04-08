# Anomaly Triggers V2

```python
anomaly_triggers_v2_controller = client.anomaly_triggers_v2
```

## Class Name

`AnomalyTriggersV2Controller`

## Methods

* [Create Anomaly Detection Trigger V2](../../doc/controllers/anomaly-triggers-v2.md#create-anomaly-detection-trigger-v2)
* [Update Anomaly Detection Trigger V2](../../doc/controllers/anomaly-triggers-v2.md#update-anomaly-detection-trigger-v2)
* [List Anomaly Detection Trigger Settings V2](../../doc/controllers/anomaly-triggers-v2.md#list-anomaly-detection-trigger-settings-v2)


# Create Anomaly Detection Trigger V2

Creates the trigger to identify an anomaly.

```python
def create_anomaly_detection_trigger_v2(self,
                                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`List[CreateTriggerRequestOptions]`](../../doc/models/create-trigger-request-options.md) | Body, Required | Request to create an anomaly trigger. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`AnomalyDetectionTrigger`](../../doc/models/anomaly-detection-trigger.md).

## Example Usage

```python
body = [
    CreateTriggerRequestOptions(
        name='Anomaly Daily Usage REST Test-Patch 1',
        trigger_category='UsageAnomaly',
        account_name='0000123456-00001',
        anomaly_trigger_request=AnomalyTriggerRequest(
            account_names='0000123456-00001',
            include_abnormal=True,
            include_very_abnormal=True,
            include_under_expected_usage=True,
            include_over_expected_usage=True
        ),
        notification=Notification(
            notification_type='DailySummary',
            callback=True,
            email_notification=False,
            notification_group_name='Anomaly Test API',
            notification_frequency_factor=3,
            notification_frequency_interval='Hourly',
            external_email_recipients='placeholder@verizon.com',
            sms_notification=True,
            sms_numbers=[
                SMSNumber(
                    carrier='US Cellular',
                    number='9299280711'
                )
            ],
            reminder=True,
            severity='Critical'
        )
    )
]

result = anomaly_triggers_v2_controller.create_anomaly_detection_trigger_v2(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "triggerId": "595f5c44-c31c-4552-8670-020a1545a84d"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | An error occurred. | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |


# Update Anomaly Detection Trigger V2

Updates an existing trigger using the account name.

```python
def update_anomaly_detection_trigger_v2(self,
                                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`List[UpdateTriggerRequestOptions]`](../../doc/models/update-trigger-request-options.md) | Body, Required | Request to update existing trigger. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`IntelligenceSuccessResult`](../../doc/models/intelligence-success-result.md).

## Example Usage

```python
body = [
    UpdateTriggerRequestOptions(
        trigger_id='595f5c44-c31c-4552-8670-020a1545a84d',
        trigger_name='Anomaly Daily Usage REST Test-Patch Update 4',
        trigger_category='UsageAnomaly',
        account_name='0000123456-00001',
        anomaly_trigger_request=AnomalyTriggerRequest(
            account_names='0000123456-00001',
            include_abnormal=True,
            include_very_abnormal=True,
            include_under_expected_usage=False,
            include_over_expected_usage=True
        ),
        notification=Notification(
            notification_type='DailySummary',
            callback=True,
            email_notification=False,
            notification_group_name='Anomaly Test API',
            notification_frequency_factor=3,
            notification_frequency_interval='Hourly',
            external_email_recipients='placeholder@verizon.com',
            sms_notification=True,
            sms_numbers=[
                SMSNumber(
                    carrier='US Cellular',
                    number='9299280711'
                )
            ],
            reminder=True,
            severity='Critical'
        )
    )
]

result = anomaly_triggers_v2_controller.update_anomaly_detection_trigger_v2(body)
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
| Default | An error occurred. | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |


# List Anomaly Detection Trigger Settings V2

Retrieves the values for a specific trigger ID.

```python
def list_anomaly_detection_trigger_settings_v2(self,
                                              trigger_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `str` | Template, Required | The trigger ID of a specific trigger. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`AnomalyTriggerResult`](../../doc/models/anomaly-trigger-result.md).

## Example Usage

```python
trigger_id = 'be1b5958-3e11-41db-9abd-b1b7618c0035'

result = anomaly_triggers_v2_controller.list_anomaly_detection_trigger_settings_v2(trigger_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "triggers": [
    {
      "triggerId": "BE1B5958-3E11-41DB-9ABD-B1B7618C0035",
      "triggerName": "Anomaly Daily Usage REST Test-1",
      "organizationName": "AnamolyDetectionRTRTest",
      "triggerCategory": "UsageAnomaly",
      "triggerAttributes": [
        {
          "key": "DataPercentage50",
          "value": false
        }
      ],
      "createdAt": "2021-10-21T23:57:03.397.0000Z",
      "modifiedAt": "2021-10-21T23:57:03.397.0000Z",
      "notification": {
        "notificationType": "DailySummary",
        "callback": true,
        "emailNotification": true,
        "notificationGroupName": "Anomaly Test API",
        "notificationFrequencyFactor": -2147483648,
        "externalEmailRecipients": "placeholder@verizon.com",
        "smsNotification": true,
        "smsNumbers": [
          {
            "carrier": "US Cellular",
            "number": "9299280711"
          }
        ],
        "reminder": false,
        "severity": "Critical"
      }
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | An error occurred. | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |

