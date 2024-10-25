
# Change PWN Device Ipaddress Request

## Structure

`ChangePWNDeviceIpaddressRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | - |
| `device_list` | [`List[DeviceListIP]`](../../doc/models/device-list-ip.md) | Required | - |

## Example (as JSON)

```json
{
  "accountName": "0342351414-00001",
  "deviceList": [
    {
      "deviceIds": [
        {
          "id": "99948099913024600000",
          "kind": "iccid"
        }
      ],
      "ipAddress": "10.3.4.5"
    },
    {
      "deviceIds": [
        {
          "id": "999480500019111000001",
          "kind": "iccid"
        }
      ],
      "ipAddress": "10.4.5.7"
    }
  ]
}
```

