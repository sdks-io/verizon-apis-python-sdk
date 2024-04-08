
# Retrieve Monitors Request

## Structure

`RetrieveMonitorsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | The name of a billing account. |
| `devices` | [`List[AccountDeviceList]`](../../doc/models/account-device-list.md) | Required | The devices for which you want to restore service, specified by device identifier. |
| `monitor_type` | `str` | Optional | The name of a billing account. |

## Example (as JSON)

```json
{
  "accountName": "0868924207-00001",
  "devices": [
    {
      "deviceIds": [
        {
          "id": "89148000000800139708",
          "kind": "iccid"
        }
      ],
      "ipAddress": "ipAddress4"
    }
  ],
  "monitorType": "monitorType"
}
```

