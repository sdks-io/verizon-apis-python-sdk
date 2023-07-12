
# Cluster Version Info

## Structure

`ClusterVersionInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cluster_id` | `string` | Optional | - |
| `kube_version` | `string` | Optional | - |
| `organization_id` | `string` | Optional | - |
| `partner_id` | `string` | Optional | - |
| `created_at` | `string` | Optional | - |
| `modified_at` | `string` | Optional | - |
| `id` | `string` | Optional | - |
| `behind_latest_by` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |

## Example (as JSON)

```json
{
  "cluster_id": "cluster_id4",
  "kube_version": "kube_version4",
  "organization_id": "organization_id0",
  "partner_id": "partner_id2",
  "created_at": "created_at2"
}
```

