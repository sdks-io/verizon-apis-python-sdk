
# Account Service

Service associated with the account.

## Structure

`AccountService`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | The name of the service plan. |
| `description` | `str` | Optional | The description of the service plan. |
| `states` | [`List[State]`](../../doc/models/state.md) | Optional | The state of the service plan. |

## Example (as JSON)

```json
{
  "name": "Svc1",
  "description": "Usage Segmentation - Main Line.",
  "states": [
    {
      "name": "Svc1 Activate",
      "workflowSequenceNumber": 1.0,
      "servicePlans": [
        "4523aef7250f67205fd5",
        "4d4090c0f2d48814c94d"
      ]
    },
    {
      "name": "Svc1 No Telematics",
      "workflowSequenceNumber": 3.0,
      "servicePlans": [
        "4523aef7250f67205fd5",
        "4d4090c0f2d48814c94d"
      ]
    },
    {
      "name": "Svc1 Deactivate",
      "workflowSequenceNumber": 2.0,
      "servicePlans": [
        "4523aef7250f67205fd5",
        "4d4090c0f2d48814c94d"
      ]
    }
  ]
}
```

