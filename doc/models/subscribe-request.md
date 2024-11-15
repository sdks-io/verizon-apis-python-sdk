
# Subscribe Request

## Structure

`SubscribeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The numeric name of an account |
| `device_info` | [`List[DeviceInfo]`](../../doc/models/device-info.md) | Optional | An array of device identifiers (deviceId values) |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "deviceInfo": [
    {
      "deviceId": {
        "id": "id0",
        "kind": "kind8"
      },
      "deviceIPv6Addr": "deviceIPv6Addr4",
      "flowInfo": [
        {
          "flowServer": "flowServer4",
          "flowDevice": "flowDevice2",
          "flowDirection": "flowDirection6",
          "flowProtocol": "flowProtocol4",
          "qciOption": "qciOption0"
        }
      ]
    },
    {
      "deviceId": {
        "id": "id0",
        "kind": "kind8"
      },
      "deviceIPv6Addr": "deviceIPv6Addr4",
      "flowInfo": [
        {
          "flowServer": "flowServer4",
          "flowDevice": "flowDevice2",
          "flowDirection": "flowDirection6",
          "flowProtocol": "flowProtocol4",
          "qciOption": "qciOption0"
        }
      ]
    }
  ]
}
```

