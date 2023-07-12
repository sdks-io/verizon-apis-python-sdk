
# Node Configuration

## Structure

`NodeConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | Name of the nodeGroup. |
| `is_wavelength_zone` | `bool` | Optional | **Default**: `False` |
| `is_managed_node_group` | `bool` | Optional | **Default**: `False` |
| `is_spot_instance_needed` | `bool` | Optional | **Default**: `False` |
| `end_point_access_type` | [`EndPointAccessTypeEnum`](../../doc/models/end-point-access-type-enum.md) | Optional | **Default**: `'private'` |
| `instance_type` | `string` | Optional | **Default**: `'m5.xlarge'` |
| `nodes` | `int` | Optional | **Default**: `2`<br>**Constraints**: `>= 0`, `<= 1024` |
| `nodes_min` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `nodes_max` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `node_volume_type` | `string` | Optional | - |
| `subnet_cidr_block` | `string` | Optional | - |
| `node_ami_family` | `string` | Optional | **Default**: `'AmazonLinux2'` |
| `node_volume_size` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `key_name` | `string` | Optional | - |
| `max_pod_per_node` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `use_volume_encryption` | `bool` | Optional | **Default**: `True` |
| `node_private_networking` | `bool` | Optional | **Default**: `False` |
| `instance_profile_arn` | `string` | Optional | - |
| `instance_role_arn` | `string` | Optional | - |
| `instance_role_permission_boundary` | `string` | Optional | - |
| `security_group_ids` | [`List of IdList`](../../doc/models/id-list.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `availability_zone_ids` | [`List of IdList`](../../doc/models/id-list.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `labels` | [`NodeConfigurationLabel`](../../doc/models/node-configuration-label.md) | Optional | - |
| `tags` | [`NodeConfigurationTag`](../../doc/models/node-configuration-tag.md) | Optional | - |
| `auto_create_service_roles` | `bool` | Optional | **Default**: `True` |
| `enable_full_access_to_ecr` | `bool` | Optional | - |
| `enable_asg_access` | `bool` | Optional | - |
| `enable_dns_access` | `bool` | Optional | - |
| `enable_app_mesh_access` | `bool` | Optional | - |
| `enable_alb_access` | `bool` | Optional | - |
| `enable_efs_access` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "autoCreateServiceRoles": true,
  "enableAlbAccess": true,
  "enableAppMeshAccess": true,
  "enableAsgAccess": true,
  "enableDnsAccess": true,
  "enableEfsAccess": true,
  "enableFullAccessToEcr": true,
  "endPointAccessType": "private",
  "instanceType": "m5.xlarge",
  "isManagedNodeGroup": false,
  "isSpotInstanceNeeded": false,
  "isWavelengthZone": false,
  "labels": {},
  "name": "ng-22",
  "nodeAmiFamily": "AmazonLinux2",
  "nodePrivateNetworking": false,
  "nodeVolumeSize": 80,
  "nodeVolumeType": "gp3",
  "nodes": 2,
  "nodesMax": 2,
  "nodesMin": 2,
  "tags": {},
  "useVolumeEncryption": true
}
```

