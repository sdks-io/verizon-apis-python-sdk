# Diagnostics Subscriptions

```python
diagnostics_subscriptions_controller = client.diagnostics_subscriptions
```

## Class Name

`DiagnosticsSubscriptionsController`


# Get Diagnostics Subscription

This endpoint retrieves a diagnostics subscription by account.

```python
def get_diagnostics_subscription(self,
                                account_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Query, Required | Account identifier. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DiagnosticsSubscription`](../../doc/models/diagnostics-subscription.md).

## Example Usage

```python
account_name = '0000123456-00001'

result = diagnostics_subscriptions_controller.get_diagnostics_subscription(account_name)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "TestQAAccount",
  "skuName": "TS-BUNDLE-KTO-DIAGNOSTIC-MRC",
  "totalAllowed": 100,
  "totalUsed": 50,
  "createdOn": "2019-08-29T00:47:59.240Z",
  "lastUpdated": "2019-08-29T00:47:59.240Z"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response. | [`DeviceDiagnosticsResultException`](../../doc/models/device-diagnostics-result-exception.md) |

