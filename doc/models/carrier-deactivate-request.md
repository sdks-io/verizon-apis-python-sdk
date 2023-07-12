
# Carrier Deactivate Request

Request to deactivate a carrier.

## Structure

`CarrierDeactivateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Optional | The name of a billing account. |
| `custom_fields` | [`List of CustomFields`](../../doc/models/custom-fields.md) | Optional | Custom field names and values, if you want to only include devices that have matching values. |
| `devices` | [`List of AccountDeviceList`](../../doc/models/account-device-list.md) | Optional | The devices for which you want to deactivate service, specified by device identifier. |
| `etf_waiver` | `bool` | Optional | Fees may be assessed for deactivating Verizon Wireless devices, depending on the account contract. The etfWaiver parameter waives the Early Termination Fee (ETF), if applicable. |
| `group_name` | `string` | Optional | The name of a device group, if you want to deactivate all devices in that group. |
| `reason_code` | `string` | Optional | Code identifying the reason for the deactivation. Currently the only valid reason code is “FF”, which corresponds to General Admin/Maintenance. |
| `service_plan` | `string` | Optional | The name of a service plan, if you want to only include devices that have that service plan. |

## Example (as JSON)

```json
{
  "devices": [
    {
      "deviceIds": [
        {
          "id": "20-digit ICCID",
          "kind": "iccid"
        }
      ]
    }
  ],
  "reasonCode": "FF",
  "etfWaiver": true,
  "accountName": "accountName4",
  "customFields": [
    {
      "key": "key0",
      "value": "value2"
    },
    {
      "key": "key1",
      "value": "value3"
    },
    {
      "key": "key2",
      "value": "value4"
    }
  ],
  "groupName": "groupName0"
}
```

