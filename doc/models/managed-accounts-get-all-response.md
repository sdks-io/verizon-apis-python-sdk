
# Managed Accounts Get All Response

## Structure

`ManagedAccountsGetAllResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Account Name |
| `managed_acc_added_list` | [`List[ManagedAccAddedList]`](../../doc/models/managed-acc-added-list.md) | Optional | - |
| `managed_acc_provisioned_list` | [`List[ManagedAccProvisionedList]`](../../doc/models/managed-acc-provisioned-list.md) | Optional | - |

## Example (as JSON)

```json
{
  "accountName": "0212312345-00001",
  "ManagedAccAddedList": [
    {
      "id": "id6",
      "txid": "txid6"
    }
  ],
  "managedAccProvisionedList": [
    {
      "id": "id2",
      "txid": "txid0"
    }
  ]
}
```

