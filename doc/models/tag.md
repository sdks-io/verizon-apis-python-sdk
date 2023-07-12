
# Tag

Any name for the tag.

## Structure

`Tag`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | Id of the user creating the repository.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `key` | `string` | Required | Key properties/metadata attribute.<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!\/,+\-=_:.&*%\s]+$` |
| `description` | `string` | Optional | Description for the repository being created.<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |
| `value` | `string` | Optional | Properties/metadata value attribute.<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!\/,+\-=_:.&*%\s]+$` |
| `created_date` | `datetime` | Optional | Date when the repository was created. |
| `last_modified_date` | `datetime` | Optional | Date when the repository was updated. |
| `created_by` | `string` | Optional | User information by whom the repository was created.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `updated_by` | `string` | Optional | User information by whom the repository was updated.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |

## Example (as JSON)

```json
{
  "id": "uuid",
  "key": "Mytag",
  "description": "Tag.",
  "value": "IOT",
  "createdDate": "2006-01-02T15:04:05Z",
  "lastModifiedDate": "2006-01-02T15:04:05Z",
  "createdBy": "User",
  "updatedBy": "User"
}
```

