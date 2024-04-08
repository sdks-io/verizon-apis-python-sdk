# Device Reports

```python
device_reports_controller = client.device_reports
```

## Class Name

`DeviceReportsController`

## Methods

* [Calculate Aggregated Report Synchronous](../../doc/controllers/device-reports.md#calculate-aggregated-report-synchronous)
* [Calculate Aggregated Report Asynchronous](../../doc/controllers/device-reports.md#calculate-aggregated-report-asynchronous)
* [Get Sessions Report](../../doc/controllers/device-reports.md#get-sessions-report)


# Calculate Aggregated Report Synchronous

Calculate aggregated report per day with number of sessions and usage information. User will receive synchronous response for specified list of devices (Max 10) and date range (Max 180 days).

```python
def calculate_aggregated_report_synchronous(self,
                                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AggregateSessionReportRequest`](../../doc/models/aggregate-session-report-request.md) | Body, Required | Aggregated report request. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`AggregateSessionReport`](../../doc/models/aggregate-session-report.md).

## Example Usage

```python
body = AggregateSessionReportRequest(
    account_number='0844021539-00001',
    imei=[
        '709312034493372'
    ],
    start_date='2022-12-09T22:01:06.217Z',
    end_date='2022-12-09T22:01:08.734Z',
    no_session_flag='false'
)

result = device_reports_controller.calculate_aggregated_report_synchronous(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "txid": null,
  "usage": [
    {
      "imei": "709312034493372",
      "numberOfSessions": 1,
      "bytesTransferred": 2057
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 401 | Unauthorized request. Access token is missing or invalid. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 403 | Forbidden request. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 404 | Bad request. Not found. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 409 | Bad request. Conflict state. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 500 | Internal Server Error. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |


# Calculate Aggregated Report Asynchronous

Calculate aggregated report per day with number of sessions and usage information. User will receive an asynchronous callback for the specified list of devices (Max 10000) and date range (Max 180 days).

```python
def calculate_aggregated_report_asynchronous(self,
                                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AggregateSessionReportRequest`](../../doc/models/aggregate-session-report-request.md) | Body, Required | Aggregated session report request. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`AggregatedReportCallbackResult`](../../doc/models/aggregated-report-callback-result.md).

## Example Usage

```python
body = AggregateSessionReportRequest(
    account_number='0844021539-00001',
    imei=[
        '709312034493372'
    ],
    start_date='2022-12-09T22:01:06.217Z',
    end_date='2022-12-09T22:01:08.734Z',
    no_session_flag='false'
)

result = device_reports_controller.calculate_aggregated_report_asynchronous(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "txid": "60c07fff-470b-4d6d-afcc-75e6a7c238f6",
  "status": "QUEUED"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 401 | Unauthorized request. Access token is missing or invalid. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 403 | Forbidden request. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 404 | Bad request. Not found. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 409 | Bad request. Conflict state. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 500 | Internal Server Error. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |


# Get Sessions Report

Detailed report of session duration and number of bytes transferred per day.

```python
def get_sessions_report(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SessionReportRequest`](../../doc/models/session-report-request.md) | Body, Required | Request for sessions report. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`SessionReport`](../../doc/models/session-report.md).

## Example Usage

```python
body = SessionReportRequest(
    account_number='0844021539-00001',
    imei='709312034493372',
    start_date='2022-12-09T22:01:06.217Z',
    end_date='2022-12-09T22:01:08.734Z'
)

result = device_reports_controller.get_sessions_report(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "709312034493372",
  "txid": "60c07fff-470b-4d6d-afcc-75e6a7c238f6"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 401 | Unauthorized request. Access token is missing or invalid. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 403 | Forbidden request. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 404 | Bad request. Not found. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 409 | Bad request. Conflict state. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 500 | Internal Server Error. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |

