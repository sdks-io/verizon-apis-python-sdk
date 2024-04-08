# Performance Metrics

```python
performance_metrics_controller = client.performance_metrics
```

## Class Name

`PerformanceMetricsController`


# Query MEC Performance Metrics

Query the most recent data for Key Performance Indicators (KPIs) like network availability, MEC hostnames and more.

```python
def query_mec_performance_metrics(self,
                                 body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`QueryMECPerformanceMetricsRequest`](../../doc/models/query-mec-performance-metrics-request.md) | Body, Optional | - |

## Requires scope

### oAuth2

`discovery:read`, `serviceprofile:read`, `serviceprofile:write`, `serviceregistry:read`, `serviceregistry:write`, `ts.application.ro`, `ts.mec.fullaccess`, `ts.mec.limitaccess`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`MECPerformanceMetrics`](../../doc/models/mec-performance-metrics.md).

## Example Usage

```python
body = QueryMECPerformanceMetricsRequest(
    imei='440246108109673',
    msisdn='10691876598'
)

result = performance_metrics_controller.query_mec_performance_metrics(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "QueryStatus": "Success",
  "Start": "1/28/2021 12:00:00",
  "End": "1/28/2021 12:15:00",
  "QueryResult": [
    {
      "name": "NetworkAvailability",
      "data": [
        "100",
        "percent",
        "high"
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request. | [`EdgePerformanceResultException`](../../doc/models/edge-performance-result-exception.md) |
| 401 | Unauthorized request. | [`EdgePerformanceResultException`](../../doc/models/edge-performance-result-exception.md) |
| 403 | Request forbidden. | [`EdgePerformanceResultException`](../../doc/models/edge-performance-result-exception.md) |
| 404 | Resource Not Found. | [`EdgePerformanceResultException`](../../doc/models/edge-performance-result-exception.md) |
| 405 | Method Not Allowed. | [`EdgePerformanceResultException`](../../doc/models/edge-performance-result-exception.md) |
| 503 | Service Unavailable. | [`EdgePerformanceResultException`](../../doc/models/edge-performance-result-exception.md) |

