
# Delete Devices Request

Request to delete a device request.

## Structure

`DeleteDevicesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Optional | The Verizon billing account that the device group belongs to. An account name is usually numeric, and must include any leading zeros. |
| `devices_to_delete` | [`List of AccountDeviceList`](../../doc/models/account-device-list.md) | Optional | A list of up to 100 devices that you want to delete, specified by device identifier. You only need to provide one identifier per device. |

## Example (as JSON)

```json
{
  "devicesToDelete": [
    {
      "deviceIds": [
        {
          "id": "09005470263",
          "kind": "esn"
        }
      ]
    },
    {
      "deviceIds": [
        {
          "id": "85000022411113460014",
          "kind": "iccid"
        }
      ]
    },
    {
      "deviceIds": [
        {
          "id": "85000022412313460016",
          "kind": "iccid"
        }
      ]
    }
  ],
  "accountName": "accountName4"
}
```

