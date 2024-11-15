
# Response to Usage Query

## Structure

`ResponseToUsageQuery`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hasmoredata` | `bool` | Optional | - |
| `device_id` | [`ReadySimDeviceId`](../../doc/models/ready-sim-device-id.md) | Optional | - |
| `usage_history` | [`List[UsageHistory]`](../../doc/models/usage-history.md) | Optional | - |

## Example (as JSON)

```json
{
  "hasmoredata": false,
  "deviceId": {
    "kind": "kind8",
    "id": "id0"
  },
  "usageHistory": [
    {
      "bytesUsed": 76,
      "serviceplan": "serviceplan2",
      "smsUsed": 176,
      "moSMS": 230,
      "mtSMS": 18
    },
    {
      "bytesUsed": 76,
      "serviceplan": "serviceplan2",
      "smsUsed": 176,
      "moSMS": 230,
      "mtSMS": 18
    }
  ]
}
```

