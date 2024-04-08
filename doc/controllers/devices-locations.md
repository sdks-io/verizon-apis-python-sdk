# Devices Locations

```python
devices_locations_controller = client.devices_locations
```

## Class Name

`DevicesLocationsController`

## Methods

* [List Devices Locations Synchronous](../../doc/controllers/devices-locations.md#list-devices-locations-synchronous)
* [List Devices Locations Asynchronous](../../doc/controllers/devices-locations.md#list-devices-locations-asynchronous)
* [Cancel Device Location Request](../../doc/controllers/devices-locations.md#cancel-device-location-request)
* [Create Location Report](../../doc/controllers/devices-locations.md#create-location-report)
* [Retrieve Location Report](../../doc/controllers/devices-locations.md#retrieve-location-report)
* [Get Location Report Status](../../doc/controllers/devices-locations.md#get-location-report-status)
* [Cancel Queued Location Report Generation](../../doc/controllers/devices-locations.md#cancel-queued-location-report-generation)


# List Devices Locations Synchronous

This locations endpoint retrieves the locations for a list of devices.

```python
def list_devices_locations_synchronous(self,
                                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LocationRequest`](../../doc/models/location-request.md) | Body, Required | Request to obtain location of devices. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[Location]`](../../doc/models/location.md).

## Example Usage

```python
body = LocationRequest(
    account_name='1234567890-00001',
    device_list=[
        DeviceInfo(
            id='980003420535573',
            kind='imei',
            mdn='7892345678'
        ),
        DeviceInfo(
            id='375535024300089',
            kind='imei',
            mdn='7897654321'
        ),
        DeviceInfo(
            id='A100003861E585',
            kind='meid',
            mdn='7897650914'
        )
    ],
    accuracy_mode=AccuracyModeEnum.ENUM_0,
    cache_mode=CacheModeEnum.ENUM_1
)

result = devices_locations_controller.list_devices_locations_synchronous(body)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "msid": "7892345678",
    "pd": {
      "time": "20170520004421",
      "x": "33.45324",
      "y": "-84.59621",
      "radius": "5571",
      "qos": false
    },
    "error": {}
  },
  {
    "msid": "8583239709",
    "pd": {
      "time": "20170525214342",
      "x": "38.8408694",
      "y": "-105.0422583",
      "radius": "3866",
      "qos": false
    },
    "error": {}
  },
  {
    "msid": "7897654321",
    "pd": {},
    "error": {
      "time": "20170525214342",
      "type": "POSITION METHOD FAILURE",
      "info": "Exception code=ABSENT SUBSCRIBER"
    }
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |


# List Devices Locations Asynchronous

Requests the current or cached location of up to 10,000 IoT or consumer devices (phones, tablets. etc.). This request returns a synchronous transaction ID, and the location information for each device is returned asynchronously as a DeviceLocation callback message.

```python
def list_devices_locations_asynchronous(self,
                                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LocationRequest`](../../doc/models/location-request.md) | Body, Required | An asynchronous request to obtain locations of devices. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`SynchronousLocationRequestResult`](../../doc/models/synchronous-location-request-result.md).

## Example Usage

```python
body = LocationRequest(
    account_name='2234434445-32333',
    device_list=[
        DeviceInfo(
            id='354677790348290',
            kind='imei',
            mdn='5557337468'
        )
    ],
    accuracy_mode=AccuracyModeEnum.ENUM_0,
    cache_mode=CacheModeEnum.ENUM_2
)

result = devices_locations_controller.list_devices_locations_asynchronous(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "txid": "4be7c858-0ef9-4b15-a0c1-95061456d835",
  "status": "QUEUED"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |


# Cancel Device Location Request

Cancel a queued or unfinished device location request.

```python
def cancel_device_location_request(self,
                                  account_name,
                                  txid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Query, Required | Account identifier in "##########-#####". |
| `txid` | `str` | Template, Required | Transaction ID of the request to cancel, from the synchronous response to the original request. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`TransactionID`](../../doc/models/transaction-id.md).

## Example Usage

```python
account_name = '1234567890-00001'

txid = '2c90bd28-ece4-42ef-9f02-7e3bd4fbff33'

result = devices_locations_controller.cancel_device_location_request(
    account_name,
    txid
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "txid": "2c90bd28-ece4-42ef-9f02-7e3bd4fbff33"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |


# Create Location Report

Request an asynchronous device location report.

```python
def create_location_report(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LocationRequest`](../../doc/models/location-request.md) | Body, Required | Request for device location report. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`AsynchronousLocationRequestResult`](../../doc/models/asynchronous-location-request-result.md).

## Example Usage

```python
body = LocationRequest(
    account_name='1234567890-00001',
    device_list=[
        DeviceInfo(
            id='980003420535573',
            kind='imei',
            mdn='7892345678'
        ),
        DeviceInfo(
            id='375535024300089',
            kind='imei',
            mdn='7897654321'
        ),
        DeviceInfo(
            id='A100003861E585',
            kind='meid',
            mdn='7897650914'
        )
    ],
    accuracy_mode=AccuracyModeEnum.ENUM_0,
    cache_mode=CacheModeEnum.ENUM_1
)

result = devices_locations_controller.create_location_report(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "txid": "2c90bd28-ece4-42ef-9f02-7e3bd4fbff33",
  "status": "QUEUED"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |


# Retrieve Location Report

Download a completed asynchronous device location report.

```python
def retrieve_location_report(self,
                            account,
                            txid,
                            startindex)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier in "##########-#####". |
| `txid` | `str` | Template, Required | Transaction ID from POST /locationreports response. |
| `startindex` | `int` | Template, Required | Zero-based number of the first record to return. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`LocationReport`](../../doc/models/location-report.md).

## Example Usage

```python
account = '0252012345-00001'

txid = '2017-12-11Te8b47da2-3a45-46cf-9903-61815e1e97e9'

startindex = 0

result = devices_locations_controller.retrieve_location_report(
    account,
    txid,
    startindex
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "startIndex": "0",
  "txid": "2017-12-11Te8b47da2-3a45-46cf-9903-61815e1e97e9",
  "totalCount": 3,
  "hasMoreData": false,
  "devLocationList": [
    {
      "error": {},
      "msid": "7892345678",
      "pd": {
        "qos": false,
        "radius": "5571",
        "time": "20170520004421",
        "x": "33.45324",
        "y": "-84.59621"
      }
    },
    {
      "error": {},
      "msid": "8583239709",
      "pd": {
        "qos": false,
        "radius": "3866",
        "time": "20170525214342",
        "x": "38.8408694",
        "y": "-105.0422583"
      }
    },
    {
      "error": {
        "time": "20170525214342",
        "type": "POSITION METHOD FAILURE",
        "info": "Exception code=ABSENT SUBSCRIBER"
      },
      "msid": "7897654321",
      "pd": {}
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |


# Get Location Report Status

Returns the current status of a requested device location report.

```python
def get_location_report_status(self,
                              account,
                              txid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier in "##########-#####". |
| `txid` | `str` | Template, Required | Transaction ID of the report. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`LocationReportStatus`](../../doc/models/location-report-status.md).

## Example Usage

```python
account = '0252012345-00001'

txid = '2c90bd28-ece4-42ef-9f02-7e3bd4fbff33'

result = devices_locations_controller.get_location_report_status(
    account,
    txid
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "txid": "2c90bd28-ece4-42ef-9f02-7e3bd4fbff33",
  "status": "INPROGRESS"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |


# Cancel Queued Location Report Generation

Cancel a queued device location report.

```python
def cancel_queued_location_report_generation(self,
                                            account,
                                            txid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier in "##########-#####". |
| `txid` | `str` | Template, Required | Transaction ID of the report to cancel. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`TransactionID`](../../doc/models/transaction-id.md).

## Example Usage

```python
account = '0252012345-00001'

txid = '2c90bd28-ece4-42ef-9f02-7e3bd4fbff33'

result = devices_locations_controller.cancel_queued_location_report_generation(
    account,
    txid
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "txid": "2c90bd28-ece4-42ef-9f02-7e3bd4fbff33"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |

