# Session Management

```python
session_management_controller = client.session_management
```

## Class Name

`SessionManagementController`

## Methods

* [Start Connectivity Management Session](../../doc/controllers/session-management.md#start-connectivity-management-session)
* [End Connectivity Management Session](../../doc/controllers/session-management.md#end-connectivity-management-session)
* [Reset Connectivity Management Password](../../doc/controllers/session-management.md#reset-connectivity-management-password)


# Start Connectivity Management Session

Initiates a Connectivity Management session and returns a VZ-M2M session token that is required in subsequent API requests.

```python
def start_connectivity_management_session(self,
                                         body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LogInRequest`](../../doc/models/log-in-request.md) | Body, Optional | Request to initiate a session. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`LogInResult`](../../doc/models/log-in-result.md).

## Example Usage

```python
body = LogInRequest(
    username='zbeeblebrox',
    password='IMgr8'
)

result = session_management_controller.start_connectivity_management_session(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "sessionToken": "bcce3ea6-fe4f-4952-bacf-eadd80718e83"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# End Connectivity Management Session

Ends a Connectivity Management session.

```python
def end_connectivity_management_session(self)
```

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`LogOutRequest`](../../doc/models/log-out-request.md).

## Example Usage

```python
result = session_management_controller.end_connectivity_management_session()
print(result)
```

## Example Response *(as JSON)*

```json
{
  "sessionToken": "bcce3ea6-fe4f-4952-bacf-eadd80718e83"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# Reset Connectivity Management Password

The new password is effective immediately. Passwords do not expire, but Verizon recommends changing your password every 90 days.

```python
def reset_connectivity_management_password(self,
                                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SessionResetPasswordRequest`](../../doc/models/session-reset-password-request.md) | Body, Required | Request with current password that needs to be reset. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`SessionResetPasswordResult`](../../doc/models/session-reset-password-result.md).

## Example Usage

```python
body = SessionResetPasswordRequest(
    old_password='grflbk'
)

result = session_management_controller.reset_connectivity_management_password(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "newPassword": "Wh0a1545a84d"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |

