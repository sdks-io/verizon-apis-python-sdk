# Software Management Subscriptions V1

```python
software_management_subscriptions_v1_controller = client.software_management_subscriptions_v1
```

## Class Name

`SoftwareManagementSubscriptionsV1Controller`

## Methods

* [Get Account Subscription Status](../../doc/controllers/software-management-subscriptions-v1.md#get-account-subscription-status)
* [Get Account License Status](../../doc/controllers/software-management-subscriptions-v1.md#get-account-license-status)


# Get Account Subscription Status

This subscriptions endpoint retrieves an account's current Software Management Service subscription status.

```python
def get_account_subscription_status(self,
                                   account)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier in "##########-#####". |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`V1AccountSubscription`](../../doc/models/v1-account-subscription.md).

## Example Usage

```python
account = '0402196254-00001'

result = software_management_subscriptions_v1_controller.get_account_subscription_status(account)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0402196254-00001",
  "purchaseType": "TS-HFOTA-EVNT,TS-HFOTA-MRC",
  "licenseCount": 9000,
  "licenseUsedCount": 1000,
  "updateTime": "2018-03-02T16:03:06.000Z"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV1ResultException`](../../doc/models/fota-v1-result-exception.md) |


# Get Account License Status

Returns information about an account's Software Management Services licenses and a list of licensed devices.

```python
def get_account_license_status(self,
                              account,
                              start_index)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier in "##########-#####". |
| `start_index` | `str` | Template, Required | The zero-based number of the first record to return. Set startIndex=0 for the first request. If there are more than 1,000 devices in the response, set startIndex=1000 for the second request, 2000 for the third request, etc. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`AccountLicenseInfo`](../../doc/models/account-license-info.md).

## Example Usage

```python
account = '0402196254-00001'

start_index = '0'

result = software_management_subscriptions_v1_controller.get_account_license_status(
    account,
    start_index
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0402196254-00001",
  "totalLicenses": 5000,
  "assignedLicenses": 4319,
  "hasMoreData": true,
  "lastSeenDeviceId": 1000,
  "deviceList": [
    {
      "deviceId": "990003425730535",
      "assignmentTime": "2017-11-29T16:03:42.000Z"
    },
    {
      "deviceId": "990000473475989",
      "assignmentTime": "2017-11-29T16:03:42.000Z"
    },
    {
      "deviceId": "990000347475989",
      "assignmentTime": "2017-11-29T16:03:42.000Z"
    },
    {
      "deviceId": "990007303425535",
      "assignmentTime": "2016-11-29T15:03:36.000Z"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV1ResultException`](../../doc/models/fota-v1-result-exception.md) |

