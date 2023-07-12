
# Search Sensor History Response List

A success response includes an array of all matching events.

## Structure

`SearchSensorHistoryResponseList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `search_sensor_history` | [`List of SearchDeviceResponse`](../../doc/models/search-device-response.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example (as JSON)

```json
{
  "SearchSensorHistory": [
    {
      "action": "action4",
      "createdon": "createdon4",
      "deviceid": "deviceid2",
      "fields": {
        "temperature": "temperature8"
      },
      "id": "id8"
    },
    {
      "action": "action3",
      "createdon": "createdon3",
      "deviceid": "deviceid1",
      "fields": {
        "temperature": "temperature9"
      },
      "id": "id9"
    }
  ]
}
```

