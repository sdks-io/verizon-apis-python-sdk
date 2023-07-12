
# MEC Performance Query Result

Result of the query for obtaining MEC performance metrics.

## Structure

`MECPerformanceQueryResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | Name of the parameter. |
| `data` | `List of string` | Optional | Parameter values. |

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

