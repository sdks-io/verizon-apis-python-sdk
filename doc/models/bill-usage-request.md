
# Bill Usage Request

Bill usage request.

## Structure

`BillUsageRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account identifier. |
| `start_date` | `str` | Required | Start date to search for billable usage, mm-dd-yyyy. |
| `end_date` | `str` | Required | End date to search for billable usage, mm-dd-yyyy. |
| `usage_for_all_accounts` | `bool` | Optional | Request usage for single or multiple accounts. |

## Example (as JSON)

```json
{
  "accountName": "1234567890-00001",
  "startDate": "04-01-2018",
  "endDate": "04-30-2018",
  "usageForAllAccounts": true
}
```

