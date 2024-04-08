
# Subscribe Request

## Structure

`SubscribeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | - |
| `device_info` | [`List[QosDeviceInfo]`](../../doc/models/qos-device-info.md) | Required | - |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "deviceInfo": [
    {
      "deviceId": {
        "id": "10-digit phone number",
        "kind": "mdn"
      },
      "deviceIPv6Addr": "IPv6 address",
      "flowInfo": [
        {
          "flowServer": "[IPv6 address]:port",
          "flowDevice": "[IPv6 address]:port",
          "flowDirection": "UPLINK",
          "flowProtocol": "UDP",
          "qciOption": "Premium"
        }
      ]
    }
  ]
}
```

