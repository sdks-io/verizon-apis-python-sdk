
# Address

The customer address for the line's primary place of use, for line usage taxation.

## Structure

`Address`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_line_1` | `str` | Required | The street address for the line's primary place of use. This must be a physical address for taxation; it cannot be a P.O. box. |
| `address_line_2` | `str` | Optional | Optional additional street address information. |
| `city` | `str` | Required | The city for the line's primary place of use. |
| `state` | `str` | Required | The state for the line's primary place of use. |
| `zip` | `str` | Required | The ZIP code for the line's primary place of use. |
| `zip_4` | `str` | Optional | The ZIP+4 for the line's primary place of use. |
| `country` | `str` | Required | Either “US” or “USA” for the country of the line's primary place of use. |
| `phone` | `str` | Optional | A phone number where the customer can be reached. |
| `phone_type` | `str` | Optional | A single letter to indicate the customer phone type. |
| `email_address` | `str` | Optional | An email address for the customer. |

## Example (as JSON)

```json
{
  "addressLine1": "1600 Pennsylvania Ave NW",
  "city": "Washington",
  "state": "DC",
  "zip": "20500",
  "country": "USA",
  "addressLine2": "addressLine28",
  "zip4": "zip42",
  "phone": "phone8",
  "phoneType": "phoneType2",
  "emailAddress": "emailAddress8"
}
```

