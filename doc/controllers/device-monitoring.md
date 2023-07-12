# Device Monitoring

```python
device_monitoring_controller = client.device_monitoring
```

## Class Name

`DeviceMonitoringController`

## Methods

* [Device Reachability](../../doc/controllers/device-monitoring.md#device-reachability)
* [Stop Device Reachability](../../doc/controllers/device-monitoring.md#stop-device-reachability)


# Device Reachability

Register for notification reports based on the request type.

```python
def device_reachability(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`NotificationReportRequest`](../../doc/models/notification-report-request.md) | Body, Required | Create Reachability Report Request |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
body = NotificationReportRequest(
    account_name='0242072320-00001',
    request_type='REACHABLE_FOR_DATA',
    devices=[
        DeviceList(
            device_ids=[
                DeviceId1(
                    id='89148000004292933820',
                    kind=KindEnum.ICCID
                ),
                DeviceId1(
                    id='89148000003164287919',
                    kind=KindEnum.ICCID
                )
            ]
        )
    ],
    monitor_expiration_time='2019-12-02T15:00:00-08:00Z'
)

result = device_monitoring_controller.device_reachability(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Stop Device Reachability

Stop Device Reachability monitors.

```python
def stop_device_reachability(self,
                            account_name,
                            monitor_ids)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Query, Required | The numeric name of the account. |
| `monitor_ids` | `List of string` | Query, Required | The array contains the monitorIDs (UUID) for which the monitor is to be deleted. |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
account_name = '0242123520-00001'

monitor_ids = [
    '35596ca6-bab4-4333-a914-42b4fc2da54c',
    '35596ca6-bab4-4333-a914-42b4fc2da54b'
]

result = device_monitoring_controller.stop_device_reachability(
    account_name,
    monitor_ids
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |

