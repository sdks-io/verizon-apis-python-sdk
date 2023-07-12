
# Operations Wf

`operationsWf` attribute of a service.

## Structure

`OperationsWf`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_type` | [`EventTypeEnum`](../../doc/models/event-type-enum.md) | Optional | Workflow event type. Ex: BACKUP, RESTORE, MOVE, SUSPEND, STOP, AUTOSCALE, DEPRECATE.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `upload_type` | [`UploadTypeEnum`](../../doc/models/upload-type-enum.md) | Optional | Allowed values are: GIT files (PULL_FROM_REPO), MANUAL_UPLOAD.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `repository_id` | `string` | Optional | Repository ID of an existing repository.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `repository` | [`Repository`](../../doc/models/repository.md) | Optional | Users can create a repository to maintain service artifacts. Repository would be either a Git or HELM repository. |
| `source_code_type` | [`SourceCodeTypeEnum`](../../doc/models/source-code-type-enum.md) | Optional | Source code type can be JAVA or GO.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `revision_type` | [`WorkloadRevisionTypeEnum`](../../doc/models/workload-revision-type-enum.md) | Optional | Revision type can be a BRANCH or TAG.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `name` | `string` | Optional | Branch or tag name.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `path` | `string` | Optional | The workflow path.<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s\/]+$` |

## Example (as JSON)

```json
{
  "eventType": "BACKUP",
  "uploadType": "PULL_FROM_REPO",
  "repositoryId": "2e13f3a1-287f-4c63-9218-d026bf1bda32",
  "repository": {
    "id": "2e13f3a1-287f-4c63-9218-d026bf1bda32",
    "name": "myRepo",
    "description": "My organization repository.",
    "type": "Git",
    "tag": "myTag",
    "endpoint": "https://charts.bitnami.com/bitnami",
    "reacheability": "Internet",
    "CACertificate": "G2",
    "Agents": [
      "Verizon"
    ],
    "sslDisabled": false,
    "isValidated": true,
    "validationStatus": "CREDENTIAL_VALIDATION_SUCCESS",
    "credentialsType": "UserPassCredentials",
    "credentials": {
      "name": "Adam123",
      "password": "password"
    },
    "sshKey": "MIIBpjBABgkqhkiG9",
    "lastValidatedDate": "2006-01-02T15:04:05Z",
    "createdDate": "2006-01-02T15:04:05Z",
    "lastModifiedDate": "2006-01-02T15:04:05Z",
    "createdBy": "User",
    "updatedBy": "User",
    "isDeleted": false
  },
  "sourceCodeType": "JAVA",
  "revisionType": "BRANCH",
  "name": "gitbranch",
  "path": "workflows/operationswf/workflowname"
}
```

