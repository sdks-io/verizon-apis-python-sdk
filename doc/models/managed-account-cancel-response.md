
# Managed Account Cancel Response

## Structure

`ManagedAccountCancelResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `txid` | `str` | Required | Transaction identifier |
| `account_name` | `str` | Required | Managed account identifier |
| `paccount_name` | `str` | Required | Primary account identifier |
| `service_name` | [`ServiceNameEnum`](../../doc/models/service-name-enum.md) | Required | Service name<br>**Default**: `'Location'` |
| `status` | `str` | Required | Deactivate/cancel status, Success or Fail |
| `reason` | `str` | Required | Detailed reason |

## Example (as JSON)

```json
{
  "txid": "4fbff332-ece4-42ef-9f02-7e3bdc90bd28",
  "accountName": "1223334444-00001",
  "paccountName": "1223334444-00001",
  "serviceName": "Location",
  "status": "Success",
  "reason": "Success"
}
```

