
# Compatibility

Compatibility would have the attribute CSP which is Cloud service provider e.g. AWS_PUBLIC_CLOUD, AWS_WL, AWS_OUTPOST, AZURE_EDGE, AZURE_PUBLIC_CLOUD.

## Structure

`Compatibility`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `csp` | [`CSPCompatibilityEnum`](../../doc/models/csp-compatibility-enum.md) | Optional | Cloud service provider e.g. AWS_PUBLIC_CLOUD, AWS_WL, AWS_OUTPOST, AZURE_EDGE, AZURE_PUBLIC_CLOUD.<br>**Default**: `'AWS_WL'` |

## Example (as JSON)

```json
{
  "csp": "AWS_WL"
}
```

