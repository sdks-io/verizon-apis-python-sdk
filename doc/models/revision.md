
# Revision

## Structure

`Revision`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `string` | Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `additional_params` | [`List of EdgeServiceLaunchParams`](../../doc/models/edge-service-launch-params.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example (as JSON)

```json
{
  "additionalParams": [],
  "version": "2.3.4"
}
```

