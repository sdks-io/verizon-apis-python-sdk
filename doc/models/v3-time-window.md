
# V3 Time Window

Time window.

## Structure

`V3TimeWindow`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_time` | `int` | Required | Start hour in range [0..23], current hour >= startTime. |
| `end_time` | `int` | Required | End hour in range [1..24], current hour < endTime. |

## Example (as JSON)

```json
{
  "startTime": 18,
  "endTime": 22
}
```

