
# Bullseye Service Result

Status of Hyper Precise Location on the device.

## Structure

`BullseyeServiceResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `string` | Optional | The account the device belongs to. |
| `device_list` | [`List of DeviceServiceInformation`](../../doc/models/device-service-information.md) | Optional | List of devices. |
| `response_type` | [`ApiResponseCode`](../../doc/models/api-response-code.md) | Optional | ResponseCode and/or a message indicating success or failure of the request. |

## Example (as JSON)

```json
{
  "accountNumber": "0844021539-00001",
  "deviceList": [
    {
      "imei": "709312034493372",
      "BullseyeEnable": true,
      "responseType": {
        "responseCode": "INVALID_ACCESS",
        "message": "message4"
      }
    }
  ],
  "responseType": {
    "responseCode": "INTERNAL_ERROR",
    "message": "message8"
  }
}
```

