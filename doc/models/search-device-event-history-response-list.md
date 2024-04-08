
# Search Device Event History Response List

A success response includes an array of all matching events.

## Structure

`SearchDeviceEventHistoryResponseList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `search_device_event_history` | [`List[SearchDeviceResponse]`](../../doc/models/search-device-response.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example (as JSON)

```json
{
  "SearchDeviceEventHistory": [
    {
      "action": "action4",
      "createdon": "createdon4",
      "deviceid": "deviceid8",
      "fields": {
        "temperature": "temperature0"
      },
      "id": "id8"
    }
  ]
}
```

