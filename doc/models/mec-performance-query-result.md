
# MEC Performance Query Result

Result of the query for obtaining MEC performance metrics.

## Structure

`MECPerformanceQueryResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the parameter. |
| `data` | `List[str]` | Optional | Parameter values. |

## Example (as JSON)

```json
{
  "name": "NetworkAvailability",
  "data": [
    "100",
    "percent",
    "high"
  ]
}
```

