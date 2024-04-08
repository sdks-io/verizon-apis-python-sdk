# Software Management Subscriptions V3

```python
software_management_subscriptions_v3_controller = client.software_management_subscriptions_v3
```

## Class Name

`SoftwareManagementSubscriptionsV3Controller`


# Get Account Subscription Status

This endpoint retrieves a FOTA subscription by account.

```python
def get_account_subscription_status(self,
                                   acc)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `str` | Template, Required | Account identifier. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`FotaV3Subscription`](../../doc/models/fota-v3-subscription.md).

## Example Usage

```python
acc = '0000123456-00001'

result = software_management_subscriptions_v3_controller.get_account_subscription_status(acc)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0000123456-000001",
  "purchaseType": "TS-HFOTA-EVNT,TS-HFOTA-MRC",
  "licenseCount": 500,
  "licenseUsedCount": 400,
  "updateTime": "2020-09-17T21:11:32.170Z"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV3ResultException`](../../doc/models/fota-v3-result-exception.md) |

