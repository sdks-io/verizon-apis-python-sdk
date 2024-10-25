# Global Reporting

```python
global_reporting_controller = client.global_reporting
```

## Class Name

`GlobalReportingController`

## Methods

* [Deviceprovhistory Using POST](../../doc/controllers/global-reporting.md#deviceprovhistory-using-post)
* [Retrieve Global List](../../doc/controllers/global-reporting.md#retrieve-global-list)


# Deviceprovhistory Using POST

Retrieve the provisioning history of a specific device or devices.

```python
def deviceprovhistory_using_post(self,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ESIMProvhistoryRequest`](../../doc/models/esim-provhistory-request.md) | Body, Required | Device Provisioning History |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ESIMRequestResponse`](../../doc/models/esim-request-response.md).

## Example Usage

```python
body = ESIMProvhistoryRequest(
    account_name='0000123456-00001',
    earliest=dateutil.parser.parse('10/15/2021 04:49:35'),
    latest=dateutil.parser.parse('10/15/2021 04:49:49')
)

result = global_reporting_controller.deviceprovhistory_using_post(body)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "d1f08526-5443-4054-9a29-4456490ea9f8"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`ESIMRestErrorResponseException`](../../doc/models/esim-rest-error-response-exception.md) |
| 401 | Unauthorized | [`ESIMRestErrorResponseException`](../../doc/models/esim-rest-error-response-exception.md) |
| 403 | Forbidden | [`ESIMRestErrorResponseException`](../../doc/models/esim-rest-error-response-exception.md) |
| 404 | Not Found / Does not exist | [`ESIMRestErrorResponseException`](../../doc/models/esim-rest-error-response-exception.md) |
| 406 | Format / Request Unacceptable | [`ESIMRestErrorResponseException`](../../doc/models/esim-rest-error-response-exception.md) |
| 429 | Too many requests | [`ESIMRestErrorResponseException`](../../doc/models/esim-rest-error-response-exception.md) |
| Default | Error response | [`ESIMRestErrorResponseException`](../../doc/models/esim-rest-error-response-exception.md) |


# Retrieve Global List

Retrieve a list of all devices associated with an account.

```python
def retrieve_global_list(self,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ESIMGlobalDeviceList`](../../doc/models/esim-global-device-list.md) | Body, Required | Device List |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ESIMRequestResponse`](../../doc/models/esim-request-response.md).

## Example Usage

```python
body = ESIMGlobalDeviceList(
    account_name='0000123456-00001',
    carrier_name_filter='VerizonWireless'
)

result = global_reporting_controller.retrieve_global_list(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`ESIMRestErrorResponseException`](../../doc/models/esim-rest-error-response-exception.md) |
| 401 | Unauthorized | [`ESIMRestErrorResponseException`](../../doc/models/esim-rest-error-response-exception.md) |
| 403 | Forbidden | [`ESIMRestErrorResponseException`](../../doc/models/esim-rest-error-response-exception.md) |
| 404 | Not Found / Does not exist | [`ESIMRestErrorResponseException`](../../doc/models/esim-rest-error-response-exception.md) |
| 406 | Format / Request Unacceptable | [`ESIMRestErrorResponseException`](../../doc/models/esim-rest-error-response-exception.md) |
| 429 | Too many requests | [`ESIMRestErrorResponseException`](../../doc/models/esim-rest-error-response-exception.md) |
| Default | Error response | [`ESIMRestErrorResponseException`](../../doc/models/esim-rest-error-response-exception.md) |

