
# Account Device List Filter

Filter for a list of devices.

## Structure

`AccountDeviceListFilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_identifier_filters` | [`List[DeviceIdSearch]`](../../doc/models/device-id-search.md) | Required | Specify the kind of the device identifier, the type of match, and the string that you want to match. |

## Example (as JSON)

```json
{
  "deviceIdentifierFilters": [
    {
      "kind": "iccid",
      "contains": "4259",
      "startswith": "startswith8",
      "endswith": "endswith0"
    }
  ]
}
```

