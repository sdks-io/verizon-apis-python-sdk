
# Managed Accounts Provision Request

## Structure

`ManagedAccountsProvisionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Managed account identifier |
| `paccount_name` | `str` | Required | Primary Account identifier |
| `service_name` | [`ServiceNameEnum`](../../doc/models/service-name-enum.md) | Required | Service name<br>**Default**: `'Location'` |
| `mtype` | `str` | Required | SKU name |
| `txid` | `str` | Required | Transaction identifier returned by add request |

## Example (as JSON)

```json
{
  "accountName": "1223334444-00001",
  "paccountName": "1223334444-00001",
  "serviceName": "Location",
  "type": "TS-LOC-COARSE-CellID-5K",
  "txid": "d4fbff33-eeee-ffff-gggg-2c90bd287e3b"
}
```

