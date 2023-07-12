
# Edge Service Workload

## Structure

`EdgeServiceWorkload`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `name` | `string` | Required | Name of the workload needs to be deployed.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `description` | `string` | Optional | **Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |
| `package_type` | [`PackageTypeEnum`](../../doc/models/package-type-enum.md) | Optional | Deployment package type.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `upload_type` | [`WorkloadUploadTypeEnum`](../../doc/models/workload-upload-type-enum.md) | Optional | **Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `repository_type` | [`RepositoryTypeEnum`](../../doc/models/repository-type-enum.md) | Optional | **Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `repository_id` | `string` | Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `repository` | [`EdgeServiceRepository`](../../doc/models/edge-service-repository.md) | Optional | - |
| `files` | `List of string` | Optional | **Constraints**: *Maximum Items*: `10000` |
| `revision_type` | [`RevisionTypeEnum`](../../doc/models/revision-type-enum.md) | Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `helm_git_branch` | [`ServiceLaunchHelmGitBranch`](../../doc/models/service-launch-helm-git-branch.md) | Optional | - |
| `helm_git_tag` | [`ServiceLaunchHelmGitTag`](../../doc/models/service-launch-helm-git-tag.md) | Optional | - |
| `helm_yaml_git_tag` | [`ServiceLaunchHelmYamlGitTag`](../../doc/models/service-launch-helm-yaml-git-tag.md) | Optional | - |
| `helm_repo` | [`ServiceLaunchHelmRepo`](../../doc/models/service-launch-helm-repo.md) | Optional | - |
| `yaml_git_branch` | [`ServiceLaunchYamlGitBranch`](../../doc/models/service-launch-yaml-git-branch.md) | Optional | - |
| `terraform_git_branch` | [`ServiceLaunchTerraformGitBranch`](../../doc/models/service-launch-terraform-git-branch.md) | Optional | - |
| `terraform_git_tag` | [`ServiceLaunchTerraformGitTag`](../../doc/models/service-launch-terraform-git-tag.md) | Optional | - |
| `created_date` | `datetime` | Optional | - |
| `last_modified_dte` | `datetime` | Optional | - |
| `created_by` | `string` | Optional | **Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |
| `updated_by` | `string` | Optional | **Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |

## Example (as JSON)

```json
{
  "name": "MECSDWorkload",
  "id": "id0",
  "description": "description0",
  "packageType": "YAML",
  "uploadType": "PULL_FROM_REPO",
  "repositoryType": "GIT"
}
```

