
# Data Percentage 90 Trigger Attribute

Trigger attribute for when data percentage is over 90% used.

## Structure

`DataPercentage90TriggerAttribute`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Optional | Key data percentage 90. |
| `value` | `bool` | Optional | DataPercentage90<br />True - Trigger on Data percentage is over 90% used<br />False - Do not trigger when over 90% used. |

## Example (as JSON)

```json
{
  "key": "DataPercentage90",
  "value": false
}
```

