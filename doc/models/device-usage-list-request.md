
# Device Usage List Request

Request to return the daily network data usage of a single device during a specified time period.

## Structure

`DeviceUsageListRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `earliest` | `str` | Required | The earliest date for which you want usage data. |
| `latest` | `str` | Required | The last date for which you want usage data. |
| `device_id` | [`DeviceId`](../../doc/models/device-id.md) | Optional | An identifier for a single device. |
| `label` | [`Label`](../../doc/models/label.md) | Optional | - |

## Example (as JSON)

```json
{
  "earliest": "2018-03-20T00:00:01Z",
  "latest": "2020-12-31T00:00:01Z",
  "deviceId": {
    "id": "id0",
    "kind": "kind8"
  },
  "label": {
    "name": "name0",
    "value": "value2"
  }
}
```

