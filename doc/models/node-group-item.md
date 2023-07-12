
# Node Group Item

## Structure

`NodeGroupItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | - |
| `created_at` | `string` | Optional | - |
| `modified_at` | `string` | Optional | - |
| `organization_id` | `string` | Optional | - |
| `partner_id` | `string` | Optional | - |
| `instance_type` | `string` | Optional | - |
| `edge_id` | `string` | Optional | - |
| `id` | `string` | Optional | - |
| `provision_id` | `string` | Optional | - |
| `node_type` | `string` | Optional | - |
| `nodes` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `nodes_min` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `nodes_max` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `node_volume_size` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `node_volume_type` | `string` | Optional | - |
| `node_private_networking` | `bool` | Optional | - |
| `node_zones` | `List of string` | Optional | **Constraints**: *Maximum Items*: `100` |
| `node_ami_family` | `string` | Optional | - |
| `node_labels` | [`NodeLabel`](../../doc/models/node-label.md) | Optional | - |
| `nodegroup_type` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `enable_asg_access` | `bool` | Optional | - |
| `enable_full_access_to_ecr` | `bool` | Optional | - |
| `version_info_id` | `string` | Optional | - |
| `upgrade_info_id` | `string` | Optional | - |
| `tags` | [`NodeGroupItemTag`](../../doc/models/node-group-item-tag.md) | Optional | - |
| `config_file_content` | `string` | Optional | - |
| `provision` | [`Provision`](../../doc/models/provision.md) | Optional | - |
| `version_info` | [`VersionInfo`](../../doc/models/version-info.md) | Optional | - |
| `upgrade_info` | [`UpgradeInfo`](../../doc/models/upgrade-info.md) | Optional | - |

## Example (as JSON)

```json
{
  "node_private_networking": true,
  "enable_asg_access": true,
  "enable_full_access_to_ecr": false,
  "name": "name0",
  "created_at": "created_at2",
  "modified_at": "modified_at6",
  "organization_id": "organization_id0",
  "partner_id": "partner_id2"
}
```

