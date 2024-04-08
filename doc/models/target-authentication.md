
# Target Authentication

OAuth 2 token and refresh token for TS to stream events to Target.

## Structure

`TargetAuthentication`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TargetAuthenticationBody`](../../doc/models/target-authentication-body.md) | Optional | - |
| `version` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "body": {
    "grant_type": "refresh_token",
    "refresh_token": "qfeqVjZTYzMmUtZWMzZqfq4ZDUtNzFhZWVkYTlmMjk1",
    "headers": {
      "Authorization": "Basic RGFrqewfq2xpZW50QXBwVjI6YzM5YjqfqmI2LWI2MWQtNDRlZTQ5MmM1YTRk",
      "Content-Type": "application/x-www-form-urlencoded"
    },
    "host": {
      "hostandpath": "https:// myhost.com:1825"
    },
    "scope": "scope6"
  },
  "version": "1.0"
}
```

