
# Service Management Result

## Structure

`ServiceManagementResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `job_id` | `string` | Optional | Auto-generated Id of the job.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `status` | `string` | Optional | Can have one string value mentioned below - DRAFT, DESIGN, TESTING, PUBLISH, CERTIFY, READY_TO_USE, DEPRECATE, DELETED.<br>**Constraints**: *Maximum Length*: `15`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]!,+\-=_:.&*%\s]+$` |
| `state` | `string` | Optional | Can have one string value mentioned below - DRAFT_INPROGRESS, DRAFT_COMPLETE, DESIGN_INPROGRESS, DESIGN_FAILED, DESIGN_COMPLETED, VALIDATION_INPROGRESS,  VALIDATION_FAILED, VALIDATION_COMPLETED, TESTING_INPROGRESS, TESTING_FAILED, TESTING_COMPLETED, READY_TO_USE_INPROGRESS, READY_TO_USE_FAILED, READY_TO_USE_COMPLETED, READY_TO_PRIVATE_USE_INPROGRESS, READY_TO_PRIVATE_USE_FAILED, READY_TO_PRIVATE_USE_COMPLETED,  PUBLISH_INPROGRESS,  PUBLISH_FAILED,  PUBLISH_COMPLETED,  CERTIFY_INPROGRESS,  CERTIFY_FAILED, CERTIFY_COMPLETED, DEPRECATE_INPROGRESS,  DEPRECATE_FAILED, DEPRECATE_COMPLETED, MARKDELETE_INPROGRESS, MARKDELETE_FAILED, MARKDELETE_COMPLETED.<br>**Constraints**: *Maximum Length*: `15`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]!,+\-=_:.&*%\s]+$` |

## Example (as JSON)

```json
{
  "jobId": "0c6e8560-e154-40f9-961e-28da3698436d",
  "status": "Inprogress",
  "state": "DRAFT"
}
```

