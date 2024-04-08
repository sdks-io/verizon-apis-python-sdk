
# Add Devices Result

Contains the device identifiers and a success or failure response for each device in the request.

## Structure

`AddDevicesResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | [`List[DeviceId]`](../../doc/models/device-id.md) | Optional | Identifiers for the device. |
| `response` | `str` | Optional | The success message or error message for the current device. |

## Example (as JSON)

```json
{
  "deviceIds": [
    {
      "id": "89148000000800784259",
      "kind": "iccid"
    }
  ],
  "response": "Success"
}
```

