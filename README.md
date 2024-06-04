
# Getting Started with Verizon

## Introduction

The Verizon Edge Discovery Service API can direct your application clients to connect to the optimal service endpoints for your Multi-access Edge Computing (MEC) applications for every session. The Edge Discovery Service takes into account the current location of a device, its IP anchor location, current network traffic and other factors to determine which 5G Edge platform a device should connect to.

Verizon Terms of Service: [https://www.verizon.com/business/5g-edge-portal/legal.html](https://www.verizon.com/business/5g-edge-portal/legal.html)

## Install the Package

The package is compatible with Python versions `3 >=3.7, <= 3.11`.
Install the package from PyPi using the following pip command:

```python
pip install sdksio-verizon-apis-sdk==1.4.0
```

You can also view the package at:
https://pypi.python.org/pypi/sdksio-verizon-apis-sdk/1.4.0

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `vz_m2m_token` | `str` | M2M Session Token ([How to generate an M2M session token?](page:getting-started/5g-edge-developer-creds-token#obtaining-a-vz-m2m-session-token-programmatically)) |
| `environment` | `Environment` | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `client_credentials_auth_credentials` | [`ClientCredentialsAuthCredentials`](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/$a/https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/oauth-2-client-credentials-grant.md) | The credential object for OAuth 2 Client Credentials Grant |

The API client can be initialized as follows:

```python
client = VerizonClient(
    vz_m2m_token='VZ-M2M-Token',
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        oauth_client_id='OAuthClientId',
        oauth_client_secret='OAuthClientSecret',
        oauth_scopes=[
            OauthScopeEnum.DISCOVERYREAD,
            OauthScopeEnum.SERVICEPROFILEREAD
        ]
    )
)
```

API calls return an `ApiResponse` object that includes the following fields:

| Field | Description |
|  --- | --- |
| `status_code` | Status code of the HTTP response |
| `reason_phrase` | Reason phrase of the HTTP response |
| `headers` | Headers of the HTTP response as a dictionary |
| `text` | The body of the HTTP response as a string |
| `request` | HTTP request info |
| `errors` | Errors, if they exist |
| `body` | The deserialized body of the HTTP response |

## Authorization

This API uses the following authentication schemes.

* [`oAuth2 (OAuth 2 Client Credentials Grant)`](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/$a/https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/oauth-2-client-credentials-grant.md)

## List of APIs

* [5G Edge Platforms](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/5g-edge-platforms.md)
* [Service Endpoints](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/service-endpoints.md)
* [Service Profiles](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/service-profiles.md)
* [Device Management](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/device-management.md)
* [Device Groups](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/device-groups.md)
* [Session Management](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/session-management.md)
* [Connectivity Callbacks](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/connectivity-callbacks.md)
* [Account Requests](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/account-requests.md)
* [Service Plans](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/service-plans.md)
* [Device Diagnostics](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/device-diagnostics.md)
* [Device Profile Management](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/device-profile-management.md)
* [Device Monitoring](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/device-monitoring.md)
* [E UICC Device Profile Management](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/e-uicc-device-profile-management.md)
* [Devices Locations](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/devices-locations.md)
* [Devices Location Subscriptions](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/devices-location-subscriptions.md)
* [Device Location Callbacks](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/device-location-callbacks.md)
* [Usage Trigger Management](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/usage-trigger-management.md)
* [Software Management Subscriptions V1](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/software-management-subscriptions-v1.md)
* [Software Management Licenses V1](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/software-management-licenses-v1.md)
* [Firmware V1](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/firmware-v1.md)
* [Software Management Callbacks V1](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/software-management-callbacks-v1.md)
* [Software Management Reports V1](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/software-management-reports-v1.md)
* [Software Management Subscriptions V2](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/software-management-subscriptions-v2.md)
* [Software Management Licenses V2](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/software-management-licenses-v2.md)
* [Campaigns V2](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/campaigns-v2.md)
* [Software Management Callbacks V2](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/software-management-callbacks-v2.md)
* [Software Management Reports V2](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/software-management-reports-v2.md)
* [Client Logging](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/client-logging.md)
* [Server Logging](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/server-logging.md)
* [Configuration Files](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/configuration-files.md)
* [Software Management Subscriptions V3](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/software-management-subscriptions-v3.md)
* [Software Management Licenses V3](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/software-management-licenses-v3.md)
* [Campaigns V3](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/campaigns-v3.md)
* [Software Management Reports V3](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/software-management-reports-v3.md)
* [Firmware V3](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/firmware-v3.md)
* [Account Devices](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/account-devices.md)
* [Software Management Callbacks V3](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/software-management-callbacks-v3.md)
* [SIM Securefor Io T Licenses](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/sim-securefor-io-t-licenses.md)
* [Account Subscriptions](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/account-subscriptions.md)
* [Performance Metrics](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/performance-metrics.md)
* [Diagnostics Subscriptions](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/diagnostics-subscriptions.md)
* [Diagnostics Observations](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/diagnostics-observations.md)
* [Diagnostics History](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/diagnostics-history.md)
* [Diagnostics Settings](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/diagnostics-settings.md)
* [Diagnostics Callbacks](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/diagnostics-callbacks.md)
* [Diagnostics Factory Reset](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/diagnostics-factory-reset.md)
* [Cloud Connector Subscriptions](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/cloud-connector-subscriptions.md)
* [Cloud Connector Devices](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/cloud-connector-devices.md)
* [Device Service Management](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/device-service-management.md)
* [Device Reports](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/device-reports.md)
* [Hyper Precise Location Callbacks](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/hyper-precise-location-callbacks.md)
* [Anomaly Settings](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/anomaly-settings.md)
* [Anomaly Triggers](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/anomaly-triggers.md)
* [Anomaly Triggers V2](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/anomaly-triggers-v2.md)
* [Wireless Network Performance](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/wireless-network-performance.md)
* [Fixed Wireless Qualification](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/fixed-wireless-qualification.md)
* [Managinge SIM Profiles](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/managinge-sim-profiles.md)
* [Device SMS Messaging](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/device-sms-messaging.md)
* [Device Actions](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/device-actions.md)
* [Thing Space Qualityof Service API Actions](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/thing-space-qualityof-service-api-actions.md)
* [Promotion Period Information](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/promotion-period-information.md)
* [Retrievethe Triggers](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/retrievethe-triggers.md)
* [Update Triggers](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/update-triggers.md)
* [SIM Actions](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/sim-actions.md)
* [Global Reporting](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/global-reporting.md)
* [OAuth Authorization](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/oauth-authorization.md)
* [Accounts](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/accounts.md)
* [SMS](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/sms.md)
* [Exclusions](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/exclusions.md)
* [Billing](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/billing.md)
* [Targets](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/targets.md)
* [MEC](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/controllers/mec.md)

## Classes Documentation

* [Utility Classes](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/utility-classes.md)
* [HttpResponse](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/http-response.md)
* [HttpRequest](https://www.github.com/sdks-io/verizon-apis-python-sdk/tree/1.4.0/doc/http-request.md)

