
# SMS Event History Request

## Structure

`SMSEventHistoryRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | [`GIODeviceId`](../../doc/models/gio-device-id.md) | Required | - |
| `earliest` | `datetime` | Optional | - |
| `latest` | `datetime` | Optional | - |

## Example (as JSON)

```json
{
  "deviceId": {
    "kind": "eid",
    "id": "12345678901234567890123456789012"
  },
  "earliest": "2016-03-13T12:52:32.123Z",
  "latest": "2016-03-13T12:52:32.123Z"
}
```

