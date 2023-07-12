
# ERN Cluster

## Structure

`ERNCluster`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Optional | - |
| `name` | `string` | Optional | User display name.<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `name_space` | [`List of NamespaceIdItem`](../../doc/models/namespace-id-item.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": "eda2cb4e-50ef-4ae8-b304-7d2f0f7a21c1",
  "name": "us-south",
  "nameSpace": [
    {
      "id": "eda2cb4e-50ef-4ae8-b304-7d2f0f7a21c1",
      "name": "default"
    },
    {
      "id": "f8dkcb4e-50ef-4ae8-b304-7d2f0f7a21c1",
      "name": "default"
    }
  ]
}
```

