
# Account Leads Result

Returns information for all leads associated with an account.

## Structure

`AccountLeadsResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_more_data` | `bool` | Optional | False if no more leads.True if there is more data to be retrieved. |
| `leads` | [`List[AccountLead]`](../../doc/models/account-lead.md) | Optional | The leads associated with an account. |

## Example (as JSON)

```json
{
  "leads": [
    {
      "leadId": "L-10001",
      "leadState": "Qualified",
      "address": {
        "addressLine1": "1600 Pennsylvania Avenue",
        "addressLine2": "",
        "city": "Washington",
        "state": "DC",
        "zip": "20500",
        "country": "USA",
        "zip4": "zip40",
        "phone": "phone4",
        "phoneType": "phoneType0",
        "emailAddress": "emailAddress6"
      }
    }
  ],
  "hasMoreData": false
}
```

