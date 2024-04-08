
# Device List 7

## Structure

`DeviceList7`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | [`List[MECDeviceId]`](../../doc/models/mec-device-id.md) | Required | - |
| `ip_address` | `str` | Required | - |

## Example (as JSON)

```json
{
  "deviceIds": [
    {
      "id": "99948099913024600000",
      "kind": "iccid"
    }
  ],
  "ipAddress": "10.3.4.5"
}
```

