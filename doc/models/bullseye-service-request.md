
# Bullseye Service Request

Account number and list of devices.

## Structure

`BullseyeServiceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_list` | [`List[DeviceServiceRequest]`](../../doc/models/device-service-request.md) | Required | A list of devices. |
| `account_number` | `str` | Required | A unique identifier for an account. |

## Example (as JSON)

```json
{
  "deviceList": [
    {
      "imei": "354658090356210",
      "BullseyeEnable": true
    }
  ],
  "accountNumber": "0242080353-00001"
}
```

