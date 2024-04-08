
# OAuth 2 Client Credentials Grant



Documentation for accessing and setting credentials for oAuth2.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| OAuthClientId | `str` | OAuth 2 Client ID | `oauth_client_id` |
| OAuthClientSecret | `str` | OAuth 2 Client Secret | `oauth_client_secret` |
| OAuthToken | `OauthToken` | Object for storing information about the OAuth token | `oauth_token` |
| OAuthScopes | `List[OauthScopeEnum]` | List of scopes that apply to the OAuth token | `oauth_scopes` |



**Note:** Auth credentials can be set using `ClientCredentialsAuthCredentials` object, passed in as named parameter `client_credentials_auth_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must initialize the client with *OAuth 2.0 Client Credentials Grant* credentials as shown in the following code snippet.

```python
client = VerizonClient(
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



Your application must obtain user authorization before it can execute an endpoint call in case this SDK chooses to use *OAuth 2.0 Client Credentials Grant*. This authorization includes the following steps.

The `fetch_token()` method will exchange the OAuth client credentials for an *access token*. The access token is an object containing information for authorizing client requests and refreshing the token itself.

You must have initialized the client with scopes for which you need permission to access.

```python
try:
    token = client.oauth_2.fetch_token()
    client_credentials_auth_credentials = client.config.client_credentials_auth_credentials.clone_with(oauth_token=token)
    config = client.config.clone_with(client_credentials_auth_credentials=client_credentials_auth_credentials)
    client = VerizonClient(config)
except OauthProviderException as ex:
    # handle exception
    pass
except APIException as ex:
    # handle exception
    pass
```

The client can now make authorized endpoint calls.

### Scopes

Scopes enable your application to only request access to the resources it needs while enabling users to control the amount of access they grant to your application. Available scopes are defined in the [`OauthScopeEnum`](../../doc/models/oauth-scope-enum.md) enumeration.

| Scope Name | Description |
|  --- | --- |
| `DISCOVERYREAD` | Grant read-only access to discovery data |
| `SERVICEPROFILEREAD` | Grant read-only access to service profile data |
| `SERVICEPROFILEWRITE` | Grant write access to service profile data |
| `SERVICEREGISTRYREAD` | Grant read-only access to Service registry data |
| `SERVICEREGISTRYWRITE` | Grant write access to Service registry data |
| `TS_MEC_FULLACCESS` | Full access for /serviceprofiles and /serviceendpoints. |
| `TS_MEC_LIMITACCESS` | Limited access. Will not allow use of /serviceprofiles and /serviceendpoints but will allow discovery. |
| `TS_APPLICATION_RO` |  |
| `READ` | read access |
| `WRITE` | read/write access |

### Storing an access token for reuse

It is recommended that you store the access token for reuse.

```python
# store token
save_token_to_database(client.config.client_credentials_auth_credentials.oauth_token)
```

### Creating a client from a stored token

To authorize a client from a stored access token, just set the access token in Configuration along with the other configuration parameters before creating the client:

```python
client = VerizonClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        oauth_token=load_token_from_database()
    )
)
```

### Complete example



```python
from verizon.verizon_client import VerizonClient
from verizon.models.oauth_scope_enum import OauthScopeEnum
from verizon.exceptions.oauth_provider_exception import OauthProviderException

from verizon.exceptions.api_exception import APIException

client = VerizonClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        oauth_client_id='OAuthClientId',
        oauth_client_secret='OAuthClientSecret',
        oauth_scopes=[
            OauthScopeEnum.DISCOVERYREAD,
            OauthScopeEnum.SERVICEPROFILEREAD
        ]
    )
)
# function for storing token to database
def save_token_to_database(oauth_token):
    # code to save the token to database
    pass

# function for loading token from database
def load_token_from_database():
    # load token from database and return it (return None if no token exists)
    pass

# obtain access token, needed for client to be authorized
previous_token = load_token_from_database()
if previous_token:
    # restore previous access token
    client_credentials_auth_credentials = client.config.client_credentials_auth_credentials.clone_with(oauth_token=previous_token)
    config = client.config.clone_with(client_credentials_auth_credentials=client_credentials_auth_credentials)
    client = VerizonClient(config)
else:
    # obtain new access token
    try:
        token = client.oauth_2.fetch_token()
        save_token_to_database(token)
        client_credentials_auth_credentials = client.config.client_credentials_auth_credentials.clone_with(oauth_token=token)
        config = client.config.clone_with(client_credentials_auth_credentials=client_credentials_auth_credentials)
        client = VerizonClient(config)
    except OauthProviderException as ex:
        # handle exception
        pass
    except APIException as ex:
        # handle exception
        pass

# the client is now authorized and you can use controllers to make endpoint calls
```


