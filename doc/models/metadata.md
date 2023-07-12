
# Metadata

## Structure

`Metadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | - |
| `display_name` | `string` | Optional | - |
| `created_at` | `string` | Optional | - |
| `modified_at` | `string` | Optional | - |
| `labels` | [`MetadataLabel`](../../doc/models/metadata-label.md) | Optional | - |
| `annotations` | [`MetadataAnnotation`](../../doc/models/metadata-annotation.md) | Optional | - |
| `organization_id` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `partner_id` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `project_id` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `id` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "name": "name0",
  "displayName": "displayName2",
  "createdAt": "createdAt6",
  "modifiedAt": "modifiedAt6",
  "labels": {
    "alpha.rafay.io/cluster-name": "alpha.rafay.io/cluster-name4",
    "alpha.rafay.io/instance-id": "alpha.rafay.io/instance-id6",
    "alpha.rafay.io/nodegroup-name": "alpha.rafay.io/nodegroup-name2",
    "beta.kubernetes.io/arch": "beta.kubernetes.io/arch6",
    "beta.kubernetes.io/instance-type": "beta.kubernetes.io/instance-type6"
  }
}
```

