
# Primary Place of Use

## Structure

`PrimaryPlaceOfUse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_name` | [`List of CustomerName`](../../doc/models/customer-name.md) | Optional | **Constraints**: *Maximum Items*: `5` |
| `address` | [`List of Address`](../../doc/models/address.md) | Optional | **Constraints**: *Maximum Items*: `5` |

## Example (as JSON)

```json
{
  "customerName": [
    {
      "title": "title9",
      "firstName": "firstName9",
      "middleName": "middleName3",
      "lastName": "lastName9",
      "suffix": "suffix5"
    },
    {
      "title": "title8",
      "firstName": "firstName8",
      "middleName": "middleName4",
      "lastName": "lastName0",
      "suffix": "suffix4"
    },
    {
      "title": "title7",
      "firstName": "firstName7",
      "middleName": "middleName5",
      "lastName": "lastName1",
      "suffix": "suffix3"
    }
  ],
  "address": [
    {
      "addressLine1": "addressLine16",
      "addressLine2": "addressLine24",
      "city": "city4",
      "state": "state0",
      "zip": "zip8",
      "zip4": "zip48",
      "country": "country8",
      "phone": "phone4",
      "phoneType": "phoneType8",
      "emailAddress": "emailAddress4"
    }
  ]
}
```

