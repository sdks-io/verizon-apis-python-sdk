
# Managed Accounts Add Response

## Structure

`ManagedAccountsAddResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tx_id` | `string` | Optional | Transaction identifier |
| `status_list` | [`List of StatusList`](../../doc/models/status-list.md) | Optional | - |

## Example (as JSON)

```json
{
  "TxId": "2c90bd28-ece4-42ef-9f02-7e3bd4fbff33",
  "statusList": [
    {
      "id": "id4",
      "status": "status6",
      "reason": "reason0"
    },
    {
      "id": "id5",
      "status": "status7",
      "reason": "reason1"
    },
    {
      "id": "id6",
      "status": "status8",
      "reason": "reason2"
    }
  ]
}
```

