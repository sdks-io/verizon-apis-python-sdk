
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `vz_m_2_m_token` | `str` | The VZ-M2M session token from [Getting Started](/content/thingspace-portal/documentation/apis/connectivity-management/get-started.html) |
| `environment` | `Environment` | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `thingspace_oauth_credentials` | [`ThingspaceOauthCredentials`](auth/oauth-2-client-credentials-grant.md) | The credential object for OAuth 2 Client Credentials Grant |
| `vz_m_2_m_session_token_credentials` | [`VzM2mSessionTokenCredentials`](auth/custom-header-signature.md) | The credential object for Custom Header Signature |

The API client can be initialized as follows:

```python
client = VerizonthingspacequalityofserviceapiendpointsClient(
    vz_m_2_m_token='VZ-M2M-Token',
    thingspace_oauth_credentials=ThingspaceOauthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    ),
    vz_m_2_m_session_token_credentials=VzM2mSessionTokenCredentials(
        vz_m_2_m_token='VZ-M2M-Token'
    ),
    environment=Environment.PRODUCTION
)
```

## Verizon ThingSpace Quality of Service API endpoints Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| thing_space_quality_of_service_api_actions | Gets ThingSpaceQualityOfServiceAPIActionsController |
| exclusions | Gets ExclusionsController |
| o_auth_authorization | Gets OAuthAuthorizationController |

