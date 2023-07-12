
# Advance Configuration

## Structure

`AdvanceConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_role_arn` | `string` | Optional | - |
| `service_role_permission_boundary` | `string` | Optional | - |
| `enable_proxy` | `bool` | Optional | **Default**: `False` |
| `http_proxy` | `string` | Optional | - |
| `https_proxy` | `string` | Optional | - |
| `no_proxy` | `string` | Optional | - |
| `proxy_root_ca` | `string` | Optional | - |
| `enable_tls_traffic` | `bool` | Optional | **Default**: `False` |
| `enable_auto_approve` | `bool` | Optional | **Default**: `False` |
| `enable_multi_master` | `bool` | Optional | **Default**: `False` |
| `enable_dedicated_master` | `bool` | Optional | **Default**: `False` |

## Example (as JSON)

```json
{
  "enableProxy": false,
  "enableTlsTraffic": false,
  "enableAutoApprove": false,
  "enableMultiMaster": false,
  "enableDedicatedMaster": false,
  "serviceRoleArn": "serviceRoleArn4",
  "serviceRolePermissionBoundary": "serviceRolePermissionBoundary2",
  "httpProxy": "httpProxy8",
  "httpsProxy": "httpsProxy8"
}
```

