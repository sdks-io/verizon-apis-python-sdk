# Promotion Period Information

```python
promotion_period_information_controller = client.promotion_period_information
```

## Class Name

`PromotionPeriodInformationController`

## Methods

* [Get Promo Device Usage History](../../doc/controllers/promotion-period-information.md#get-promo-device-usage-history)
* [Get Promo Device Aggregate Usage History](../../doc/controllers/promotion-period-information.md#get-promo-device-aggregate-usage-history)


# Get Promo Device Usage History

Retrieves the usage history of a device during the promotion period.

```python
def get_promo_device_usage_history(self,
                                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`RequestBodyForUsage`](../../doc/models/request-body-for-usage.md) | Body, Required | Retrieve Aggregate Usage |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ResponseToUsageQuery`](../../doc/models/response-to-usage-query.md).

## Example Usage

```python
body = RequestBodyForUsage(
    start_time=dateutil.parser.parse('08/15/2021 00:00:00'),
    end_time=dateutil.parser.parse('08/16/2021 00:00:00')
)

result = promotion_period_information_controller.get_promo_device_usage_history(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "hasmoredata": false,
  "deviceId": {
    "kind": "iccid",
    "id": "20-digit iccid"
  },
  "usageHistory": [
    {
      "bytesUsed": 3072,
      "serviceplan": "The serviceplan name",
      "smsUsed": 0,
      "moSMS": 0,
      "mtSMS": 0,
      "source": "Raw Usage",
      "eventDateTime": "2021-08-15T00:00:00Z"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | All error responses will be in this format | [`ReadySimRestErrorResponseException`](../../doc/models/ready-sim-rest-error-response-exception.md) |


# Get Promo Device Aggregate Usage History

Retrieves the aggregate usage for an account using pseudo-MDN during the promotional period using a callback.

```python
def get_promo_device_aggregate_usage_history(self,
                                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`UsageRequestBody`](../../doc/models/usage-request-body.md) | Body, Required | Retrieve Aggregate Usage |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`UsageRequestResponse`](../../doc/models/usage-request-response.md).

## Example Usage

```python
body = UsageRequestBody(
    account_id='0000123456-000001',
    start_time=dateutil.parser.parse('08/15/2021 00:00:00'),
    end_time=dateutil.parser.parse('08/16/2021 00:00:00')
)

result = promotion_period_information_controller.get_promo_device_aggregate_usage_history(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "be1b5958-3e11-41db-9abd-b1b7618c0035"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`ReadySimRestErrorResponseException`](../../doc/models/ready-sim-rest-error-response-exception.md) |

