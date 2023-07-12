
# Notification Report Request

## Structure

`NotificationReportRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Required | - |
| `request_type` | `string` | Required | - |
| `devices` | [`List of DeviceList`](../../doc/models/device-list.md) | Required | - |
| `monitor_expiration_time` | `string` | Required | - |

## Example (as JSON)

```json
{
  "accountName": "0242072320-00001",
  "requestType": "REACHABLE_FOR_DATA",
  "devices": [
    {
      "deviceIds": [
        {
          "id": "id6",
          "kind": "imei"
        },
        {
          "id": "id7",
          "kind": "eid"
        },
        {
          "id": "id8",
          "kind": "esn"
        }
      ]
    }
  ],
  "monitorExpirationTime": "2019-12-02T15:00:00-08:00Z"
}
```

