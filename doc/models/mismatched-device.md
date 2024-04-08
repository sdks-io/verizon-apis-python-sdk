
# Mismatched Device

4G devices with an ICCID (SIM) that was not activated with the expected IMEI (hardware) during a specified time frame.

## Structure

`MismatchedDevice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The account that the device is associated with. |
| `mdn` | `str` | Optional | The assigned phone number of the device. |
| `activation_date` | `str` | Optional | The date and time when the SIM was last activated. |
| `iccid` | `str` | Optional | The ID of the SIM. |
| `pre_imei` | `str` | Optional | The IMEI of the device prior to the SIM OTA activation on simOtaDate. |
| `post_imei` | `str` | Optional | The IMEI of the device after the SIM OTA activation on simOtaDate. |
| `sim_ota_date` | `str` | Optional | The date and time of the SIM OTA activation. |

## Example (as JSON)

```json
{
  "accountName": "0212398765-00001",
  "mdn": "5096300587",
  "activationDate": "2011-01-21T10:55:27-08:00",
  "iccid": "89148000000800784259",
  "preImei": "990003420535573",
  "postImei": "987603420573553",
  "simOtaDate": "2017-12-01T16:00:00-08:00"
}
```

