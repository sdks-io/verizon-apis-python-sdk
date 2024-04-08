# SIM Securefor Io T Licenses

```python
sim_securefor_io_t_licenses_controller = client.sim_securefor_io_t_licenses
```

## Class Name

`SIMSecureforIoTLicensesController`

## Methods

* [Assign License to Devices](../../doc/controllers/sim-securefor-io-t-licenses.md#assign-license-to-devices)
* [Unassign License to Devices](../../doc/controllers/sim-securefor-io-t-licenses.md#unassign-license-to-devices)


# Assign License to Devices

Assigns SIM-Secure for IoT licenses to SIMs.

```python
def assign_license_to_devices(self,
                             body,
                             x_request_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AssignLicenseRequest`](../../doc/models/assign-license-request.md) | Body, Required | Request to assign license to devices. |
| `x_request_id` | `str` | Header, Optional | Transaction Id. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`SecuritySuccessResult`](../../doc/models/security-success-result.md).

## Example Usage

```python
body = AssignLicenseRequest(
    account_name='0000123456-00001',
    devices=[
        LicenseDeviceList(
            device_ids=[
                LicenseDeviceId(
                    id='864508030109877',
                    kind='IMEI'
                )
            ]
        )
    ],
    sku_number='SIMSec-IoT-Lt'
)

result = sim_secure_for_io_t_licenses_controller.assign_license_to_devices(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "c3f3d17c-79ff-4b35-82df-94446785b6e0"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request. | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 401 | Unauthorized request. | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 403 | Request Forbidden. | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 404 | Not Found / Does not exist. | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 406 | Format / Request Unacceptable. | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 429 | Too many requests. | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| Default | Error response. | [`SecurityResultException`](../../doc/models/security-result-exception.md) |


# Unassign License to Devices

Unassigns SIM-Secure for IoT Flexible and Flexible Bundle license from SIMs.

```python
def unassign_license_to_devices(self,
                               x_request_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `x_request_id` | `str` | Header, Required | Transaction Id. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`SecuritySuccessResult`](../../doc/models/security-success-result.md).

## Example Usage

```python
x_request_id = 'X-Request-ID2'

result = sim_secure_for_io_t_licenses_controller.unassign_license_to_devices(x_request_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "1f28c944-d007-44c9-9543-003b8820cc69"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request. | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 401 | Unauthorized request. | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 403 | Request forbidden. | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 404 | Not Found / Does not exist. | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 406 | Format / Request Unacceptable. | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 429 | Too many requests. | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| Default | Error response. | [`SecurityResultException`](../../doc/models/security-result-exception.md) |

