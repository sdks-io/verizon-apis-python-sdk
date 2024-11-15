
# Callback Registration Request

Specifies the callback service that is being subscribed to and the URL where the listening service is running.

## Structure

`CallbackRegistrationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | The name of the billing account for which callback messages will be sent. Format: "##########-#####". |
| `service_name` | `str` | Required | The name of the callback service, which identifies the type and format of messages that will be sent to the registered URL. |
| `endpoint` | `str` | Required | The URL for your web server. |
| `http_headers` | `object` | Optional | Your HTTP headers. |

## Example (as JSON)

```json
{
  "accountName": "TestQAAccount",
  "serviceName": "Diagnostics",
  "endpoint": "https://yourwebsite.com",
  "httpHeaders": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

