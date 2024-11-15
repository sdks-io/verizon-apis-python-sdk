
# Search Device by Property Response List

A success response includes an array of all matching devices.

## Structure

`SearchDeviceByPropertyResponseList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_property` | [`List[SearchDeviceByPropertyResponse]`](../../doc/models/search-device-by-property-response.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example (as JSON)

```json
{
  "DeviceProperty": [
    {
      "billingaccountid": "billingaccountid4",
      "createdon": "createdon6",
      "eventretention": "eventretention2",
      "fields": {
        "item": {
          "acceleration": {
            "x": "x6",
            "y": "y4",
            "z": "z6"
          },
          "battery": "battery0",
          "humidity": "humidity4",
          "light": "light6",
          "pressure": "pressure2"
        }
      },
      "iccid": "iccid4"
    },
    {
      "billingaccountid": "billingaccountid4",
      "createdon": "createdon6",
      "eventretention": "eventretention2",
      "fields": {
        "item": {
          "acceleration": {
            "x": "x6",
            "y": "y4",
            "z": "z6"
          },
          "battery": "battery0",
          "humidity": "humidity4",
          "light": "light6",
          "pressure": "pressure2"
        }
      },
      "iccid": "iccid4"
    }
  ]
}
```

