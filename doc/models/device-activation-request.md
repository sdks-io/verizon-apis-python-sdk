
# Device Activation Request

Request for device status to check availability of activation.

## Structure

`DeviceActivationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Optional | The name of a billing account. |
| `devices` | [`List of AccountDeviceList`](../../doc/models/account-device-list.md) | Optional | Up to 10,000 devices that you want to move to a different account, specified by device identifier. |

## Example (as JSON)

```json
{
  "accountName": "0212345678-00001",
  "devices": [
    {
      "deviceIds": [
        {
          "kind": "meid",
          "id": "A100008385E561"
        }
      ]
    }
  ]
}
```

