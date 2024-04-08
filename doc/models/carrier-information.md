
# Carrier Information

Information about the carrier.

## Structure

`CarrierInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `carrier_name` | `str` | Optional | The carrier that will perform the activation. This parameter is only required if you have more than one carrier. |
| `service_plan` | `str` | Optional | The service plan code that is assigned to the device. |
| `state` | `str` | Optional | The device state. Valid values include: Activate, Suspend, Deactive, Pre-active. |

## Example (as JSON)

```json
{
  "carrierName": "Verizon Wireless",
  "servicePlan": "m2m4G",
  "state": "active"
}
```

