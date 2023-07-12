
# Service File

Response to get file of a service.

## Structure

`ServiceFile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | System generated unique UUID.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `service_name` | `string` | Optional | Service name to which the file is going to be associated.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `service_version` | `string` | Optional | Version of the service being used.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9\.]+$` |
| `file` | `string` | Optional | File which is to be uploaded should be provided in formData.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9.\-_]+$` |
| `category_name` | `string` | Optional | Name of the workload being used in the service.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `category_version` | `string` | Optional | Version of the workload being used in the service.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9.\-_]+$` |
| `category_type` | `string` | Optional | Type of the workload being used in the service eg: use WORKLOAD_TGZ to upload the workload file in tgz format.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `validation_status` | `string` | Optional | Gives the success and failure response for the validation.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9-_ .]+$` |
| `created_date` | `datetime` | Optional | System captured creation date and time when tag is created. |
| `last_modified_date` | `datetime` | Optional | System captured date and time when the tag was last modified. |
| `created_by` | `string` | Optional | User information who created the tag.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `updated_by` | `string` | Optional | Last user information who made changes to tag.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |

## Example (as JSON)

```json
{
  "id": "uuid",
  "serviceName": "gst-server",
  "serviceVersion": "1.0.0",
  "file": "values.yaml",
  "categoryName": "gst-server-workload",
  "categoryVersion": "1.0.0",
  "categoryType": "WORKLOAD_VALUES",
  "validationStatus": "Validation Success",
  "createdDate": "2006-01-02T15:04:05Z",
  "lastModifiedDate": "2006-01-02T15:04:05Z",
  "createdBy": "User",
  "updatedBy": "User"
}
```

