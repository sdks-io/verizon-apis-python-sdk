
# Contact Info Update Request

Request to update contact information.

## Structure

`ContactInfoUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Optional | The name of the billing account that the devices belong to. An account name is usually numeric, and must include any leading zeros. |
| `devices` | [`List of AccountDeviceList`](../../doc/models/account-device-list.md) | Optional | A list of the devices that you want to change, specified by device identifier. You only need to provide one identifier per device. Do not include accountName, groupName, customFields, or servicePlan if you use this parameter. |
| `primary_place_of_use` | `object` | Optional | The customer name and the address of the device's primary place of use. These values are applied to all devices in the request.The Primary Place of Use location may affect taxation or have other legal implications. You may want to speak with legal and/or financial advisers before entering values for these fields. |

## Example (as JSON)

```json
{
  "devices": [
    {
      "deviceIds": [
        {
          "kind": "ESN",
          "id": "19110173057"
        },
        {
          "kind": "ESN",
          "id": "19110173057"
        }
      ]
    }
  ],
  "accountName": "0212345678-00001",
  "primaryPlaceOfUse": {
    "address": {
      "addressLine1": "9868 Scranton Rd",
      "addressLine2": "Suite A",
      "city": "San Diego",
      "state": "CA",
      "country": "USA",
      "zip": "92121",
      "zip4": "0001",
      "phone": "1234567890",
      "phoneType": "H",
      "emailAddress": "zaffod@theinternet.com"
    },
    "customerName": {
      "firstName": "Zaffod",
      "lastName": "Beeblebrox",
      "middleName": "P",
      "title": "President",
      "suffix": "I"
    }
  }
}
```

