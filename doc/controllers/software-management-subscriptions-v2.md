# Software Management Subscriptions V2

```python
software_management_subscriptions_v2_controller = client.software_management_subscriptions_v2
```

## Class Name

`SoftwareManagementSubscriptionsV2Controller`


# Get Account Subscription Status

This endpoint retrieves a FOTA subscription by account.

```python
def get_account_subscription_status(self,
                                   account)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`FotaV2Subscription`](../../doc/models/fota-v2-subscription.md).

## Example Usage

```python
account = '0000123456-00001'

result = software_management_subscriptions_v2_controller.get_account_subscription_status(account)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "00000000000-123345",
  "purchaseType": "TS-HFOTA-EVNT,TS-HFOTA-MRC",
  "licenseCount": 500,
  "licenseUsedCount": 400,
  "updateTime": "2020-09-17T21:11:32.170Z"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |

