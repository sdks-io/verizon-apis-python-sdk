
# Connection Event

Network connection events for a device during a specified time period.

## Structure

`ConnectionEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `connection_event_attributes` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | The attributes that describe the connection event. |
| `extended_attributes` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | Currently not used. |
| `occurred_at` | `str` | Optional | The date and time when the connection event occured. |

## Example (as JSON)

```json
{
  "connectionEventAttributes": [
    {
      "key": "BytesUsed",
      "value": "0"
    },
    {
      "key": "Event",
      "value": "Start"
    }
  ],
  "extendedAttributes": [],
  "occurredAt": "2015-12-17T14:12:36-05:00"
}
```

