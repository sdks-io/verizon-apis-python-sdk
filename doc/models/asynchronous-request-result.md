
# Asynchronous Request Result

A successful request returns the request ID and the current status.

## Structure

`AsynchronousRequestResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | The unique ID of the asynchronous request. |
| `status` | [`RequestStatusEnum`](../../doc/models/request-status-enum.md) | Optional | The current status of the callback response. |

## Example (as JSON)

```json
{
  "requestId": "86c83330-4bf5-4235-9c4e-a83f93aeae4c",
  "status": "Success"
}
```

