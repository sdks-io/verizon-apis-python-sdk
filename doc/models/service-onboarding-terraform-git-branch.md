
# Service Onboarding Terraform Git Branch

## Structure

`ServiceOnboardingTerraformGitBranch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `branch_name` | `string` | Required | **Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s\/]+$` |
| `terraform_path` | `string` | Required | **Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s\/]+$` |

## Example (as JSON)

```json
{
  "branchName": "mec_terraform_git",
  "terraformPath": "/home/helmchart"
}
```

