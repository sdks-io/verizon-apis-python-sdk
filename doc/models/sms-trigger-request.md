
# SMS Trigger Request

## Structure

`SMSTriggerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `comparator` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `sms_type` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `threshold` | `int` | Optional | **Constraints**: `>= 0`, `<= 100` |

## Example (as JSON)

```json
{
  "comparator": "comparator0",
  "smsType": "smsType6",
  "threshold": 222
}
```

