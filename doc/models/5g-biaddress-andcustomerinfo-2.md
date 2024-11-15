
# 5g Biaddress Andcustomerinfo 2

## Structure

`M5gBiaddressAndcustomerinfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `primary_placeofuse` | [`M5gBiaddressAndcustomerinfo`](../../doc/models/5g-biaddress-andcustomerinfo.md) | Optional | - |

## Example (as JSON)

```json
{
  "primaryPlaceofuse": {
    "address": {
      "addressLine1": "street number and name",
      "city": "city of the address",
      "state": "2-letter state ID (conforms to ISO 3166-2)",
      "zip": "5-digit zip code",
      "zip+4": "the +4 digits used for zip codes"
    },
    "customerName": {
      "firstNname": "First name",
      "lastName": "Surname or Last Name"
    },
    "primaryPlaceofuse": {
      "address": {
        "addressLine1": "addressLine18",
        "city": "city6",
        "state": "state2",
        "zip": "zip0",
        "zip+4": "zip+48"
      },
      "customerName": {
        "firstName": "firstName4",
        "lastName": "lastName4",
        "middleName": "middleName8",
        "title": "title4",
        "suffex": "suffex4"
      }
    }
  }
}
```

