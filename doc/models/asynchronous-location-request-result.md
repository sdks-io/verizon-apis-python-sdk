
# Asynchronous Location Request Result

## Structure

`AsynchronousLocationRequestResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `txid` | `str` | Optional | The transaction ID of the report. |
| `status` | [`ReportStatusEnum`](../../doc/models/report-status-enum.md) | Optional | Status of the report. |
| `estimated_duration` | `str` | Optional | Estimated number of minutes required to complete the report. |

## Example (as JSON)

```json
{
  "txid": "2017-12-11Te8b47da2-3a45-46cf-9903-61815e1e97e9",
  "status": "COMPLETED",
  "estimatedDuration": "estimatedDuration2"
}
```

