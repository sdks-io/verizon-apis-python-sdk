
# GIO Sms Message

## Structure

`GIOSmsMessage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | [`List[GIODeviceId]`](../../doc/models/gio-device-id.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `message` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `120`, *Pattern*: `^[A-Za-z0-9 ]{3,120}$` |
| `timestamp` | `datetime` | Optional | - |

## Example (as JSON)

```json
{
  "message": "a text message",
  "deviceIds": [
    {
      "kind": "kind8",
      "id": "id0"
    }
  ],
  "timestamp": "2016-03-13T12:52:32.123Z"
}
```

