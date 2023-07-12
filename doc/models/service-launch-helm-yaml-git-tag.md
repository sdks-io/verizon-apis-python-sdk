
# Service Launch Helm Yaml Git Tag

## Structure

`ServiceLaunchHelmYamlGitTag`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tag_name` | `string` | Optional | - |
| `values_yaml_paths` | `List of string` | Optional | **Constraints**: *Maximum Items*: `100` |

## Example (as JSON)

```json
{
  "tagName": "mec_vz_helm_git",
  "valuesYamlPaths": [
    "/home/helmchart"
  ]
}
```

