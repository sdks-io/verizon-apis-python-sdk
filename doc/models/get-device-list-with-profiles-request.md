
# Get Device List With Profiles Request

## Structure

`GetDeviceListWithProfilesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9\-]{3,32}$` |
| `provisioning_status_filter` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `profile_status_filter` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `carrier_name_filter` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `device_filter` | [`List[GIODeviceId]`](../../doc/models/gio-device-id.md) | Optional | **Constraints**: *Maximum Items*: `50` |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "provisioningStatusFilter": "ACTIVE",
  "profileStatusFilter": "UNKNOWN",
  "carrierNameFilter": "carrierNameFilter2",
  "deviceFilter": [
    {
      "kind": "kind2",
      "id": "id4"
    }
  ]
}
```

