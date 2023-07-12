
# Device Provisioning History List Request

Request to return the provisioning history of a specified device during a specified time period.

## Structure

`DeviceProvisioningHistoryListRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | [`DeviceId`](../../doc/models/device-id.md) | Optional | An identifier for a single device. |
| `earliest` | `string` | Optional | The earliest date and time for which you want provisioning data. |
| `latest` | `string` | Optional | The last date and time for which you want provisioning data. |

## Example (as JSON)

```json
{
  "deviceId": {
    "id": "89141390780800784259",
    "kind": "iccid"
  },
  "earliest": "2015-09-16T00:00:01Z",
  "latest": "2015-09-18T00:00:01Z"
}
```

