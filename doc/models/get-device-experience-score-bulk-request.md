
# Get Device Experience Score Bulk Request

Get device experience score bulk request.

## Structure

`GetDeviceExperienceScoreBulkRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account name.<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9-]{3,32}$` |
| `device_list` | [`List[DeviceIdentifier]`](../../doc/models/device-identifier.md) | Required | **Constraints**: *Maximum Items*: `100` |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "deviceList": [
    {
      "kind": "iccid",
      "id": "01234567899876543210",
      "mdn": "0123456789"
    }
  ]
}
```

