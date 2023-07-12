
# Aggregate Usage Error

Error reported by a device.

## Structure

`AggregateUsageError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `imei` | `string` | Optional | International Mobile Equipment Identifier. This is the ID of the device reporting errors. |
| `error_message` | `string` | Optional | A general error message. |
| `error_response` | [`IErrorMessage`](../../doc/models/i-error-message.md) | Optional | Error message. |

## Example (as JSON)

```json
{
  "errorResponse": {
    "httpStatusCode": "200 OK",
    "errorCode": "INVALID_ACCESS",
    "errorMessage": "errorMessage4",
    "detailErrorMessage": "detailErrorMessage6"
  },
  "imei": "imei6",
  "errorMessage": "errorMessage8"
}
```

