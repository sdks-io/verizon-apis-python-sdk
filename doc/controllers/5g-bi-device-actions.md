# 5G BI Device Actions

```python
m_5g_bi_device_actions_controller = client.m_5g_bi_device_actions
```

## Class Name

`M5gBIDeviceActionsController`

## Methods

* [Business Internetlist Device Information](../../doc/controllers/5g-bi-device-actions.md#business-internetlist-device-information)
* [Business Internetactivate Using POST](../../doc/controllers/5g-bi-device-actions.md#business-internetactivate-using-post)
* [Business Internet Serviceplanchange](../../doc/controllers/5g-bi-device-actions.md#business-internet-serviceplanchange)


# Business Internetlist Device Information

Uses the decive's Integrated Circuit Card Identification Number (ICCID) to retrive and display the device's properties.

```python
def business_internetlist_device_information(self,
                                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`M5gBideviceId`](../../doc/models/5g-bidevice-id.md) | Body, Required | Device Profile Query |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`M5gBideviceDetailsresponse`](../../doc/models/5g-bidevice-detailsresponse.md).

## Example Usage

```python
body = M5gBideviceId(
    device_id=M5gBideviceId1(
        id='20-digit ICCID',
        kind='iccid'
    )
)

result = m_5g_bi_device_actions_controller.business_internetlist_device_information(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`M5gBiRestErrorResponseException`](../../doc/models/5g-bi-rest-error-response-exception.md) |


# Business Internetactivate Using POST

Uses the device's ICCID and IMEI to activate service.

```python
def business_internetactivate_using_post(self,
                                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`M5gBiactivateRequest`](../../doc/models/5g-biactivate-request.md) | Body, Required | Activate 5G BI service. Defining <code>publicIpRestriction</code> as "Unrestricted" or "Restricted" is required for activating as Public Static. Leave  <code>publicIpRestriction</code> undefined to activate as Public Dynamic. Removing <code>publicIpRestriction</code> from the request will activate as Mobile Private Network (MPN). |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`M5gBiRequestResponse`](../../doc/models/5g-bi-request-response.md).

## Example Usage

```python
body = M5gBiactivateRequest(
    account_name='0000123456-00001',
    service_plan='service plan name',
    device_list_with_service_address=[
        DeviceListWithServiceAddress1(
            device_id=[
                M5gBideviceId1(
                    id='15-digit IMEI',
                    kind='imei'
                ),
                M5gBideviceId1(
                    id='20-digit ICCID',
                    kind='iccid'
                )
            ]
        ),
        DeviceListWithServiceAddress1(
            primary_placeofuse=M5gBiprimaryPlaceofuse(
                address=M5gBiAddress(
                    address_line_1='street number and name',
                    city='city of address',
                    state='2-letter state ID (conforms to ISO 3166-2)',
                    zip='5-digit ZIP code',
                    zip_4='the +4 digits used for ZIP codes',
                    phone='a 10-digit phone number',
                    phone_type='W'
                ),
                customer_name=M5gBiCustomerName(
                    first_name='First name',
                    last_name='Surname or Last Name',
                    middle_name='middle name or initial',
                    title='Mr. or Ms.',
                    suffex='Dr or Esq'
                )
            )
        )
    ],
    public_ip_restriction='Unrestricted',
    carrier_name='Verizon Wireless',
    mdn_zip_code='the 5-digit ZIP code of the Mobile Directory Number (MDN)'
)

result = m_5g_bi_device_actions_controller.business_internetactivate_using_post(body)
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
| Default | Error response | [`M5gBiRestErrorResponseException`](../../doc/models/5g-bi-rest-error-response-exception.md) |


# Business Internet Serviceplanchange

Change a device's service plan to use 5G BI.

```python
def business_internet_serviceplanchange(self,
                                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`M5gBichangeRequest`](../../doc/models/5g-bichange-request.md) | Body, Required | This endpoint is for use when changing a device's service plan to a 5G BI service plan. The service plan can change for an active device up to four times per month but will require address validation for each change. The service plan cannot be changed for a device while its service is suspended. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`M5gBiRequestResponse`](../../doc/models/5g-bi-request-response.md).

## Example Usage

```python
body = M5gBichangeRequest(
    account_name='0000123456-00001',
    service_plan='5G BI service plan name being changed to',
    device_list_with_service_address=[
        DeviceListWithServiceAddress(
            device_id=[
                M5gBideviceId1(
                    id='15-digit IMEI',
                    kind='imei'
                )
            ]
        ),
        DeviceListWithServiceAddress(
            primary_placeofuse=M5gBiaddressAndcustomerinfo()
        )
    ],
    current_service_plan='Name of the plan being changed from'
)

result = m_5g_bi_device_actions_controller.business_internet_serviceplanchange(body)
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
| Default | Error response | [`M5gBiRestErrorResponseException`](../../doc/models/5g-bi-rest-error-response-exception.md) |

