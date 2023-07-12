
# Session Report

Session report for a device.

## Structure

`SessionReport`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sessions` | [`List of DailyUsageItem`](../../doc/models/daily-usage-item.md) | Optional | An object containing the start and end time of the session with the amount of data transferred. |
| `id` | `string` | Required | The 10-digit ID of the device. |
| `txid` | `string` | Required | A unique string that associates the request with the location report information that is sent in asynchronous callback message.ThingSpace will send a separate callback message for each device that was in the request. All of the callback messages will have the same txid. |
| `example` | `object` | Optional | - |

## Example (as JSON)

```json
{
  "id": "709312034493372",
  "txid": "60c07fff-470b-4d6d-afcc-75e6a7c238f6",
  "sessions": [
    {
      "startTime": "startTime8",
      "endTime": "endTime4",
      "numBytes": 84
    },
    {
      "startTime": "startTime9",
      "endTime": "endTime3",
      "numBytes": 83
    },
    {
      "startTime": "startTime0",
      "endTime": "endTime2",
      "numBytes": 82
    }
  ],
  "example": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

