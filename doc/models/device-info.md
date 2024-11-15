
# Device Info

## Structure

`DeviceInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | [`DeviceId`](../../doc/models/device-id.md) | Optional | device identifiers consisting of an ID value and what that value represents (kind) |
| `device_i_pv_6_addr` | `str` | Optional | the IPv6 IP address of the device |
| `flow_info` | [`List[FlowInfo]`](../../doc/models/flow-info.md) | Optional | The details of the data connection |

## Example (as JSON)

```json
{
  "deviceIPv6Addr": "IPv6 address",
  "deviceId": {
    "id": "id0",
    "kind": "kind8"
  },
  "flowInfo": [
    {
      "flowServer": "flowServer4",
      "flowDevice": "flowDevice2",
      "flowDirection": "flowDirection6",
      "flowProtocol": "flowProtocol4",
      "qciOption": "qciOption0"
    },
    {
      "flowServer": "flowServer4",
      "flowDevice": "flowDevice2",
      "flowDirection": "flowDirection6",
      "flowProtocol": "flowProtocol4",
      "qciOption": "qciOption0"
    }
  ]
}
```

