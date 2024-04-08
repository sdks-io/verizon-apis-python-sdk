
# Device Usage List Result

Response to return the daily network data usage of a single device during a specified time period.

## Structure

`DeviceUsageListResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_more_data` | `bool` | Optional | False for a status 200 response.True for a status 202 response, indicating that there is more data to be retrieved. |
| `usage_history` | [`List[Usage]`](../../doc/models/usage.md) | Optional | Placeholder. |

## Example (as JSON)

```json
{
  "hasMoreData": false,
  "usageHistory": [
    {
      "bytesUsed": 4096,
      "extendedAttributes": [
        {
          "key": "MoSms",
          "value": "0"
        }
      ],
      "smsUsed": 0,
      "source": "Raw Usage",
      "timestamp": "2020-12-01T00:00:00Z",
      "servicePlan": "servicePlan0"
    }
  ]
}
```

