# Managinge SIM Profiles

```python
managinge_sim_profiles_controller = client.managinge_sim_profiles
```

## Class Name

`ManagingeSIMProfilesController`

## Methods

* [Activate a Device Profile](../../doc/controllers/managinge-sim-profiles.md#activate-a-device-profile)
* [Enable a Device Profile](../../doc/controllers/managinge-sim-profiles.md#enable-a-device-profile)
* [Deactivate a Device Profile](../../doc/controllers/managinge-sim-profiles.md#deactivate-a-device-profile)
* [Enable a Device Profile for Download](../../doc/controllers/managinge-sim-profiles.md#enable-a-device-profile-for-download)
* [Download a Device Profile](../../doc/controllers/managinge-sim-profiles.md#download-a-device-profile)
* [Delete a Device Profile](../../doc/controllers/managinge-sim-profiles.md#delete-a-device-profile)


# Activate a Device Profile

Activate a device with either a lead or local profile.

```python
def activate_a_device_profile(self,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GIOProfileRequest`](../../doc/models/gio-profile-request.md) | Body, Required | Device Profile Query |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`GIORequestResponse`](../../doc/models/gio-request-response.md).

## Example Usage

```python
body = GIOProfileRequest(
    devices=[
        GIODeviceList()
    ],
    account_name='0000123456-00001',
    mdn_zip_code='12345',
    service_plan='service plan name'
)

result = managing_e_sim_profiles_controller.activate_a_device_profile(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |


# Enable a Device Profile

Enable a device lead or local profile.

```python
def enable_a_device_profile(self,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceProfileRequest`](../../doc/models/device-profile-request.md) | Body, Required | Device Profile Query |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`GIORequestResponse`](../../doc/models/gio-request-response.md).

## Example Usage

```python
body = DeviceProfileRequest(
    account_name='0000123456-00001',
    service_plan='service plan name'
)

result = managing_e_sim_profiles_controller.enable_a_device_profile(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |


# Deactivate a Device Profile

Deactivate the lead or local profile. **Note:** to reactivate the profile, use the **Activate** endpoint above.

```python
def deactivate_a_device_profile(self,
                               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GIODeactivateDeviceProfileRequest`](../../doc/models/gio-deactivate-device-profile-request.md) | Body, Required | Device Profile Query |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`GIORequestResponse`](../../doc/models/gio-request-response.md).

## Example Usage

```python
body = GIODeactivateDeviceProfileRequest(
    account_name='0000123456-00001',
    service_plan='service plan name',
    etf_waiver=False,
    reason_code='FF'
)

result = managing_e_sim_profiles_controller.deactivate_a_device_profile(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |


# Enable a Device Profile for Download

Enable the Global IoT Orchestration device profile for download.

```python
def enable_a_device_profile_for_download(self,
                                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceProfileRequest`](../../doc/models/device-profile-request.md) | Body, Required | Device Profile Query |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`GIORequestResponse`](../../doc/models/gio-request-response.md).

## Example Usage

```python
body = DeviceProfileRequest(
    account_name='0000123456-00001',
    service_plan='service plan name'
)

result = managing_e_sim_profiles_controller.enable_a_device_profile_for_download(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |


# Download a Device Profile

Download a Global IoT Orchestration device profile.

```python
def download_a_device_profile(self,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceProfileRequest`](../../doc/models/device-profile-request.md) | Body, Required | Device Profile Query |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`GIORequestResponse`](../../doc/models/gio-request-response.md).

## Example Usage

```python
body = DeviceProfileRequest(
    account_name='0000123456-00001',
    service_plan='service plan name'
)

result = managing_e_sim_profiles_controller.download_a_device_profile(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |


# Delete a Device Profile

Delete a device profile for Global IoT Orchestration. **Note:** the profile must be deactivated first!

```python
def delete_a_device_profile(self,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceProfileRequest`](../../doc/models/device-profile-request.md) | Body, Required | Device Profile Query |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`GIORequestResponse`](../../doc/models/gio-request-response.md).

## Example Usage

```python
body = DeviceProfileRequest(
    account_name='0000123456-00001',
    service_plan='service plan name'
)

result = managing_e_sim_profiles_controller.delete_a_device_profile(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |

