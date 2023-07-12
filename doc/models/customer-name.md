
# Customer Name

The customer name to be used for line usage taxation.

## Structure

`CustomerName`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `string` | Optional | An optional title for the customer, such as “Mr.” or “Dr.” |
| `first_name` | `string` | Required | The customer's first name. |
| `middle_name` | `string` | Optional | The customer's middle name. |
| `last_name` | `string` | Required | The customer's last name. |
| `suffix` | `string` | Optional | An optional suffix for the customer name, such as “Jr.” or “III.” |

## Example (as JSON)

```json
{
  "title": "President",
  "firstName": "Zaffod",
  "lastName": "Beeblebrox",
  "middleName": "middleName8",
  "suffix": "suffix0"
}
```

