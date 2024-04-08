# Anomaly Settings

```python
anomaly_settings_controller = client.anomaly_settings
```

## Class Name

`AnomalySettingsController`

## Methods

* [Activate Anomaly Detection](../../doc/controllers/anomaly-settings.md#activate-anomaly-detection)
* [List Anomaly Detection Settings](../../doc/controllers/anomaly-settings.md#list-anomaly-detection-settings)
* [Reset Anomaly Detection Parameters](../../doc/controllers/anomaly-settings.md#reset-anomaly-detection-parameters)


# Activate Anomaly Detection

Uses the subscribed account ID to activate anomaly detection and set threshold values.

```python
def activate_anomaly_detection(self,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AnomalyDetectionRequest`](../../doc/models/anomaly-detection-request.md) | Body, Required | Request to activate anomaly detection. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`IntelligenceSuccessResult`](../../doc/models/intelligence-success-result.md).

## Example Usage

```python
body = AnomalyDetectionRequest(
    account_name='0000123456-00001',
    request_type='anomaly',
    sensitivity_parameter=SensitivityParameters(
        abnormal_max_value=1.1,
        enable_abnormal=True,
        enable_very_abnormal=True,
        very_abnormal_max_value=0.55
    )
)

result = anomaly_settings_controller.activate_anomaly_detection(body)
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


# List Anomaly Detection Settings

Retrieves the current anomaly detection settings for an account.

```python
def list_anomaly_detection_settings(self,
                                   account_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Template, Required | The name of the subscribed account. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`AnomalyDetectionSettings`](../../doc/models/anomaly-detection-settings.md).

## Example Usage

```python
account_name = '0000123456-00001'

result = anomaly_settings_controller.list_anomaly_detection_settings(account_name)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "Success",
  "sensitivityParameter": {
    "abnormalMaxValue": 1.1,
    "enableAbnormal": true,
    "enableVeryAbnormal": true,
    "veryAbnormalMaxValue": 0.55
  },
  "status": "Active"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | An error occurred. | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |


# Reset Anomaly Detection Parameters

Resets the thresholds to zero.

```python
def reset_anomaly_detection_parameters(self,
                                      account_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Template, Required | The name of the subscribed account. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`IntelligenceSuccessResult`](../../doc/models/intelligence-success-result.md).

## Example Usage

```python
account_name = '0000123456-00001'

result = anomaly_settings_controller.reset_anomaly_detection_parameters(account_name)
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

