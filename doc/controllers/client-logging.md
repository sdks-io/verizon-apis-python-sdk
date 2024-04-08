# Client Logging

```python
client_logging_controller = client.client_logging
```

## Class Name

`ClientLoggingController`

## Methods

* [List Devices With Logging Enabled](../../doc/controllers/client-logging.md#list-devices-with-logging-enabled)
* [Enable Logging for Devices](../../doc/controllers/client-logging.md#enable-logging-for-devices)
* [Disable Logging for Devices](../../doc/controllers/client-logging.md#disable-logging-for-devices)
* [Enable Device Logging](../../doc/controllers/client-logging.md#enable-device-logging)
* [Disable Device Logging](../../doc/controllers/client-logging.md#disable-device-logging)
* [List Device Logs](../../doc/controllers/client-logging.md#list-device-logs)


# List Devices With Logging Enabled

Returns an array of all devices in the specified account for which logging is enabled.

```python
def list_devices_with_logging_enabled(self,
                                     account)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[DeviceLoggingStatus]`](../../doc/models/device-logging-status.md).

## Example Usage

```python
account = '0000123456-00001'

result = client_logging_controller.list_devices_with_logging_enabled(account)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "deviceId": "990013907835573",
    "expiryDate": "2020-10-19"
  },
  {
    "deviceId": "991124018926684",
    "expiryDate": "2020-10-19"
  },
  {
    "deviceId": "992234129057795",
    "expiryDate": "2020-10-23"
  },
  {
    "deviceId": "998891785613351",
    "expiryDate": "2020-10-23"
  },
  {
    "deviceId": "990013907835573",
    "expiryDate": "2020-10-23"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# Enable Logging for Devices

Each customer may have a maximum of 20 devices enabled for logging.

```python
def enable_logging_for_devices(self,
                              account,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |
| `body` | [`DeviceLoggingRequest`](../../doc/models/device-logging-request.md) | Body, Required | Device logging information. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[DeviceLoggingStatus]`](../../doc/models/device-logging-status.md).

## Example Usage

```python
account = '0000123456-00001'

body = DeviceLoggingRequest(
    device_ids=[
        '990013907835573',
        '991124018926684',
        '992234129057795',
        '998891785613351',
        '990013907835573'
    ]
)

result = client_logging_controller.enable_logging_for_devices(
    account,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "deviceId": "990013907835573",
    "expiryDate": "2020-10-19"
  },
  {
    "deviceId": "991124018926684",
    "expiryDate": "2020-10-19"
  },
  {
    "deviceId": "992234129057795",
    "expiryDate": "2020-10-23"
  },
  {
    "deviceId": "998891785613351",
    "expiryDate": "2020-10-23"
  },
  {
    "deviceId": "990013907835573",
    "expiryDate": "2020-10-23"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# Disable Logging for Devices

Turn logging off for a list of devices.

```python
def disable_logging_for_devices(self,
                               account,
                               device_ids)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |
| `device_ids` | `str` | Query, Required | The list of device IDs. |

## Response Type

This method returns a `ApiResponse` instance.

## Example Usage

```python
account = '0000123456-00001'

device_ids = '990013907835573'

result = client_logging_controller.disable_logging_for_devices(
    account,
    device_ids
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# Enable Device Logging

Enables logging for a specific device.

```python
def enable_device_logging(self,
                         account,
                         device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |
| `device_id` | `str` | Template, Required | Device IMEI identifier. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceLoggingStatus`](../../doc/models/device-logging-status.md).

## Example Usage

```python
account = '0000123456-00001'

device_id = '990013907835573'

result = client_logging_controller.enable_device_logging(
    account,
    device_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "deviceId": "990013907835573",
  "expiryDate": "2020-10-19"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# Disable Device Logging

Disables logging for a specific device.

```python
def disable_device_logging(self,
                          account,
                          device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |
| `device_id` | `str` | Template, Required | Device IMEI identifier. |

## Response Type

This method returns a `ApiResponse` instance.

## Example Usage

```python
account = '0000123456-00001'

device_id = '990013907835573'

result = client_logging_controller.disable_device_logging(
    account,
    device_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# List Device Logs

Gets logs for a specific device.

```python
def list_device_logs(self,
                    account,
                    device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |
| `device_id` | `str` | Template, Required | Device IMEI identifier. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[DeviceLog]`](../../doc/models/device-log.md).

## Example Usage

```python
account = '0000123456-00001'

device_id = '990013907835573'

result = client_logging_controller.list_device_logs(
    account,
    device_id
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "deviceId": "990013907835573",
    "logTime": "2020-10-22T19:29:50.901Z",
    "logType": "string",
    "eventLog": "string",
    "binaryLogFileBase64": "string",
    "binaryLogFilename": "string"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |

