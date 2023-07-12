
# Service Launch Yaml Git Branch

## Structure

`ServiceLaunchYamlGitBranch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `branch_name` | `string` | Optional | - |
| `values_yaml_paths` | `List of string` | Optional | **Constraints**: *Maximum Items*: `100` |

## Example (as JSON)

```json
{
  "valuesYamlPaths": [
    "/home/helmchart"
  ],
  "branchName": "branchName2"
}
```

