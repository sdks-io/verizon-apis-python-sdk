
# Managed Accounts Get All Response

## Structure

`ManagedAccountsGetAllResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Optional | Account Name |
| `managed_acc_added_list` | [`List of ManagedAccAddedList`](../../doc/models/managed-acc-added-list.md) | Optional | - |
| `managed_acc_provisioned_list` | [`List of ManagedAccProvisionedList`](../../doc/models/managed-acc-provisioned-list.md) | Optional | - |

## Example (as JSON)

```json
{
  "accountName": "0212312345-00001",
  "ManagedAccAddedList": [
    {
      "id": "id3",
      "txid": "txid9"
    },
    {
      "id": "id4",
      "txid": "txid8"
    },
    {
      "id": "id5",
      "txid": "txid7"
    }
  ],
  "managedAccProvisionedList": [
    {
      "id": "id1",
      "txid": "txid1"
    },
    {
      "id": "id2",
      "txid": "txid0"
    },
    {
      "id": "id3",
      "txid": "txid9"
    }
  ]
}
```

