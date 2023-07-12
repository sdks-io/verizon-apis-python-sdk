
# Device Group

Returns a list of all device groups in a specified account.

## Structure

`DeviceGroup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `string` | Optional | The description of the device group. |
| `extended_attributes` | [`List of CustomFields`](../../doc/models/custom-fields.md) | Optional | Any extended attributes for the device group, as Key and Value pairs. |
| `is_default_group` | `bool` | Optional | Identifies the default device group. |
| `name` | `string` | Optional | The name of the device group. |

## Example (as JSON)

```json
{
  "name": "Unassigned Devices",
  "description": "All devices that are not in another device group.",
  "isDefaultGroup": true,
  "extendedAttributes": []
}
```

