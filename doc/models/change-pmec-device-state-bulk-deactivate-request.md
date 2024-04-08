
# Change Pmec Device State Bulk Deactivate Request

## Structure

`ChangePmecDeviceStateBulkDeactivateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | - |
| `device_list` | [`List[MECDeviceList]`](../../doc/models/mec-device-list.md) | Required | - |

## Example (as JSON)

```json
{
  "accountName": "0342351414-00001",
  "deviceList": [
    {
      "deviceIds": [
        {
          "id": "99948099913031600000",
          "kind": "iccid"
        }
      ]
    },
    {
      "deviceIds": [
        {
          "id": "99948099913031700000",
          "kind": "iccid"
        }
      ]
    }
  ]
}
```

