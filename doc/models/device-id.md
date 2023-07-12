
# Device Id

An identifier for a single device.

## Structure

`DeviceId`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The value of the device identifier. |
| `kind` | `string` | Optional | The type of the device identifier. Valid types of identifiers are:ESN (decimal),EID,ICCID (up to 20 digits),IMEI (up to 16 digits),MDN,MEID (hexadecimal),MSISDN. |

## Example (as JSON)

```json
{
  "kind": "imei",
  "id": "990013907835573"
}
```

