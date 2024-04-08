
# Firmware IMEI

A list of IMEIs for devices to be synchronized between ThingSpace and the FOTA server.

## Structure

`FirmwareIMEI`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_list` | `List[str]` | Required | Device IMEI list.<br>**Constraints**: *Maximum Items*: `1000` |

## Example (as JSON)

```json
{
  "deviceList": [
    "15-digit IMEI"
  ]
}
```

