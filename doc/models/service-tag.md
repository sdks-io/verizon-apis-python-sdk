
# Service Tag

Service tag has key and value attribute.

## Structure

`ServiceTag`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `string` | Optional | Service tag key attribute.<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!\/,+\-=_:.&*%\s]+$` |
| `value` | `string` | Optional | Service tag value attribute.<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!\/,+\-=_:.&*%\s]+$` |

## Example (as JSON)

```json
{
  "key": "vnsp.mec.verizon.com/serviceType",
  "value": "My service"
}
```

