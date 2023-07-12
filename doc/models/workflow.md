
# Workflow

Workflow attribute of a service.

## Structure

`Workflow`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Required | The service version workflow name.<br>**Constraints**: *Maximum Length*: `63`, *Pattern*: `^[a-z0-9-_.]+$` |
| `version` | `string` | Required | The service version workflow value.<br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9\.]+$` |
| `id` | `string` | Optional | Auto-generated UUID for each workdflow triggered.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `mtype` | [`WorkflowTypeEnum`](../../doc/models/workflow-type-enum.md) | Optional | Service type e.g. Installation, Operations, Custom.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `installation_wf` | [`InstallationWf`](../../doc/models/installation-wf.md) | Optional | `installationWf` attribute of a service. |
| `operations_wf` | [`OperationsWf`](../../doc/models/operations-wf.md) | Optional | `operationsWf` attribute of a service. |
| `custom_wf` | [`CustomWf`](../../doc/models/custom-wf.md) | Optional | `customWf` attribute of a service. |
| `files` | `List of string` | Optional | Files which are being generated.<br>**Constraints**: *Maximum Items*: `10000`, *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]!,+\-=_:.&*%\s]+$` |
| `status` | `string` | Optional | Status of the workflow.<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s\/]+$` |
| `created_date` | `datetime` | Optional | The date on which the workflow is created. |
| `last_modified_date` | `datetime` | Optional | The date when the created workflow was last modified. |
| `created_by` | `string` | Optional | Identity of the user who created the workflow.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `updated_by` | `string` | Optional | Identity of the user who updated the workflow.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |

## Example (as JSON)

```json
{
  "name": "camera_add_on",
  "version": "1.0.0",
  "id": "2e13f3a1-287f-4c63-9218-d026bf1bda32",
  "type": "INSTALLATION",
  "installationWf": {
    "hookType": "PRE_INSTALLATION",
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
    "path": "workflows/intallationwf/workflowname"
  },
  "operationsWf": {
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
  },
  "customWf": {
    "eventName": "CAMERA_ADD",
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
    "path": "workflows/customwf/workflowname"
  },
  "files": [
    "filestring"
  ],
  "status": "new",
  "createdDate": "2006-01-02T15:04:05Z",
  "lastModifiedDate": "2006-01-02T15:04:05Z",
  "createdBy": "User",
  "updatedBy": "User"
}
```

