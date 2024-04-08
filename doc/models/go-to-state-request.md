
# Go to State Request

Changes the provisioning state of one or more devices to a specified customer-defined service and state.

## Structure

`GoToStateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_name` | `str` | Required | The name of a customer-defined service to push the devices to. |
| `state_name` | `str` | Required | The name of a customer-defined stage state to push the devices to. |
| `service_plan` | `str` | Required | The service plan code that you want to assign to all specified devices in the new state. |
| `mdn_zip_code` | `str` | Required | The Zip code of the location where the line of service will primarily be used, or a Zip code that you have been told to use with these devices. For accounts that are configured for geographic numbering, this is the ZIP code from which the MDN will be derived. |
| `devices` | [`List[AccountDeviceList]`](../../doc/models/account-device-list.md) | Optional | Up to 10,000 devices that you want to push to a different state, specified by device identifier. |
| `filter` | [`DeviceFilter`](../../doc/models/device-filter.md) | Optional | Specify the kind of the device identifier, the type of match, and the string that you want to match. |
| `carrier_ip_pool_name` | `str` | Optional | The pool from which your device IP addresses will be derived if the service or state change requires new IP addresses.If you do not include this element, the default pool will be used. |
| `public_ip_restriction` | `str` | Optional | For devices with static IP addresses on the public network, this specifies whether the devices have general access to the Internet. Valid values are “restricted” or “unrestricted”. |
| `sku_number` | `str` | Optional | The Stock Keeping Unit (SKU) number of a 4G device type with an embedded SIM. Can be used with ICCID or EID device identifiers in lieu of an IMEI when activating 4G devices. The SkuNumber will be used with all devices in the request, so all devices must be of the same type. |
| `custom_fields` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | The names and values of any custom fields that you want to set for the devices. |
| `devices_with_service_address` | `List[object]` | Optional | This is an array that associates an IP address with a device identifier. This variable is only relevant for Business Internet/Fixed Wireless Access |
| `ip_address` | `str` | Optional | The IP address of the device. |
| `group_name` | `str` | Optional | The name of a device group that the devices should be added to. |
| `primary_place_of_use` | [`PlaceOfUse`](../../doc/models/place-of-use.md) | Optional | The customer name and the address of the device's primary place of use. Leave these fields empty to use the account profile address as the primary place of use. These values will be applied to all devices in the request.If the account is enabled for non-geographic MDNs and the device supports it, the primaryPlaceOfUse address will also be used to derive the MDN for the device. |

## Example (as JSON)

```json
{
  "devices": [
    {
      "deviceIds": [
        {
          "kind": "imei",
          "id": "990013907835573"
        },
        {
          "kind": "iccid",
          "id": "89141390780800784259"
        }
      ],
      "ipAddress": "ipAddress4"
    },
    {
      "deviceIds": [
        {
          "kind": "imei",
          "id": "990013907884259"
        },
        {
          "kind": "iccid",
          "id": "89141390780800735573"
        }
      ],
      "ipAddress": "ipAddress4"
    }
  ],
  "serviceName": "My Service",
  "stateName": "My State",
  "servicePlan": "87641",
  "mdnZipCode": "94203",
  "groupName": "4G West",
  "publicIpRestriction": "unrestricted",
  "primaryPlaceOfUse": {
    "customerName": {
      "title": "President",
      "firstName": "Zaffod",
      "lastName": "Beeblebrox"
    },
    "address": {
      "addressLine1": "1600 Pennsylvania Ave NW",
      "city": "Washington",
      "state": "DC",
      "zip": "20500",
      "country": "USA"
    }
  },
  "filter": {
    "account": "account4",
    "groupName": "groupName6",
    "servicePlan": "servicePlan6",
    "customFields": [
      {
        "key": "key0",
        "value": "value2"
      },
      {
        "key": "key0",
        "value": "value2"
      },
      {
        "key": "key0",
        "value": "value2"
      }
    ]
  },
  "carrierIpPoolName": "carrierIpPoolName8",
  "skuNumber": "skuNumber6"
}
```

