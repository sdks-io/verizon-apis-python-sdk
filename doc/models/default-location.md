
# Default Location

Default location where service needs to be deployed.

## Structure

`DefaultLocation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `region` | `string` | Optional | CSP region where service needs to be deployed.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |
| `zone` | `string` | Optional | Zone within a region where service needs to be deployed.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |

## Example (as JSON)

```json
{
  "region": "us-west",
  "zone": "us-west-2-wl1-den-wlz-1"
}
```

