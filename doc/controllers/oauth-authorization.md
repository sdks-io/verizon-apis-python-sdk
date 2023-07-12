# OAuth Authorization

```python
oauth_authorization_controller = client.oauth_authorization
```

## Class Name

`OauthAuthorizationController`


# Request Token

Create a new OAuth 2 token.

:information_source: **Note** This endpoint does not require authentication.

```python
def request_token(self,
                 authorization,
                 scope=None,
                 _optional_form_parameters=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization` | `string` | Header, Required | Authorization header in Basic auth format |
| `scope` | `string` | Form, Optional | Requested scopes as a space-delimited list. |
| `_optional_form_parameters` | `array` | Optional | Pass additional field parameters. |

## Response Type

[`OauthToken`](../../doc/models/oauth-token.md)

## Example Usage

```python
authorization = 'Authorization8'

_optional_form_parameters = {
    "key0": 'additionalFieldParams9'
}

result = oauth_authorization_controller.request_token(
    authorization,
    _optional_form_parameters
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | OAuth 2 provider returned an error. | [`OauthProviderException`](../../doc/models/oauth-provider-exception.md) |
| 401 | OAuth 2 provider says client authentication failed. | [`OauthProviderException`](../../doc/models/oauth-provider-exception.md) |

