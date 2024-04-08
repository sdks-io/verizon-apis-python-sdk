
# Sms Messages Response

## Structure

`SmsMessagesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `messages` | [`List[GIOSmsMessage]`](../../doc/models/gio-sms-message.md) | Optional | **Constraints**: *Maximum Items*: `5` |
| `has_more_data` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "hasMoreData": false,
  "messages": [
    {
      "deviceIds": [
        {
          "kind": "kind8",
          "id": "id0"
        },
        {
          "kind": "kind8",
          "id": "id0"
        }
      ],
      "message": "message8",
      "timestamp": "2016-03-13T12:52:32.123Z"
    },
    {
      "deviceIds": [
        {
          "kind": "kind8",
          "id": "id0"
        },
        {
          "kind": "kind8",
          "id": "id0"
        }
      ],
      "message": "message8",
      "timestamp": "2016-03-13T12:52:32.123Z"
    }
  ]
}
```

