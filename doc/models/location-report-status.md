
# Location Report Status

Status of the report.

## Structure

`LocationReportStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `txid` | `str` | Optional | The transaction ID of the report. |
| `status` | [`ReportStatusEnum`](../../doc/models/report-status-enum.md) | Optional | Status of the report. |

## Example (as JSON)

```json
{
  "txid": "2c90bd28-ece4-42ef-9f02-7e3bd4fbff33",
  "status": "QUEUED"
}
```

