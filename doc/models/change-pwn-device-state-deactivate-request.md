
# Change PWN Device State Deactivate Request

## Structure

`ChangePWNDeviceStateDeactivateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | - |
| `device_list` | [`List[PWNDeviceList]`](../../doc/models/pwn-device-list.md) | Required | - |

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
      ]
    }
  ]
}
```

