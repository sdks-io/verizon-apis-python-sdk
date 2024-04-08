# Device Management

```python
device_management_controller = client.device_management
```

## Class Name

`DeviceManagementController`

## Methods

* [Activate Service for Devices](../../doc/controllers/device-management.md#activate-service-for-devices)
* [Add Devices](../../doc/controllers/device-management.md#add-devices)
* [Update Devices Contact Information](../../doc/controllers/device-management.md#update-devices-contact-information)
* [Update Devices Custom Fields](../../doc/controllers/device-management.md#update-devices-custom-fields)
* [Deactivate Service for Devices](../../doc/controllers/device-management.md#deactivate-service-for-devices)
* [Delete Deactivated Devices](../../doc/controllers/device-management.md#delete-deactivated-devices)
* [List Devices Information](../../doc/controllers/device-management.md#list-devices-information)
* [List Devices With Imei Iccid Mismatch](../../doc/controllers/device-management.md#list-devices-with-imei-iccid-mismatch)
* [Move Devices Within Accounts of Profile](../../doc/controllers/device-management.md#move-devices-within-accounts-of-profile)
* [Update Devices State](../../doc/controllers/device-management.md#update-devices-state)
* [Change Devices Service Plan](../../doc/controllers/device-management.md#change-devices-service-plan)
* [Suspend Service for Devices](../../doc/controllers/device-management.md#suspend-service-for-devices)
* [Restore Service for Suspended Devices](../../doc/controllers/device-management.md#restore-service-for-suspended-devices)
* [Check Devices Availability for Activation](../../doc/controllers/device-management.md#check-devices-availability-for-activation)
* [Retrieve Device Connection History](../../doc/controllers/device-management.md#retrieve-device-connection-history)
* [Update Devices Cost Center Code](../../doc/controllers/device-management.md#update-devices-cost-center-code)
* [Get Device Extended Diagnostic Information](../../doc/controllers/device-management.md#get-device-extended-diagnostic-information)
* [List Devices Provisioning History](../../doc/controllers/device-management.md#list-devices-provisioning-history)
* [List Current Devices PRL Version](../../doc/controllers/device-management.md#list-current-devices-prl-version)
* [Get Device Service Suspension Status](../../doc/controllers/device-management.md#get-device-service-suspension-status)
* [List Devices Usage History](../../doc/controllers/device-management.md#list-devices-usage-history)
* [Retrieve Aggregate Device Usage History](../../doc/controllers/device-management.md#retrieve-aggregate-device-usage-history)
* [Update Device Id](../../doc/controllers/device-management.md#update-device-id)
* [Device Upload](../../doc/controllers/device-management.md#device-upload)
* [Billed Usage Info](../../doc/controllers/device-management.md#billed-usage-info)
* [Usage Segmentation Label Association](../../doc/controllers/device-management.md#usage-segmentation-label-association)
* [Usage Segmentation Label Deletion](../../doc/controllers/device-management.md#usage-segmentation-label-deletion)
* [Activation Order Status](../../doc/controllers/device-management.md#activation-order-status)
* [Upload Device Identifier](../../doc/controllers/device-management.md#upload-device-identifier)


# Activate Service for Devices

If the devices do not already exist in the account, this API resource adds them before activation.

```python
def activate_service_for_devices(self,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CarrierActivateRequest`](../../doc/models/carrier-activate-request.md) | Body, Required | Request for activating a service on devices. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = CarrierActivateRequest(
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
    service_plan='m2m_4G',
    mdn_zip_code='98801',
    account_name='0868924207-00001',
    custom_fields=[
        CustomFields(
            key='CustomField2',
            value='SuperVend'
        )
    ],
    group_name='4G West',
    primary_place_of_use=PlaceOfUse(
        address=Address(
            address_line_1='1600 Pennsylvania Ave NW',
            city='Washington',
            state='DC',
            zip='20500',
            country='USA'
        ),
        customer_name=CustomerName(
            first_name='Zaffod',
            last_name='Beeblebrox',
            title='President'
        )
    )
)

result = device_management_controller.activate_service_for_devices(body)
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


# Add Devices

Use this API if you want to manage some device settings before you are ready to activate service for the devices.

```python
def add_devices(self,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AddDevicesRequest`](../../doc/models/add-devices-request.md) | Body, Required | Devices to add. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[AddDevicesResult]`](../../doc/models/add-devices-result.md).

## Example Usage

```python
body = AddDevicesRequest(
    state='preactive',
    devices_to_add=[
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
    account_name='0868924207-00001',
    custom_fields=[
        CustomFields(
            key='CustomField2',
            value='SuperVend'
        )
    ],
    group_name='West Region'
)

result = device_management_controller.add_devices(body)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "deviceIds": [
      {
        "id": "89148000000800784259",
        "kind": "iccid"
      }
    ],
    "response": "Success"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# Update Devices Contact Information

Sends a CarrierService callback message for each device in the request when the contact information has been changed, or if there was a problem and the change could not be completed.

```python
def update_devices_contact_information(self,
                                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ContactInfoUpdateRequest`](../../doc/models/contact-info-update-request.md) | Body, Required | Request to update contact information for devices. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = ContactInfoUpdateRequest(
    primary_place_of_use=PlaceOfUse(
        address=Address(
            address_line_1='9868 Scranton Rd',
            city='San Diego',
            state='CA',
            zip='92121',
            country='USA',
            address_line_2='Suite A',
            zip_4='0001',
            phone='1234567890',
            phone_type='H',
            email_address='zaffod@theinternet.com'
        ),
        customer_name=CustomerName(
            first_name='Zaffod',
            last_name='Beeblebrox',
            title='President',
            middle_name='P',
            suffix='I'
        )
    ),
    account_name='0212345678-00001',
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='19110173057',
                    kind='ESN'
                ),
                DeviceId(
                    id='19110173057',
                    kind='ESN'
                )
            ]
        )
    ]
)

result = device_management_controller.update_devices_contact_information(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "24da9f9a-d110-4a54-86b4-93fb76aab83c"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# Update Devices Custom Fields

Sends a CarrierService callback message for each device in the request when the custom fields have been changed, or if there was a problem and the change could not be completed.

```python
def update_devices_custom_fields(self,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CustomFieldsUpdateRequest`](../../doc/models/custom-fields-update-request.md) | Body, Required | Request to update custom field of devices. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = CustomFieldsUpdateRequest(
    custom_fields_to_update=[
        CustomFields(
            key='CustomField1',
            value='West Region'
        ),
        CustomFields(
            key='CustomField2',
            value='Distribution'
        )
    ],
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='89148000000800139708',
                    kind='iccid'
                )
            ]
        )
    ]
)

result = device_management_controller.update_devices_custom_fields(body)
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


# Deactivate Service for Devices

Deactivating service for a device may result in an early termination fee (ETF) being charged to the account, depending on the terms of the contract with Verizon. If your contract allows ETF waivers and if you want to use one for a particular deactivation, set the etfWaiver value to True.

```python
def deactivate_service_for_devices(self,
                                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CarrierDeactivateRequest`](../../doc/models/carrier-deactivate-request.md) | Body, Required | Request to deactivate service for one or more devices. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = CarrierDeactivateRequest(
    account_name='0000123456-00001',
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='20-digit ICCID',
                    kind='iccid'
                )
            ]
        ),
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='20-digit ICCID',
                    kind='iccid'
                )
            ]
        )
    ],
    reason_code='FF',
    etf_waiver=True
)

result = device_management_controller.deactivate_service_for_devices(body)
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


# Delete Deactivated Devices

Use this API to remove unneeded devices from an account.

```python
def delete_deactivated_devices(self,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeleteDevicesRequest`](../../doc/models/delete-devices-request.md) | Body, Required | Devices to delete. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[DeleteDevicesResult]`](../../doc/models/delete-devices-result.md).

## Example Usage

```python
body = DeleteDevicesRequest(
    devices_to_delete=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='09005470263',
                    kind='esn'
                )
            ]
        ),
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='85000022411113460014',
                    kind='iccid'
                )
            ]
        ),
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='85000022412313460016',
                    kind='iccid'
                )
            ]
        )
    ]
)

result = device_management_controller.delete_deactivated_devices(body)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "deviceIds": {
      "id": "09005470263",
      "kind": "esn"
    },
    "status": "Success"
  },
  {
    "deviceIds": {
      "id": "85000022411113460014",
      "kind": "iccid"
    },
    "status": "Success"
  },
  {
    "deviceIds": [
      {
        "id": "85000022412313460016",
        "kind": "iccid"
      },
      {
        "id": "09005470263",
        "kind": "esn"
      }
    ],
    "status": "Failed",
    "message": "The device is not in deactive state."
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# List Devices Information

Returns information about a single device or information about all devices that match the given parameters. Returned information includes device provisioning state, service plan, MDN, MIN, and IP address.

```python
def list_devices_information(self,
                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AccountDeviceListRequest`](../../doc/models/account-device-list-request.md) | Body, Required | Device information query. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`AccountDeviceListResult`](../../doc/models/account-device-list-result.md).

## Example Usage

```python
body = AccountDeviceListRequest(
    device_id=DeviceId(
        id='20-digit ICCID',
        kind='iccid'
    )
)

result = device_management_controller.list_devices_information(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "hasMoreData": false,
  "devices": [
    {
      "accountName": "0000123456-00001",
      "billingCycleEndDate": "2020-05-09T20:00:00-04:00",
      "carrierInformations": [
        {
          "carrierName": "Verizon Wireless",
          "servicePlan": "m2m4G",
          "state": "active"
        }
      ],
      "connected": false,
      "createdAt": "2019-08-07T10:42:15-04:00",
      "deviceIds": [
        {
          "id": "10-digit MDN",
          "kind": "mdn"
        },
        {
          "id": "15-digit IMEI",
          "kind": "imei"
        }
      ],
      "groupNames": [
        "southwest"
      ],
      "ipAddress": "0.0.0.0",
      "lastActivationBy": "Joe Q Public",
      "lastActivationDate": "2019-08-07T10:42:34-04:00",
      "lastConnectionDate": "2020-03-12T04:23:37-04:00"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# List Devices With Imei Iccid Mismatch

Returns a list of all 4G devices with an ICCID (SIM) that was not activated with the expected IMEI (hardware) during a specified time frame.

```python
def list_devices_with_imei_iccid_mismatch(self,
                                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceMismatchListRequest`](../../doc/models/device-mismatch-list-request.md) | Body, Required | Request to list devices with mismatched IMEIs and ICCIDs. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceMismatchListResult`](../../doc/models/device-mismatch-list-result.md).

## Example Usage

```python
body = DeviceMismatchListRequest(
    filter=DateFilter(
        earliest='2020-05-01T15:00:00-08:00Z',
        latest='2020-07-30T15:00:00-08:00Z'
    ),
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='8914800000080078',
                    kind='ICCID'
                ),
                DeviceId(
                    id='5096300587',
                    kind='MDN'
                )
            ]
        )
    ],
    account_name='0342077109-00001'
)

result = device_management_controller.list_devices_with_imei_iccid_mismatch(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "devices": [
    {
      "accountName": "0212398765-00001",
      "mdn": "5096300587",
      "activationDate": "2011-01-21T10:55:27-08:00",
      "iccid": "89148000000800784259",
      "preImei": "990003420535573",
      "postImei": "987603420573553",
      "simOtaDate": "2017-12-01T16:00:00-08:00"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# Move Devices Within Accounts of Profile

Move active devices from one billing account to another within a customer profile.

```python
def move_devices_within_accounts_of_profile(self,
                                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`MoveDeviceRequest`](../../doc/models/move-device-request.md) | Body, Required | Request to move devices between accounts. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = MoveDeviceRequest(
    account_name='0212345678-00001',
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='19110173057',
                    kind='ESN'
                )
            ]
        )
    ],
    service_plan='M2M5GB'
)

result = device_management_controller.move_devices_within_accounts_of_profile(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "ec682a8b-e288-4806-934d-24e7a59ed889"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# Update Devices State

Changes the provisioning state of one or more devices to a specified customer-defined service and state.

```python
def update_devices_state(self,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GoToStateRequest`](../../doc/models/go-to-state-request.md) | Body, Required | Request to change device state to one defined by the user. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = GoToStateRequest(
    service_name='My Service',
    state_name='My State',
    service_plan='87641',
    mdn_zip_code='94203',
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
    public_ip_restriction='unrestricted',
    group_name='4G West',
    primary_place_of_use=PlaceOfUse(
        address=Address(
            address_line_1='1600 Pennsylvania Ave NW',
            city='Washington',
            state='DC',
            zip='20500',
            country='USA'
        ),
        customer_name=CustomerName(
            first_name='Zaffod',
            last_name='Beeblebrox',
            title='President'
        )
    )
)

result = device_management_controller.update_devices_state(body)
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


# Change Devices Service Plan

Changes the service plan for one or more devices.

```python
def change_devices_service_plan(self,
                               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ServicePlanUpdateRequest`](../../doc/models/service-plan-update-request.md) | Body, Required | Request to change device service plan. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = ServicePlanUpdateRequest(
    service_plan='new_service_plan_code',
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='A100003685E561',
                    kind='meid'
                )
            ]
        )
    ]
)

result = device_management_controller.change_devices_service_plan(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "c8de7c1d-59b9-4cf3-b969-db76cb2ce509"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# Suspend Service for Devices

Suspends service for one or more devices.

```python
def suspend_service_for_devices(self,
                               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CarrierActionsRequest`](../../doc/models/carrier-actions-request.md) | Body, Required | Request to suspend service for one or more devices. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = CarrierActionsRequest(
    account_name='0000123456-00001',
    custom_fields=[
        CustomFields(
            key='customField1',
            value='key value'
        )
    ],
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='20-digit ICCID',
                    kind='iccid'
                )
            ]
        )
    ],
    with_billing=True,
    group_name='name of the group',
    service_plan='service plan name'
)

result = device_management_controller.suspend_service_for_devices(body)
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


# Restore Service for Suspended Devices

Restores service to one or more suspended devices.

```python
def restore_service_for_suspended_devices(self,
                                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CarrierActionsRequest`](../../doc/models/carrier-actions-request.md) | Body, Required | Request to restore services of one or more suspended devices. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = CarrierActionsRequest(
    account_name='0000123456-00001',
    custom_fields=[
        CustomFields(
            key='customField1',
            value='key value'
        )
    ],
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='20-digit ICCID',
                    kind='iccid'
                )
            ]
        )
    ],
    group_name='name of the group',
    service_plan='service plan name'
)

result = device_management_controller.restore_service_for_suspended_devices(body)
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


# Check Devices Availability for Activation

Checks whether specified devices are registered by the manufacturer with the Verizon network and are available to be activated.

```python
def check_devices_availability_for_activation(self,
                                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceActivationRequest`](../../doc/models/device-activation-request.md) | Body, Required | Request to check if devices can be activated or not. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = DeviceActivationRequest(
    account_name='0212345678-00001',
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='A100008385E561',
                    kind='meid'
                )
            ]
        )
    ]
)

result = device_management_controller.check_devices_availability_for_activation(body)
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


# Retrieve Device Connection History

Each response includes a maximum of 500 records. To obtain more records, you can call the API multiple times, adjusting the earliest value each time to start where the previous request finished.

```python
def retrieve_device_connection_history(self,
                                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceConnectionListRequest`](../../doc/models/device-connection-list-request.md) | Body, Required | Query to retrieve device connection history. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ConnectionHistoryResult`](../../doc/models/connection-history-result.md).

## Example Usage

```python
body = DeviceConnectionListRequest(
    device_id=DeviceId(
        id='89141390780800784259',
        kind='iccid'
    ),
    earliest='2015-09-16T00:00:01Z',
    latest='2010-09-18T00:00:01Z'
)

result = device_management_controller.retrieve_device_connection_history(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "connectionHistory": [
    {
      "connectionEventAttributes": [
        {
          "key": "BytesUsed",
          "value": "0"
        },
        {
          "key": "Event",
          "value": "Start"
        }
      ],
      "extendedAttributes": [],
      "occurredAt": "2015-12-17T14:12:36-05:00"
    },
    {
      "connectionEventAttributes": [
        {
          "key": "BytesUsed",
          "value": "419863234"
        },
        {
          "key": "Event",
          "value": "Stop"
        },
        {
          "key": "Msisdn",
          "value": "15086303371"
        }
      ],
      "extendedAttributes": [],
      "occurredAt": "2015-12-19T01:20:00-05:00"
    }
  ],
  "hasMoreData": false
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# Update Devices Cost Center Code

Changes or removes the CostCenterCode value or customer name and address (Primary Place of Use) for one or more devices.

```python
def update_devices_cost_center_code(self,
                                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceCostCenterRequest`](../../doc/models/device-cost-center-request.md) | Body, Required | Request to update cost center code value for one or more devices. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = DeviceCostCenterRequest(
    cost_center='cc12345',
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='89148000000800139708',
                    kind='iccid'
                )
            ]
        )
    ]
)

result = device_management_controller.update_devices_cost_center_code(body)
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


# Get Device Extended Diagnostic Information

Returns extended diagnostic information about a specified device, including connectivity, provisioning, billing and location status.

```python
def get_device_extended_diagnostic_information(self,
                                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceExtendedDiagnosticsRequest`](../../doc/models/device-extended-diagnostics-request.md) | Body, Required | Request to query extended diagnostics information for a device. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceExtendedDiagnosticsResult`](../../doc/models/device-extended-diagnostics-result.md).

## Example Usage

```python
body = DeviceExtendedDiagnosticsRequest(
    account_name='1223334444-00001',
    device_list=[
        DeviceId(
            id='10-digit MDN',
            kind='mdn'
        )
    ]
)

result = device_management_controller.get_device_extended_diagnostic_information(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "categories": [
    {
      "categoryName": "Connectivity",
      "extendedAttributes": [
        {
          "key": "Connected",
          "value": "false"
        }
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# List Devices Provisioning History

Returns the provisioning history of a specified device during a specified time period.

```python
def list_devices_provisioning_history(self,
                                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceProvisioningHistoryListRequest`](../../doc/models/device-provisioning-history-list-request.md) | Body, Required | Query to obtain device provisioning history. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[DeviceProvisioningHistoryListResult]`](../../doc/models/device-provisioning-history-list-result.md).

## Example Usage

```python
body = DeviceProvisioningHistoryListRequest(
    device_id=DeviceId(
        id='89141390780800784259',
        kind='iccid'
    ),
    earliest='2015-09-16T00:00:01Z',
    latest='2015-09-18T00:00:01Z'
)

result = device_management_controller.list_devices_provisioning_history(body)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "provisioningHistory": [
      {
        "occurredAt": "2015-12-17T13:56:13-05:00",
        "status": "Success",
        "eventBy": "Harry Potter",
        "eventType": "Activation Confirmed",
        "servicePlan": "Tablet5GB",
        "mdn": "",
        "msisdn": "15086303371",
        "extendedAttributes": []
      }
    ],
    "hasMoreData": false
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# List Current Devices PRL Version

4G and GSM devices do not have a PRL.

```python
def list_current_devices_prl_version(self,
                                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DevicePrlListRequest`](../../doc/models/device-prl-list-request.md) | Body, Required | Request to query device PRL. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = DevicePrlListRequest(
    account_name='101234-0001',
    group_name='West Region',
    service_plan='3G 2MB'
)

result = device_management_controller.list_current_devices_prl_version(body)
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


# Get Device Service Suspension Status

Returns DeviceSuspensionStatus callback messages containing the current device state and information on how many days a device has been suspended and can continue to be suspended.

```python
def get_device_service_suspension_status(self,
                                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceSuspensionStatusRequest`](../../doc/models/device-suspension-status-request.md) | Body, Required | Request to obtain service suspenstion status for a device. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = DeviceSuspensionStatusRequest(
    filter=DeviceFilterWithoutAccount(
        group_name='suspended devices'
    ),
    account_name='1223334444-00001'
)

result = device_management_controller.get_device_service_suspension_status(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "904dcdc6-a590-45e4-ac76-403306f6d883"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# List Devices Usage History

Returns the network data usage history of a device during a specified time period.

```python
def list_devices_usage_history(self,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceUsageListRequest`](../../doc/models/device-usage-list-request.md) | Body, Required | Request to obtain usage history for a specific device. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceUsageListResult`](../../doc/models/device-usage-list-result.md).

## Example Usage

```python
body = DeviceUsageListRequest(
    earliest='2018-03-20T00:00:01Z',
    latest='2020-12-31T00:00:01Z'
)

result = device_management_controller.list_devices_usage_history(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "hasMoreData": false,
  "usageHistory": [
    {
      "bytesUsed": 4096,
      "extendedAttributes": [
        {
          "key": "MoSms",
          "value": "0"
        }
      ],
      "smsUsed": 0,
      "source": "Raw Usage",
      "timestamp": "2020-12-01T00:00:00Z"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# Retrieve Aggregate Device Usage History

The information is returned in a callback response, so you must register a URL for DeviceUsage callback messages using the POST /callbacks API.

```python
def retrieve_aggregate_device_usage_history(self,
                                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceAggregateUsageListRequest`](../../doc/models/device-aggregate-usage-list-request.md) | Body, Required | A request to retrieve aggregated device usage history information. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = DeviceAggregateUsageListRequest(
    start_time='2021-08-01T00:00:00-06:00',
    end_time='2021-08-30T00:00:00-06:00',
    device_ids=[
        DeviceId(
            id='84258000000891490087',
            kind='ICCID'
        )
    ],
    account_name='9992330389-00001'
)

result = device_management_controller.retrieve_aggregate_device_usage_history(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "1631e200-7398-4609-b1f8-398341229176"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# Update Device Id

Changes the identifier of a 3G or 4G device to match hardware changes made for a line of service. Use this request to transfer the line of service and the MDN to new hardware, or to change the MDN.

```python
def update_device_id(self,
                    service_type,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_type` | `str` | Template, Required | Identifier type. |
| `body` | [`ChangeDeviceIdRequest`](../../doc/models/change-device-id-request.md) | Body, Required | Request to update device id. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
service_type = 'serviceType6'

body = ChangeDeviceIdRequest(
    device_ids=[
        DeviceId(
            id='42590078891480000008',
            kind='iccid'
        )
    ],
    change_4_g_option='ChangeICCID',
    device_ids_to=[
        DeviceId(
            id='89148000000842590078',
            kind='iccid'
        )
    ],
    service_plan='4G 2GB',
    zip_code='98802'
)

result = device_management_controller.update_device_id(
    service_type,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "a28892ea-6503-4aa7-bfa2-4cd45d42f61b"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# Device Upload

This corresponds to the M2M-MC SOAP interface, `DeviceUploadService`.

```python
def device_upload(self,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceUploadRequest`](../../doc/models/device-upload-request.md) | Body, Required | Device Upload Query |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`RequestResponse`](../../doc/models/request-response.md).

## Example Usage

```python
body = DeviceUploadRequest(
    account_name='1223334444-00001',
    devices=[
        DeviceList(
            device_ids=[
                DeviceId(
                    id='15-digit IMEI',
                    kind='imei'
                )
            ]
        ),
        DeviceList(
            device_ids=[
                DeviceId(
                    id='15-digit IMEI',
                    kind='imei'
                )
            ]
        )
    ],
    email_address='bob@mycompany.com',
    device_sku='VZW123456',
    upload_type='IMEI'
)

result = device_management_controller.device_upload(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Billed Usage Info

Gets billed usage for for either multiple devices or an entire billing account.

```python
def billed_usage_info(self,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BilledusageListRequest`](../../doc/models/billedusage-list-request.md) | Body, Required | Request to list devices with mismatched IMEIs and ICCIDs. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = BilledusageListRequest(
    account_name='0342077109-00001'
)

result = device_management_controller.billed_usage_info(body)
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


# Usage Segmentation Label Association

Allows you to associate your own usage segmentation label with a device.

```python
def usage_segmentation_label_association(self,
                                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AssociateLabelRequest`](../../doc/models/associate-label-request.md) | Body, Required | Request to associate a label to a device. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = AssociateLabelRequest(
    account_name='1223334444-00001',
    labels=AccountLabels(
        devices=[
            DeviceList()
        ]
    )
)

result = device_management_controller.usage_segmentation_label_association(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "ec682a8b-e288-4806-934d-24e7a59ed889"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# Usage Segmentation Label Deletion

Allow customers to remove the associated label from a device.

```python
def usage_segmentation_label_deletion(self,
                                     account_name,
                                     label_list)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Query, Required | The numeric name of the account. |
| `label_list` | [`LabelsList`](../../doc/models/labels-list.md) | Query, Required | A list of the Label IDs to remove from the exclusion list. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
account_name = '0000123456-00001'

label_list = LabelsList()

result = device_management_controller.usage_segmentation_label_deletion(
    account_name,
    label_list
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "ec682a8b-e288-4806-934d-24e7a59ed889"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# Activation Order Status

Uploads and activates device identifiers and SKUs for new devices from OEMs to Verizon.

```python
def activation_order_status(self,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`UploadsActivatesDeviceRequest`](../../doc/models/uploads-activates-device-request.md) | Body, Required | Request to Uploads and activates device. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = UploadsActivatesDeviceRequest(
    account_name='1223334444-00001',
    email_address='bob@mycompany.com',
    device_sku='VZW123456',
    upload_type='IMEI ICCID Pair',
    service_plan='15MBShr',
    mdn_zip_code='92222',
    devices=[
        DeviceList(
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
        )
    ],
    carrier_ip_pool_name=''
)

result = device_management_controller.activation_order_status(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "ec682a8b-e288-4806-934d-24e7a59ed889"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# Upload Device Identifier

Checks the status of an activation order and lists where the order is in the provisioning process.

```python
def upload_device_identifier(self,
                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CheckOrderStatusRequest`](../../doc/models/check-order-status-request.md) | Body, Required | The request body identifies the device and reporting period that you want included in the report. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = CheckOrderStatusRequest(
    account_name='4Gpublicaccount ',
    devices=[
        DeviceList(
            device_ids=[
                DeviceId(
                    id='20112019672551234613',
                    kind='iccid'
                )
            ]
        )
    ],
    order_request_id=' f55fea16-3664-4a32-ae9d-c0cbe3eedf1d '
)

result = device_management_controller.upload_device_identifier(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "c7b45cf2-cab1-4e42-82f8-20350f4c4ea3"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |

