
# Service Resume Result

## Structure

`ServiceResumeResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `string` | Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `correlation_id` | `string` | Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `message` | `string` | Optional | **Constraints**: *Maximum Length*: `500`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `status` | `string` | Optional | **Constraints**: *Maximum Length*: `15`, *Pattern*: `^[A-Za-z]{1,15}$` |
| `sub_status` | `string` | Optional | **Constraints**: *Maximum Length*: `15`, *Pattern*: `^[A-Za-z]{1,15}$` |

## Example (as JSON)

```json
{
  "requestId": "requestId2",
  "correlationId": "correlationId0",
  "message": "message0",
  "status": "status8",
  "subStatus": "subStatus6"
}
```

