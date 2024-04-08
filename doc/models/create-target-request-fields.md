
# Create Target Request Fields

## Structure

`CreateTargetRequestFields`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `httpheaders` | [`FieldsHttpHeaders`](../../doc/models/fields-http-headers.md) | Optional | - |
| `devicetypes` | `List[str]` | Optional | List of device types. |

## Example (as JSON)

```json
{
  "httpheaders": {
    "Authorization": "SharedAccessSignature sr=d1f9b6bf-1380-41f6-b757-d9805e48392b&sig=EF5tnXClw3MWkb84OkIOUhMH%2FaS1DRD2nXT69QR8RD8%3D&skn=TSCCtoken&se=1648827260410"
  },
  "devicetypes": [
    "cHeAssetTracker",
    "cHeAssetTrackerV2",
    "tgAssetTracker",
    "tgAssetTrackerV2"
  ]
}
```

