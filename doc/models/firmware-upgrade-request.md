
# Firmware Upgrade Request

Details of the firmware upgrade request.

## Structure

`FirmwareUpgradeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account identifier in "##########-#####". |
| `firmware_name` | `str` | Required | The name of the firmware image that will be used for the upgrade, from a GET /firmware response. |
| `firmware_to` | `str` | Required | The name of the firmware version that will be on the devices after a successful upgrade. |
| `start_date` | `datetime` | Required | The date that the upgrade should begin. |
| `device_list` | `List[str]` | Required | The IMEIs of the devices. |

## Example (as JSON)

```json
{
  "accountName": "0402196254-00001",
  "firmwareName": "FOTA_Verizon_Model-A_01To02_HF",
  "firmwareTo": "VerizonFirmwareVersion-02",
  "startDate": "2018-04-01T16:03:00.000Z",
  "deviceList": [
    "990003425730535",
    "990000473475989"
  ]
}
```

