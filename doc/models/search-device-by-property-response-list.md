
# Search Device by Property Response List

A success response includes an array of all matching devices.

## Structure

`SearchDeviceByPropertyResponseList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_property` | [`List of SearchDeviceByPropertyResponse`](../../doc/models/search-device-by-property-response.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example (as JSON)

```json
{
  "DeviceProperty": [
    {
      "billingaccountid": "billingaccountid0",
      "createdon": "createdon8",
      "eventretention": "eventretention2",
      "fields": {
        "item": {
          "acceleration": {
            "x": "x0",
            "y": "y8",
            "z": "z0"
          },
          "battery": "battery2",
          "humidity": "humidity6",
          "light": "light8",
          "pressure": "pressure4"
        }
      },
      "iccid": "iccid0"
    }
  ]
}
```

