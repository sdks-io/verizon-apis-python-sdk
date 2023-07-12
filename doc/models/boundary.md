
# Boundary

Deployment boundary of a service.

## Structure

`Boundary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `csp` | [`CSPCompatibilityEnum`](../../doc/models/csp-compatibility-enum.md) | Optional | Cloud service provider e.g. AWS_PUBLIC_CLOUD, AWS_WL, AWS_OUTPOST, AZURE_EDGE, AZURE_PUBLIC_CLOUD.<br>**Default**: `'AWS_WL'` |
| `region` | `string` | Optional | Boundary region e.g. US East (Ohio).<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |
| `zone_id` | `List of string` | Optional | Zones listed under a specific region.<br>**Constraints**: *Maximum Items*: `10000`, *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |

## Example (as JSON)

```json
{
  "csp": "AWS_WL",
  "region": "US East (Ohio)",
  "zoneId": [
    "rds.us-east-1.amazonaws.com",
    "rds.us-east-2.amazonaws.com"
  ]
}
```

