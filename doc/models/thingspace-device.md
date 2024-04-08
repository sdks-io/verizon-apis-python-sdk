
# Thingspace Device

Device that exist in Verizon Mobile Device Management (MDM).

## Structure

`ThingspaceDevice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The billing account that the device is associated with. |
| `billing_cycle_end_date` | `str` | Optional | The date that the device's current billing cycle ends. |
| `carrier_informations` | [`List[CarrierInformation]`](../../doc/models/carrier-information.md) | Optional | The carrier information associated with the device. |
| `connected` | `bool` | Optional | True if the device is connected; false if it is not. |
| `created_at` | `str` | Optional | The date and time that the device was added to the system. |
| `custom_fields` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | The custom fields and values that have been set for the device. |
| `device_ids` | [`List[DeviceId]`](../../doc/models/device-id.md) | Optional | All identifiers for the device. |
| `extended_attributes` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | Any extended attributes for the device, as Key and Value pairs. The pairs listed below are returned as part of the response for a single device, but are not included if the request was for information about multiple devices. |
| `group_names` | `List[str]` | Optional | The device groups that the device belongs to. |
| `ip_address` | `str` | Optional | The IP address of the device. |
| `last_activation_by` | `str` | Optional | The user who last activated the device. |
| `last_activation_date` | `str` | Optional | The date and time that the device was last activated. |
| `last_connection_date` | `str` | Optional | The most recent connection date and time. |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "billingCycleEndDate": "2020-05-09T20:00:00-04:00",
  "carrierInformations": [
    {
      "carrierName": "Verizon Wireless",
      "servicePlan": "m2m4G",
      "state": "active"
    }
  ],
  "connected": false,
  "createdAt": "2019-08-07T10:42:15-04:00",
  "deviceIds": [
    {
      "id": "10-digit MDN",
      "kind": "mdn"
    },
    {
      "id": "15-digit IMEI",
      "kind": "imei"
    }
  ],
  "groupNames": [
    "southwest"
  ],
  "ipAddress": "0.0.0.0",
  "lastActivationBy": "Joe Q Public",
  "lastActivationDate": "2019-08-07T10:42:34-04:00",
  "lastConnectionDate": "2020-03-12T04:23:37-04:00"
}
```

