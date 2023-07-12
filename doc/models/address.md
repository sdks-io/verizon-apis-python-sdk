
# Address

The customer address for the line's primary place of use, for line usage taxation.

## Structure

`Address`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_line_1` | `string` | Required | The street address for the line's primary place of use. This must be a physical address for taxation; it cannot be a P.O. box. |
| `address_line_2` | `string` | Optional | Optional additional street address information. |
| `city` | `string` | Required | The city for the line's primary place of use. |
| `state` | `string` | Required | The state for the line's primary place of use. |
| `zip` | `string` | Required | The ZIP code for the line's primary place of use. |
| `zip_4` | `string` | Optional | The ZIP+4 for the line's primary place of use. |
| `country` | `string` | Required | Either “US” or “USA” for the country of the line's primary place of use. |
| `phone` | `string` | Optional | A phone number where the customer can be reached. |
| `phone_type` | `string` | Optional | A single letter to indicate the customer phone type. |
| `email_address` | `string` | Optional | An email address for the customer. |

## Example (as JSON)

```json
{
  "addressLine1": "1600 Pennsylvania Ave NW",
  "city": "Washington",
  "state": "DC",
  "zip": "20500",
  "country": "USA",
  "addressLine2": "addressLine20",
  "zip4": "zip46",
  "phone": "phone0",
  "phoneType": "phoneType6",
  "emailAddress": "emailAddress0"
}
```

