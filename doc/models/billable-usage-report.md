
# Billable Usage Report

Bill usage report.

## Structure

`BillableUsageReport`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Account identifier. |
| `usage_for_all_accounts` | `bool` | Optional | The usage is for a single or multiple accounts. |
| `sku_name` | `str` | Optional | SKU Name of the service subscription. |
| `transactions_allowed` | `str` | Optional | The number of location requests included with the subscription type. |
| `total_transaction_count` | `str` | Optional | The total number of billable device location requests during the reporting period from all included accounts. |
| `primary_account` | [`ServiceUsage`](../../doc/models/service-usage.md) | Optional | - |
| `managed_accounts` | [`List[ServiceUsage]`](../../doc/models/service-usage.md) | Optional | Zero or more managed accounts. |

## Example (as JSON)

```json
{
  "accountName": "1223334444-00001",
  "usageForAllAccounts": false,
  "skuName": "TS-LOC-COARSE-CellID-Aggr",
  "transactionsAllowed": "5000",
  "totalTransactionCount": "350",
  "PrimaryAccount": {
    "accountName": "1223334444-00001",
    "transactionsCount": "125"
  },
  "ManagedAccounts": []
}
```

