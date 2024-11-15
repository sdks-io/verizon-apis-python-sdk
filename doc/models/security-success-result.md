
# Security Success Result

Success response.

## Structure

`SecuritySuccessResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | A unique string that associates the request with the results that are sent via a callback message.The ThingSpace Platform sends a separate callback message for each device that matches the request criteria, indicating whether the operation succeeded for that device and containing any requested information. All callback messages will have the same requestId. |

## Example (as JSON)

```json
{
  "requestId": "c3f3d17c-79ff-4b35-82df-94446785b6e0"
}
```

