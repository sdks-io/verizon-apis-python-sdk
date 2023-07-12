
# Workload

Workload attribute of a service.

## Structure

`Workload`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The auto-generated Id of the workload.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `name` | `string` | Required | Name of the workload needs to be deployed.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `description` | `string` | Optional | A brief workload description.<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |
| `package_type` | [`ServiceDependencyPackageTypeEnum`](../../doc/models/service-dependency-package-type-enum.md) | Optional | Deployment package type.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `upload_type` | [`UploadTypeEnum`](../../doc/models/upload-type-enum.md) | Optional | Allowed values are: GIT files (PULL_FROM_REPO), MANUAL_UPLOAD.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `repository_type` | [`WorkloadRepositoryTypeEnum`](../../doc/models/workload-repository-type-enum.md) | Optional | Repository types allowed: GIT/HELM.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `repository_id` | `string` | Optional | In case of 'Pull files from my repository', The user can provide the existing repositoryID.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `repository` | [`Repository`](../../doc/models/repository.md) | Optional | Users can create a repository to maintain service artifacts. Repository would be either a Git or HELM repository. |
| `files` | `List of string` | Optional | Files which are being generated.<br>**Constraints**: *Maximum Items*: `10000`, *Maximum Length*: `10000`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]!,+\-=_:.&*%\s]+$` |
| `revision_type` | [`WorkloadRevisionTypeEnum`](../../doc/models/workload-revision-type-enum.md) | Optional | Revision type can be a BRANCH or TAG.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `helm_git_branch` | [`ServiceOnboardingHelmGitBranch`](../../doc/models/service-onboarding-helm-git-branch.md) | Optional | - |
| `helm_git_tag` | [`ServiceOnboardingHelmGitTag`](../../doc/models/service-onboarding-helm-git-tag.md) | Optional | - |
| `helm_yaml_git_tag` | [`ServiceOnboardingHelmYamlGitTag`](../../doc/models/service-onboarding-helm-yaml-git-tag.md) | Optional | - |
| `helm_helmrepo` | [`ServiceOnboardingHelmHelmrepo`](../../doc/models/service-onboarding-helm-helmrepo.md) | Optional | - |
| `yaml_git_branch` | [`ServiceOnboardingYamlGitBranch`](../../doc/models/service-onboarding-yaml-git-branch.md) | Optional | - |
| `terraform_git_branch` | [`ServiceOnboardingTerraformGitBranch`](../../doc/models/service-onboarding-terraform-git-branch.md) | Optional | - |
| `terraform_git_tag` | [`ServiceOnboardingTerraformGitTag`](../../doc/models/service-onboarding-terraform-git-tag.md) | Optional | - |
| `created_date` | `datetime` | Optional | The date on which the workload is created. |
| `last_modified_dte` | `datetime` | Optional | The date when the created workload was last modified. |
| `created_by` | `string` | Optional | Identity of the user who created the workload.<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |
| `updated_by` | `string` | Optional | Identity of the user who updated the workload.<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |

## Example (as JSON)

```json
{
  "description": "MEC SD Workload.",
  "packageType": "HELM",
  "helmHelmrepo": {
    "helmChartName": "mongodb",
    "helmChartVersion": "12.1.10"
  },
  "name": "dev-api-demo-repo",
  "repositoryType": "HELM",
  "uploadType": "PULL_FROM_REPO",
  "id": "id0"
}
```

