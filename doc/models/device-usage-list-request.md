
# Device Usage List Request

Request to return the daily network data usage of a single device during a specified time period.

## Structure

`DeviceUsageListRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | [`DeviceId`](../../doc/models/device-id.md) | Optional | An identifier for a single device. |
| `earliest` | `string` | Optional | The earliest date for which you want usage data. |
| `latest` | `string` | Optional | The last date for which you want usage data. |

## Example (as JSON)

```json
{
  "earliest": "2018-03-20T00:00:01Z",
  "latest": "2020-12-31T00:00:01Z",
  "deviceId": {
    "id": "id0",
    "kind": "kind8"
  }
}
```

