
# Node

## Structure

`Node`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | - |
| `created_at` | `string` | Optional | - |
| `modified_at` | `string` | Optional | - |
| `node_id` | `string` | Optional | - |
| `private_ip` | `string` | Optional | - |
| `num_cores` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `total_memory` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `cluster_id` | `string` | Optional | - |
| `roles` | `List of string` | Optional | **Constraints**: *Maximum Items*: `100` |
| `id` | `string` | Optional | - |
| `approved` | `bool` | Optional | - |
| `status` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "num_cores": 8,
  "total_memory": 512,
  "approved": true,
  "name": "name0",
  "created_at": "created_at2",
  "modified_at": "modified_at6",
  "node_id": "node_id2",
  "private_ip": "private_ip0"
}
```

