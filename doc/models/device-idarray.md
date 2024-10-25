
# Device Idarray

## Structure

`DeviceIdarray`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `kind` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `id` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |

## Example (as JSON)

```json
{
  "kind": "imei",
  "id": "id8"
}
```

