
# Device Id

device identifiers consisting of an ID value and what that value represents (kind)

## Structure

`DeviceId`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The numeric or alphanumeric ID value |
| `kind` | `str` | Optional | What the ID value represents, which could be a Mobile Directory Number (MDN) or an International Mobile Equipment Identifier (IMEI) as an example |

## Example (as JSON)

```json
{
  "id": "10-digit phone number",
  "kind": "mdn"
}
```

