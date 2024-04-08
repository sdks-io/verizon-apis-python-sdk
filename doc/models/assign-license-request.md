
# Assign License Request

Request to assign license.

## Structure

`AssignLicenseRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The name of a billing account.This parameter is required only if the UWS account used for the current API session has access to multiple accounts. An account name is usually numeric, and must include any leading zeros.<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32` |
| `devices` | [`List[LicenseDeviceList]`](../../doc/models/license-device-list.md) | Optional | A list of 4G devices.<br>**Constraints**: *Maximum Items*: `100` |
| `sku_number` | `str` | Optional | The Stock Keeping Unit (SKU). Valid skuNumbers for license types: “SIMSec-IoT-Lt”. (Lifetime) Once a license is assigned to a SIM, the SIM-Secure feature is enabled for the life of the SIM.“TS-BUNDLE-KTO-SIMSEC-MRC”. (Bundle) The SIM-Secure Flex license can be assigned to or removed from a SIM at any time. This SKU is bundled with other ThingSpace Services.“SIMSec-IoT”. (Flex) The SIM-Secure Flex license can be assigned to or removed from a SIM at any time. This SKU is purchased a la carte.<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32` |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "skuNumber": "SIMSec-IoT-Lt",
  "devices": [
    {
      "deviceIds": [
        {
          "id": "864508030109877",
          "kind": "IMEI"
        }
      ],
      "ipAddress": "ipAddress4"
    }
  ]
}
```

