
# Aggregated Report Callback Result

Aggregated usage report (Asynchronous).

## Structure

`AggregatedReportCallbackResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `txid` | `str` | Required | A unique string that associates the request with the location report information that is sent in asynchronous callback message.ThingSpace will send a separate callback message for each device that was in the request. All of the callback messages will have the same txid. |
| `status` | [`AggregatedReportCallbackStatusEnum`](../../doc/models/aggregated-report-callback-status-enum.md) | Optional | QUEUED or COMPLETED. Requests for IoT devices with cacheMode=0 (cached) have status=COMPLETED; all other requests are QUEUED. |

## Example (as JSON)

```json
{
  "txid": "60c07fff-470b-4d6d-afcc-75e6a7c238f6",
  "status": "QUEUED"
}
```

