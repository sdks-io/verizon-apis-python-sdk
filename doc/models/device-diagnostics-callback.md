
# Device Diagnostics Callback

Callback information of an existing diagnostics subscription.

## Structure

`DeviceDiagnosticsCallback`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | The name of the billing account for which callback messages will be sent. Format: "##########-#####". |
| `service_name` | `str` | Required | The name of the callback service, which identifies the type and format of messages that will be sent to the registered URL. |
| `endpoint` | `str` | Required | The URL for your web server. |
| `created_on` | `datetime` | Required | The date and time of when this request was created. |
| `http_headers` | `object` | Optional | Your HTTP headers. |

## Example (as JSON)

```json
{
  "accountName": "TestQAAccount",
  "serviceName": "Diagnostics",
  "endpoint": "https://yourwebsite.com",
  "createdOn": "2019-09-07T23:57:53.292Z",
  "httpHeaders": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

