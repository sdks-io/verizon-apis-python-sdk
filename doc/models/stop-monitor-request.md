
# Stop Monitor Request

## Structure

`StopMonitorRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | - |
| `monitor_ids` | `List[str]` | Required | - |

## Example (as JSON)

```json
{
  "accountName": "0242123520-00001",
  "monitorIds": [
    "35596ca6-bab4-4333-a914-42b4fc2da54c",
    "35596ca6-bab4-4333-a914-42b4fc2da54b"
  ]
}
```

