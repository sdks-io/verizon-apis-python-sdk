
# Device Extended Diagnostics Result

Result for a request to obtain device extended diagnostics.

## Structure

`DeviceExtendedDiagnosticsResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `categories` | [`List[DiagnosticsCategory]`](../../doc/models/diagnostics-category.md) | Optional | The response includes various types of information about the device, grouped into categories. Each category object contains the category name and a list of Extended Attribute objects as key-value pairs. |

## Example (as JSON)

```json
{
  "categories": [
    {
      "categoryName": "Connectivity",
      "extendedAttributes": [
        {
          "key": "Connected",
          "value": "false"
        }
      ]
    }
  ]
}
```

