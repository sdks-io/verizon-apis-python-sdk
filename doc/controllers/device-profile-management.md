# Device Profile Management

```python
device_profile_management_controller = client.device_profile_management
```

## Class Name

`DeviceProfileManagementController`

## Methods

* [Activate Device Through Profile](../../doc/controllers/device-profile-management.md#activate-device-through-profile)
* [Profile to Activate Device](../../doc/controllers/device-profile-management.md#profile-to-activate-device)
* [Profile to Deactivate Device](../../doc/controllers/device-profile-management.md#profile-to-deactivate-device)
* [Profile to Set Fallback Attribute](../../doc/controllers/device-profile-management.md#profile-to-set-fallback-attribute)


# Activate Device Through Profile

Uses the profile to bring the device under management.

```python
def activate_device_through_profile(self,
                                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ActivateDeviceProfileRequest`](../../doc/models/activate-device-profile-request.md) | Body, Required | Device Profile Query |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
body = ActivateDeviceProfileRequest(
    devices=[
        DeviceList(
            device_ids=[
                DeviceId1(
                    id='32-digit EID',
                    kind=KindEnum.EID
                ),
                DeviceId1(
                    id='15-digit IMEI',
                    kind=KindEnum.IMEI
                )
            ]
        )
    ],
    account_name='0000123456-00001',
    service_plan='The service plan name',
    mdn_zip_code='five digit zip code'
)

result = device_profile_management_controller.activate_device_through_profile(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Profile to Activate Device

Uses the profile to activate the device.

```python
def profile_to_activate_device(self,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ProfileRequest`](../../doc/models/profile-request.md) | Body, Required | Device Profile Query |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
body = ProfileRequest(
    carrier_name='the name of the mobile service provider',
    account_name='0000123456-00001',
    service_plan='The service plan name',
    mdn_zip_code='five digit zip code'
)

result = device_profile_management_controller.profile_to_activate_device(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Profile to Deactivate Device

Uses the profile to deactivate the device.

```python
def profile_to_deactivate_device(self,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ProfileRequest2`](../../doc/models/profile-request-2.md) | Body, Required | Device Profile Query |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
body = ProfileRequest2(
    account_name='0000123456-00001',
    carrier_name='the name of the mobile service provider',
    reason_code='a short code for the reason action was taken',
    etf_waiver=True,
    check_fallback_profile=False
)

result = device_profile_management_controller.profile_to_deactivate_device(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Profile to Set Fallback Attribute

Allows the profile to set the fallback attribute to the device.

```python
def profile_to_set_fallback_attribute(self,
                                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SetFallbackAttributeRequest`](../../doc/models/set-fallback-attribute-request.md) | Body, Required | Device Profile Query |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
body = SetFallbackAttributeRequest(
    account_name='0000123456-00001',
    carrier_name='the name of the mobile service provider'
)

result = device_profile_management_controller.profile_to_set_fallback_attribute(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |

