
# Synchronous Location Request Result

## Structure

`SynchronousLocationRequestResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `txid` | `str` | Required | The transaction ID of the report. |
| `status` | [`ReportStatusEnum`](../../doc/models/report-status-enum.md) | Required | Status of the report. |

## Example (as JSON)

```json
{
  "txid": "4be7c858-0ef9-4b15-a0c1-95061456d835",
  "status": "QUEUED"
}
```

