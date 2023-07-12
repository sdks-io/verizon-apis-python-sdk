
# Dependent Service

This service is dependent on other service.

## Structure

`DependentService`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | Name of the service needs to be deployed.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `version` | `string` | Optional | Version of the service being used.<br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9\.]+$` |
| `status` | [`ServiceStatusEnum`](../../doc/models/service-status-enum.md) | Optional | Can have any value as - DRAFT_INPROGRESS, DRAFT_COMPLETE, DESIGN_INPROGRESS, DESIGN_FAILED, DESIGN_COMPLETED, VALIDATION_INPROGRESS,  VALIDATION_FAILED, VALIDATION_COMPLETED, TESTING_INPROGRESS, TESTING_FAILED, TESTING_COMPLETED, READY_TO_USE_INPROGRESS, READY_TO_USE_FAILED, READY_TO_USE_COMPLETED, READY_TO_PRIVATE_USE_INPROGRESS, READY_TO_PRIVATE_USE_FAILED, READY_TO_PRIVATE_USE_COMPLETED,  PUBLISH_INPROGRESS,  PUBLISH_FAILED,  PUBLISH_COMPLETED,  CERTIFY_INPROGRESS,  CERTIFY_FAILED, CERTIFY_COMPLETED, DEPRECATE_INPROGRESS,  DEPRECATE_FAILED, DEPRECATE_COMPLETED, MARKDELETE_INPROGRESS, MARKDELETE_FAILED, MARKDELETE_COMPLETED. |
| `mtype` | [`DependentServicesTypeEnum`](../../doc/models/dependent-services-type-enum.md) | Optional | List of dependent services type. |
| `created_by` | `string` | Optional | User who created the service. Part of response only.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `last_modified_by` | `string` | Optional | User who last modified the service. Part of response only.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `instances` | `int` | Optional | Instances of a service.<br>**Constraints**: `<= 1024` |

## Example (as JSON)

```json
{
  "name": "MyService",
  "version": "1.0.0",
  "status": "DRAFT_INPROGRESS",
  "type": "MY_SERVICE",
  "createdBy": "User",
  "lastModifiedBy": "User",
  "Instances": 10
}
```

