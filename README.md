
# Getting Started with Verizon ThingSpace Quality of Service API endpoints

## Introduction

These are the endpoints to subscribe to and end the subscription for Verizon's ThingSpace Quality of Service API. These endpoints use Service Capability Exposure Function or SCEF, and rely on callbacks for asynchronous requests. **Note:** This example is in YAML and will need to be converted to JSON to use as a spec file.

## Install the Package

The package is compatible with Python versions `3 >=3.7, <= 3.11`.
Install the package from PyPi using the following pip command:

```python
pip install sdksio-verizon-apis-sdk==1.6.0
```

You can also view the package at:
https://pypi.python.org/pypi/sdksio-verizon-apis-sdk/1.6.0

## Test the SDK

You can test the generated SDK and the server with test cases. `unittest` is used as the testing framework and `pytest` is used as the test runner. You can run the tests as follows:

Navigate to the root directory of the SDK and run the following commands

```
pip install -r test-requirements.txt
pytest
```

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.6.0/doc/client.md)

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
| `thingspace_oauth_credentials` | [`ThingspaceOauthCredentials`](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.6.0/doc/auth/oauth-2-client-credentials-grant.md) | The credential object for OAuth 2 Client Credentials Grant |
| `vz_m_2_m_session_token_credentials` | [`VzM2mSessionTokenCredentials`](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.6.0/doc/auth/custom-header-signature.md) | The credential object for Custom Header Signature |

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

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| Production | **Default** |
| Staging | - |

## Authorization

This API uses the following authentication schemes.

* [`thingspace_oauth (OAuth 2 Client Credentials Grant)`](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.6.0/doc/auth/oauth-2-client-credentials-grant.md)
* [`vz-m2m-session_token (Custom Header Signature)`](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.6.0/doc/auth/custom-header-signature.md)

## List of APIs

* [Thing Space Qualityof Service API Actions](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.6.0/doc/controllers/thing-space-qualityof-service-api-actions.md)
* [Exclusions](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.6.0/doc/controllers/exclusions.md)

## Classes Documentation

* [Utility Classes](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.6.0/doc/utility-classes.md)
* [HttpResponse](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.6.0/doc/http-response.md)
* [HttpRequest](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.6.0/doc/http-request.md)

