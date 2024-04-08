
# Connectivity Management Callback

Includes callback listeners that were registered through the Connectivity Management API.

## Structure

`ConnectivityManagementCallback`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The name of the billing account for which callback messages will be sent. |
| `password` | `str` | Optional | The password defined when a URL was registered for the callback service, or an empty string if no password was defined. |
| `service_name` | `str` | Optional | The name of the callback service, which identifies the type and format of messages that will be sent to the registered URL. |
| `url` | `str` | Optional | The address of the callback listening service where the ThingSpace Platform will send callback messages for the service type. |
| `username` | `str` | Optional | The username defined when a URL was registered for the callback service, or an empty string if no username was defined. |

## Example (as JSON)

```json
{
  "accountName": "0252012345-00001",
  "password": "drowssap",
  "serviceName": "DeviceUsage",
  "url": "http://10.120.102.147:50569/CallbackListener/Usage.asmx",
  "username": "zaffod"
}
```

