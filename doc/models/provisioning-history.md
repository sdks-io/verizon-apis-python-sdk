
# Provisioning History

The provisioning history of a specified device during a specified time period.

## Structure

`ProvisioningHistory`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `occurred_at` | `str` | Optional | The date and time when the provisioning event occured. |
| `status` | `str` | Optional | The success or failure of the provisioning event. |
| `event_by` | `str` | Optional | The user who performed the provisioning event. |
| `event_type` | `str` | Optional | The provisioning action:Activate,Suspend,Restore,Deactivate,Device Move. |
| `mdn` | `str` | Optional | The MDN assigned to the device after the provisioning event. |
| `msisdn` | `str` | Optional | The MSISDN assigned to the device after the provisioning event. |
| `service_plan` | `str` | Optional | The service plan of the device after the provisioning event occurred. |
| `extended_attributes` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | Any extended attributes for the event, as Key and Value pairs. |

## Example (as JSON)

```json
{
  "occurredAt": "2015-12-17T13:56:13-05:00",
  "status": "Success",
  "eventBy": "Harry Potter",
  "eventType": "Activation Confirmed",
  "servicePlan": "Tablet5GB",
  "mdn": "",
  "msisdn": "15086303371",
  "extendedAttributes": []
}
```

