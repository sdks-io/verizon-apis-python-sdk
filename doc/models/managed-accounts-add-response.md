
# Managed Accounts Add Response

## Structure

`ManagedAccountsAddResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tx_id` | `str` | Optional | Transaction identifier |
| `status_list` | [`List[StatusList]`](../../doc/models/status-list.md) | Optional | - |

## Example (as JSON)

```json
{
  "TxId": "2c90bd28-ece4-42ef-9f02-7e3bd4fbff33",
  "statusList": [
    {
      "id": "id6",
      "status": "status8",
      "reason": "reason8"
    }
  ]
}
```

