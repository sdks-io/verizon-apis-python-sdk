
# Qos Device Info

## Structure

`QosDeviceInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | [`QosDeviceId`](../../doc/models/qos-device-id.md) | Required | - |
| `device_i_pv_6_addr` | `str` | Optional | - |
| `flow_info` | [`List[FlowInfo]`](../../doc/models/flow-info.md) | Required | - |

## Example (as JSON)

```json
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
```

