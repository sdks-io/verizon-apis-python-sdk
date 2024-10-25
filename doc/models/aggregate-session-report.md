
# Aggregate Session Report

Session and usage details for up to 10 devices.

## Structure

`AggregateSessionReport`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `txid` | `str` | Required | A unique string that associates the request with the location report information that is sent in asynchronous callback message.ThingSpace will send a separate callback message for each device that was in the request. All of the callback messages will have the same txid. |
| `usage` | [`List[AggregateUsageItem]`](../../doc/models/aggregate-usage-item.md) | Optional | Contains usage per device.<br>**Constraints**: *Unique Items Required* |
| `errors` | [`List[AggregateUsageError]`](../../doc/models/aggregate-usage-error.md) | Optional | An object containing any errors reported by the device.<br>**Constraints**: *Unique Items Required* |

## Example (as JSON)

```json
{
  "txid": "txid8",
  "usage": [
    {
      "imei": "709312034493372",
      "numberOfSessions": 1,
      "bytesTransferred": 2057
    }
  ],
  "errors": [
    {
      "imei": "imei6",
      "errorMessage": "errorMessage8",
      "errorResponse": {
        "errorCode": "INTERNAL_ERROR",
        "errorMessage": "errorMessage4",
        "httpStatusCode": "423 LOCKED",
        "detailErrorMessage": "detailErrorMessage6"
      }
    }
  ]
}
```

