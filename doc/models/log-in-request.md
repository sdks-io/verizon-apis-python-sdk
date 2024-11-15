
# Log in Request

Request to initiate a Connectivity Management session and returns a VZ-M2M session token that is required in subsequent API requests.

## Structure

`LogInRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `str` | Required | The username for authentication. |
| `password` | `str` | Required | The password for authentication. |

## Example (as JSON)

```json
{
  "username": "zbeeblebrox",
  "password": "IMgr8"
}
```

