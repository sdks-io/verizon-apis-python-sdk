
# Account Lead

A successful response returns an array of lead objects.

## Structure

`AccountLead`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`Address`](../../doc/models/address.md) | Optional | The customer address for the line's primary place of use, for line usage taxation. |
| `lead_id` | `str` | Optional | Unique number for each lead. Use this value in the leadId parameter when activating devices to credit the activations to the lead. |
| `lead_state` | `str` | Optional | The current state of the lead, such as “Qualified” or “Closed.” |

## Example (as JSON)

```json
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
```

