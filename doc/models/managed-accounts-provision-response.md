
# Managed Accounts Provision Response

## Structure

`ManagedAccountsProvisionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `txid` | `str` | Optional | Transaction identifier |
| `account_name` | `str` | Optional | Account identifier |
| `paccount_name` | `str` | Optional | Primary Account identifier |
| `service_name` | [`ServiceNameEnum`](../../doc/models/service-name-enum.md) | Optional | Service name<br>**Default**: `'Location'` |
| `status` | `str` | Optional | Provision status. Success or Fail |
| `reason` | `str` | Optional | Detailed reason |

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

