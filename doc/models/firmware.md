
# Firmware

Firmware information.

## Structure

`Firmware`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `firmware_name` | `str` | Optional | The name of the firmware image, provided by the device manufacturer. |
| `participant_name` | `str` | Optional | Internal reference; can be ignored. |
| `launch_date` | `datetime` | Optional | The release date of the firmware image. |
| `release_note` | `str` | Optional | Additional information about the release. |
| `model` | `str` | Optional | The device model that the firmware applies to. |
| `make` | `str` | Optional | The device make that the firmware applies to. |
| `from_version` | `str` | Optional | The firmware version that must currently be on the device to upgrade. |
| `to_version` | `str` | Optional | The firmware version that will be on the device after an upgrade. |

## Example (as JSON)

```json
{
  "firmwareName": "FOTA_Verizon_Model-A_01To02_HF",
  "participantName": "0402196254-00001",
  "launchDate": "2018-04-01T16:03:00.000Z",
  "releaseNote": "",
  "model": "Model-A",
  "make": "Verizon",
  "fromVersion": "VerizonFirmwareVersion-01",
  "toVersion": "VerizonFirmwareVersion-02"
}
```

