
# Update Service Profile Result

Response on successful update of service profile.

## Structure

`UpdateServiceProfileResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Optional | HTTP status code.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `message` | `str` | Optional | Service Profile that are updated or error details in case of an error.<br>**Constraints**: *Maximum Length*: `32` |

## Example (as JSON)

```json
{
  "status": "Success",
  "message": "Service Profile Updated"
}
```

