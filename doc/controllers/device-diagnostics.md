# Device Diagnostics

```python
device_diagnostics_controller = client.device_diagnostics
```

## Class Name

`DeviceDiagnosticsController`

## Methods

* [Device Reachability Status Using POST](../../doc/controllers/device-diagnostics.md#device-reachability-status-using-post)
* [Retrieve Active Monitors Using POST](../../doc/controllers/device-diagnostics.md#retrieve-active-monitors-using-post)


# Device Reachability Status Using POST

If the devices do not already exist in the account, this API resource adds them before activation.

```python
def device_reachability_status_using_post(self,
                                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`NotificationReportStatusRequest`](../../doc/models/notification-report-status-request.md) | Body, Required | Retrieve Reachability Report Status for a device. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = NotificationReportStatusRequest(
    account_name='0868924207-00001',
    device=DeviceId(
        id='990013907835573',
        kind='imei'
    ),
    request_type='requestType6'
)

result = device_diagnostics_controller.device_reachability_status_using_post(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "595f5c44-c31c-4552-8670-020a1545a84d"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# Retrieve Active Monitors Using POST

Retrieve all the active monitors.

```python
def retrieve_active_monitors_using_post(self,
                                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`RetrieveMonitorsRequest`](../../doc/models/retrieve-monitors-request.md) | Body, Required | Retrieve Monitor Request. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = RetrieveMonitorsRequest(
    account_name='0868924207-00001',
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='990013907835573',
                    kind='imei'
                ),
                DeviceId(
                    id='89141390780800784259',
                    kind='iccid'
                )
            ]
        ),
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='990013907884259',
                    kind='imei'
                ),
                DeviceId(
                    id='89141390780800735573',
                    kind='iccid'
                )
            ]
        )
    ],
    monitor_type='monitorType'
)

result = device_diagnostics_controller.retrieve_active_monitors_using_post(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "595f5c44-c31c-4552-8670-020a1545a84d"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |

