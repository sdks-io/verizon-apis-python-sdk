
# Profile Request

## Structure

`ProfileRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | - |
| `devices` | [`List[DeviceList]`](../../doc/models/device-list.md) | Required | **Constraints**: *Maximum Items*: `100` |
| `carrier_name` | `str` | Optional | - |
| `service_plan` | `str` | Optional | - |
| `mdn_zip_code` | `str` | Optional | - |
| `primary_place_of_use` | [`List[PrimaryPlaceOfUse]`](../../doc/models/primary-place-of-use.md) | Optional | **Constraints**: *Maximum Items*: `25` |
| `smsr_oid` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `46`, *Pattern*: `^[0-9.]{3,46}$` |
| `carrier_ip_pool_name` | `str` | Optional | The name of the pool of IP addresses assigned to the profile. |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "devices": [
    {
      "deviceIds": [
        {
          "id": "id0",
          "kind": "kind8"
        }
      ]
    }
  ],
  "carrierName": "the name of the mobile service provider",
  "servicePlan": "The service plan name",
  "mdnZipCode": "five digit zip code",
  "primaryPlaceOfUse": [
    {
      "customerName": [
        {
          "title": "title4",
          "firstName": "firstName4",
          "middleName": "middleName8",
          "lastName": "lastName4",
          "suffix": "suffix0"
        }
      ],
      "address": [
        {
          "addressLine1": "addressLine18",
          "addressLine2": "addressLine26",
          "city": "city6",
          "state": "state2",
          "zip": "zip0",
          "zip4": "zip40",
          "country": "country0",
          "phone": "phone4",
          "phoneType": "phoneType0",
          "emailAddress": "emailAddress6"
        },
        {
          "addressLine1": "addressLine18",
          "addressLine2": "addressLine26",
          "city": "city6",
          "state": "state2",
          "zip": "zip0",
          "zip4": "zip40",
          "country": "country0",
          "phone": "phone4",
          "phoneType": "phoneType0",
          "emailAddress": "emailAddress6"
        }
      ]
    },
    {
      "customerName": [
        {
          "title": "title4",
          "firstName": "firstName4",
          "middleName": "middleName8",
          "lastName": "lastName4",
          "suffix": "suffix0"
        }
      ],
      "address": [
        {
          "addressLine1": "addressLine18",
          "addressLine2": "addressLine26",
          "city": "city6",
          "state": "state2",
          "zip": "zip0",
          "zip4": "zip40",
          "country": "country0",
          "phone": "phone4",
          "phoneType": "phoneType0",
          "emailAddress": "emailAddress6"
        },
        {
          "addressLine1": "addressLine18",
          "addressLine2": "addressLine26",
          "city": "city6",
          "state": "state2",
          "zip": "zip0",
          "zip4": "zip40",
          "country": "country0",
          "phone": "phone4",
          "phoneType": "phoneType0",
          "emailAddress": "emailAddress6"
        }
      ]
    }
  ],
  "smsrOid": "smsrOid6"
}
```

