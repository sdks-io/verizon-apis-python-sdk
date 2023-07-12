
# Managed Account Cancel Response

## Structure

`ManagedAccountCancelResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `txid` | `string` | Required | Transaction identifier |
| `account_name` | `string` | Required | Managed account identifier |
| `paccount_name` | `string` | Required | Primary account identifier |
| `service_name` | [`ServiceNameEnum`](../../doc/models/service-name-enum.md) | Required | Service name<br>**Default**: `'Location'` |
| `status` | `string` | Required | Deactivate/cancel status, Success or Fail |
| `reason` | `string` | Required | Detailed reason |

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

