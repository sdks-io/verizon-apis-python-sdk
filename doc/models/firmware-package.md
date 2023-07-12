
# Firmware Package

Available firmware.

## Structure

`FirmwarePackage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `firmware_name` | `string` | Required | Firmware name. |
| `firmware_from` | `string` | Required | Firmware from version. |
| `firmware_to` | `string` | Required | Firmware to version. |
| `launch_date` | `datetime` | Required | Firmware launch date. |
| `release_note` | `string` | Required | Firmware release note. |
| `model` | `string` | Required | Firmware applicable device model. |
| `make` | `string` | Required | Firmware applicable device make. |
| `protocol` | [`CampaignMetaInfoProtocolEnum`](../../doc/models/campaign-meta-info-protocol-enum.md) | Required | Firmware protocol. Valid values include: LWM2M, OMD-DM.<br>**Default**: `'LWM2M'` |

## Example (as JSON)

```json
{
  "firmwareName": "VerizonSmartCommunities_LCO-277C4N_BG96MAR04A04M1G_BG96MAR04A04M1G_BETA0130B",
  "firmwareFrom": "BG96MAR04A04M1G",
  "firmwareTo": "BG96MAR04A04M1G_BETA0130B",
  "launchDate": "2012-04-23T18:25:43.511Z",
  "releaseNote": "",
  "model": "LCO-277C4N",
  "make": "Verizon Smart Communities",
  "protocol": "LWM2M"
}
```

