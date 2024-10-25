
# 5g Biaccount Nameobject

## Structure

`M5gBiaccountNameobject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | - |
| `billing_cycle_end_date` | `str` | Optional | - |
| `carrier_information` | [`List[M5gBiCarrierInformation]`](../../doc/models/5g-bi-carrier-information.md) | Optional | - |
| `connected` | `bool` | Optional | - |
| `created_at` | `str` | Optional | - |
| `custom_fields` | [`List[M5gBikeyValue1]`](../../doc/models/5g-bikey-value-1.md) | Optional | - |
| `device_ids` | [`List[M5gBideviceId1]`](../../doc/models/5g-bidevice-id-1.md) | Optional | - |
| `extended_attributes` | [`List[M5gBikeyValue1]`](../../doc/models/5g-bikey-value-1.md) | Optional | - |
| `group_names` | [`List[GroupName]`](../../doc/models/group-name.md) | Optional | - |
| `ipaddress` | `str` | Optional | - |
| `last_activation_by` | `str` | Optional | - |
| `last_activation_date` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "billingCycleEndDate": "11/10/2022 00:00:00",
  "connected": false,
  "createdAt": "10/20/2022 18:23:41",
  "ipAddress": "0.0.0.0",
  "lastActivationBy": "User Name",
  "lastActivationDate": "2022-11-02 T21:36:18Z",
  "carrierInformation": [
    {
      "carrierName": "carrierName4"
    },
    {
      "carrierName": "carrierName4"
    },
    {
      "carrierName": "carrierName4"
    }
  ]
}
```

