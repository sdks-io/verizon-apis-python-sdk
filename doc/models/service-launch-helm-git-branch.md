
# Service Launch Helm Git Branch

## Structure

`ServiceLaunchHelmGitBranch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `branch_name` | `string` | Optional | - |
| `helm_chart_path` | `string` | Optional | - |
| `values_yaml_paths` | `List of string` | Optional | - |

## Example (as JSON)

```json
{
  "branchName": "mec_vz_helm_git",
  "helmChartPath": "/home/helmchart",
  "valuesYamlPaths": [
    "/home/helmchart"
  ]
}
```

