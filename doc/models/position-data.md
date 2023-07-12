
# Position Data

Position data.

## Structure

`PositionData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `time` | `string` | Optional | Time location obtained. |
| `utcoffset` | `string` | Optional | UTC offset of time. |
| `x` | `string` | Optional | X coordinate of location. |
| `y` | `string` | Optional | Y coordinate of location. |
| `radius` | `string` | Optional | Radius of the location in meters. |
| `qos` | `bool` | Optional | Whether requested accurary is met or not. |

## Example (as JSON)

```json
{
  "qos": false,
  "radius": "5571",
  "time": "20170520004421",
  "x": "33.45324",
  "y": "-84.59621",
  "utcoffset": "utcoffset0"
}
```

