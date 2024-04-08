# Devices Location Subscriptions

```python
devices_location_subscriptions_controller = client.devices_location_subscriptions
```

## Class Name

`DevicesLocationSubscriptionsController`

## Methods

* [Get Location Service Subscription Status](../../doc/controllers/devices-location-subscriptions.md#get-location-service-subscription-status)
* [Get Location Service Usage](../../doc/controllers/devices-location-subscriptions.md#get-location-service-usage)


# Get Location Service Subscription Status

This subscriptions endpoint retrieves an account's current location subscription status.

```python
def get_location_service_subscription_status(self,
                                            account)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Template, Required | Account identifier in "##########-#####". |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceLocationSubscription`](../../doc/models/device-location-subscription.md).

## Example Usage

```python
account = '0000123456-00001'

result = devices_location_subscriptions_controller.get_location_service_subscription_status(account)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "2024009649-00001",
  "locType": "TS-LOC-COARSE-CellID-5K",
  "maxAllowance": "5000",
  "purchaseTime": "2017-05-10 06:25:25.171 +0000 UTC"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |


# Get Location Service Usage

This endpoint allows user to search for billable usage for accounts based on the provided date range.

```python
def get_location_service_usage(self,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BillUsageRequest`](../../doc/models/bill-usage-request.md) | Body, Required | Request to obtain billable usage for accounts. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type `object`.

## Example Usage

```python
body = BillUsageRequest(
    account_name='1234567890-00001',
    start_date='04-01-2018',
    end_date='04-30-2018',
    usage_for_all_accounts=True
)

result = devices_location_subscriptions_controller.get_location_service_usage(body)
print(result)
```

## Example Response

```
{
  "accountName": "1223334444-00001",
  "usageForAllAcounts": false,
  "skuName": "TS-LOC-COARSE-CellID-Aggr",
  "transactionsAllowed": "5000",
  "totalTransactionCount": "350",
  "PrimaryAccount": {
    "accountName": "1223334444-00001",
    "transactionsCount": "125"
  },
  "ManagedAccounts": []
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |

