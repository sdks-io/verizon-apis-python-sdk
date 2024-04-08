
# Usage History

## Structure

`UsageHistory`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bytes_used` | `int` | Optional | - |
| `serviceplan` | `str` | Optional | - |
| `sms_used` | `int` | Optional | - |
| `mo_sms` | `int` | Optional | - |
| `mt_sms` | `int` | Optional | - |
| `source` | `str` | Optional | - |
| `event_date_time` | `datetime` | Optional | - |

## Example (as JSON)

```json
{
  "bytesUsed": 3072,
  "serviceplan": "The serviceplan name",
  "source": "Raw Usage",
  "eventDateTime": "08/15/2021 00:00:00",
  "smsUsed": 250,
  "moSMS": 100,
  "mtSMS": 92
}
```

