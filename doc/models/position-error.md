
# Position Error

Position error.

## Structure

`PositionError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `time` | `string` | Optional | Time location obtained. |
| `utcoffset` | `string` | Optional | UTC offset of time. |
| `mtype` | `string` | Optional | Error type returned from location server. |
| `info` | `string` | Optional | Additional information about the error. |

## Example (as JSON)

```json
{
  "time": "20170525214342",
  "type": "POSITION METHOD FAILURE",
  "info": "Exception code=ABSENT SUBSCRIBER",
  "utcoffset": "utcoffset0"
}
```

