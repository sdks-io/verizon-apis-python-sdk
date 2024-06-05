
# Request Body for Usage 1

## Structure

`RequestBodyForUsage1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | [`List[ReadySimDeviceId]`](../../doc/models/ready-sim-device-id.md) | Optional | - |
| `start_time` | `datetime` | Optional | - |
| `end_time` | `datetime` | Optional | - |

## Example (as JSON)

```json
{
  "startTime": "08/15/2021 00:00:00",
  "endTime": "08/16/2021 00:00:00",
  "deviceId": [
    {
      "kind": "kind8",
      "id": "id0"
    },
    {
      "kind": "kind8",
      "id": "id0"
    }
  ]
}
```

