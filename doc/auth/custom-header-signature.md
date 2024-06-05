
# Custom Header Signature



Documentation for accessing and setting credentials for VZ-M2M-Token.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| VZ-M2M-Token | `str` | M2M Session Token ([How to generate an M2M session token?]($e/Session%20Management/StartConnectivityManagementSession)) | `vz_m2m_token` |



**Note:** Auth credentials can be set using `VZM2mTokenCredentials` object, passed in as named parameter `vz_m2m_token_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
client = VerizonClient(
    vz_m2m_token_credentials=VZM2mTokenCredentials()
)
```


