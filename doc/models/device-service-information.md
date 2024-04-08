
# Device Service Information

Device service information.

## Structure

`DeviceServiceInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response_type` | [`ApiResponseCode`](../../doc/models/api-response-code.md) | Optional | ResponseCode and/or a message indicating success or failure of the request. |
| `imei` | `str` | Required | The International Mobile Equipment Identifier of the device. |
| `bullseye_enable` | `bool` | Required | Shows if Hyper Precise is enabled (true) or disabled (false). |

## Example (as JSON)

```json
{
  "imei": "709312034493372",
  "BullseyeEnable": true,
  "responseType": {
    "responseCode": "INTERNAL_ERROR",
    "message": "message8"
  }
}
```

