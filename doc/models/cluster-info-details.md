
# Cluster Info Details

Details of the cluster information.

## Structure

`ClusterInfoDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cluster_name` | `string` | Required | Name of the cluster to be used.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `namespace` | `string` | Required | Namespace name inside cluster.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |

## Example (as JSON)

```json
{
  "clusterName": "ctc-1",
  "namespace": "default"
}
```

