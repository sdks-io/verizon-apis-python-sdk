
# CSP Profile Id Request

Request to get the Id of the CSP profile.

## Structure

`CSPProfileIdRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `csp_profile_id` | `string` | Optional | CSP Profile ID in which service will be deployed.<br>**Constraints**: *Maximum Length*: `36`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]!,+\-=_:.&*%\s]+$` |

## Example (as JSON)

```json
{
  "cspProfileId": "2e13f3a1-287f-4c63-9218-d026bf1bda32"
}
```

