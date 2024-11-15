
# I Error Message

Error message.

## Structure

`IErrorMessage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | [`ErrorResponseCodeEnum`](../../doc/models/error-response-code-enum.md) | Optional | Error Code. |
| `error_message` | `str` | Optional | Details and additional information about the error code. |
| `http_status_code` | [`HttpStatusCodeEnum`](../../doc/models/http-status-code-enum.md) | Optional | HTML error code and description. |
| `detail_error_message` | `str` | Optional | More detail and information about the HTML error code. |

## Example (as JSON)

```json
{
  "httpStatusCode": "200 OK",
  "errorCode": "INVALID_ACCESS",
  "errorMessage": "errorMessage4",
  "detailErrorMessage": "detailErrorMessage6"
}
```

