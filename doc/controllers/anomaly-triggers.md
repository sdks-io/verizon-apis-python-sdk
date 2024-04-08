# Anomaly Triggers

```python
anomaly_triggers_controller = client.anomaly_triggers
```

## Class Name

`AnomalyTriggersController`

## Methods

* [List Anomaly Detection Triggers](../../doc/controllers/anomaly-triggers.md#list-anomaly-detection-triggers)
* [Update Anomaly Detection Trigger](../../doc/controllers/anomaly-triggers.md#update-anomaly-detection-trigger)
* [Create Anomaly Detection Trigger](../../doc/controllers/anomaly-triggers.md#create-anomaly-detection-trigger)
* [List Anomaly Detection Trigger Settings](../../doc/controllers/anomaly-triggers.md#list-anomaly-detection-trigger-settings)
* [Delete Anomaly Detection Trigger](../../doc/controllers/anomaly-triggers.md#delete-anomaly-detection-trigger)


# List Anomaly Detection Triggers

This corresponds to the M2M-MC SOAP interface, `GetTriggers`.

```python
def list_anomaly_detection_triggers(self)
```

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[GetTriggerResponseList]`](../../doc/models/get-trigger-response-list.md).

## Example Usage

```python
result = anomaly_triggers_controller.list_anomaly_detection_triggers()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| 401 | Unauthorized | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| 403 | Forbidden | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| 404 | Not Found / Does not exist | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| 406 | Format / Request Unacceptable | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| 429 | Too many requests | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| Default | Error response | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |


# Update Anomaly Detection Trigger

This corresponds to the M2M-MC SOAP interface, `UpdateTriggerRequest`.

```python
def update_anomaly_detection_trigger(self,
                                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`UpdateTriggerRequest`](../../doc/models/update-trigger-request.md) | Body, Required | Update Trigger Request |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`AnomalyDetectionTrigger`](../../doc/models/anomaly-detection-trigger.md).

## Example Usage

```python
body = UpdateTriggerRequest(
    anomaly_trigger_request=AnomalyTriggerRequest(
        account_names='0000123456-00001',
        include_abnormal=True,
        include_very_abnormal=True,
        include_under_expected_usage=True,
        include_over_expected_usage=True
    )
)

result = anomaly_triggers_controller.update_anomaly_detection_trigger(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| 401 | Unauthorized | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| 403 | Forbidden | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| 404 | Not Found / Does not exist | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| 406 | Format / Request Unacceptable | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| 429 | Too many requests | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| Default | Error response | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |


# Create Anomaly Detection Trigger

This corresponds to the M2M-MC SOAP interface, `CreateTrigger`.

```python
def create_anomaly_detection_trigger(self,
                                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateTriggerRequest`](../../doc/models/create-trigger-request.md) | Body, Required | Create Trigger Request |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`AnomalyDetectionTrigger`](../../doc/models/anomaly-detection-trigger.md).

## Example Usage

```python
body = CreateTriggerRequest(
    anomaly_trigger_request=AnomalyTriggerRequest(
        account_names='0000123456-00001',
        include_abnormal=True,
        include_very_abnormal=True,
        include_under_expected_usage=True,
        include_over_expected_usage=True
    )
)

result = anomaly_triggers_controller.create_anomaly_detection_trigger(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| 401 | Unauthorized | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| 403 | Forbidden | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| 404 | Not Found / Does not exist | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| 406 | Format / Request Unacceptable | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| 429 | Too many requests | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| Default | Error response | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |


# List Anomaly Detection Trigger Settings

This corresponds to the M2M-MC SOAP interface, `GetTriggers`.

```python
def list_anomaly_detection_trigger_settings(self,
                                           trigger_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `str` | Template, Required | trigger ID |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[GetTriggerResponseList]`](../../doc/models/get-trigger-response-list.md).

## Example Usage

```python
trigger_id = 'be1b5958-3e11-41db-9abd-b1b7618c0035'

result = anomaly_triggers_controller.list_anomaly_detection_trigger_settings(trigger_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| 401 | Unauthorized | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| 403 | Forbidden | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| 404 | Not Found / Does not exist | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| 406 | Format / Request Unacceptable | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| 429 | Too many requests | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |
| Default | Error response | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |


# Delete Anomaly Detection Trigger

Deletes a specific trigger ID

```python
def delete_anomaly_detection_trigger(self,
                                    trigger_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `str` | Template, Required | The trigger ID to be deleted |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`AnomalyDetectionTrigger`](../../doc/models/anomaly-detection-trigger.md).

## Example Usage

```python
trigger_id = 'be1b5958-3e11-41db-9abd-b1b7618c0035'

result = anomaly_triggers_controller.delete_anomaly_detection_trigger(trigger_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |

