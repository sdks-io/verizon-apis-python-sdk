# Fixed Wireless Qualification

```python
fixed_wireless_qualification_controller = client.fixed_wireless_qualification
```

## Class Name

`FixedWirelessQualificationController`


# Domestic 4 G and 5G Fixed Wireless Qualification

Use this query for Fixed Wireless Qualification of an address. Network types include: LTE, C-BAND and MMWAVE.

```python
def domestic_4_g_and_5g_fixed_wireless_qualification(self,
                                                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetWirelessCoverageRequestFWA`](../../doc/models/get-wireless-coverage-request-fwa.md) | Body, Required | Request for network coverage details. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`WNPRequestResponse`](../../doc/models/wnp-request-response.md).

## Example Usage

```python
body = GetWirelessCoverageRequestFWA(
    account_name='0000123456-00001',
    request_type='FWA',
    location_type='ADDRESS',
    locations=Locations(
        address_list=[
            AddressItem(
                address_line_1='street address',
                city='city',
                state='LA',
                country='USA',
                zip='00000'
            )
        ]
    ),
    network_types_list=[
        NetworkType(
            network_type='LTE'
        )
    ]
)

result = fixed_wireless_qualification_controller.domestic_4_g_and_5g_fixed_wireless_qualification(body)
print(result)
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
| Default | Error response | [`WNPRestErrorResponseException`](../../doc/models/wnp-rest-error-response-exception.md) |

