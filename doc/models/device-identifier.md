
# Device Identifier

Device Id details.

## Structure

`DeviceIdentifier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `kind` | `str` | Required | Kind of device.<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `6`, *Pattern*: `^[A-Za-z]{3,6}$` |
| `id` | `str` | Required | Device Identity number.<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9]{3,32}$` |
| `mdn` | `str` | Optional | Device MDN number.<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `10`, *Pattern*: `^[A-Za-z0-9]{3,10}$` |

## Example (as JSON)

```json
{
  "kind": "iccid",
  "id": "01234567899876543210",
  "mdn": "0123456789"
}
```

