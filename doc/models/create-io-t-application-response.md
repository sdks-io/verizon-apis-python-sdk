
# Create Io T Application Response

A success response includes an array of all matching events. Each event includes the full event resource definition.

## Structure

`CreateIoTApplicationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `app_name` | `str` | Optional | An application will be created under the user's Azure subscription with this name and of type IOT central. |
| `shared_secret` | `str` | Optional | Part of the user credentials (from Azure) the user needs to use for calling further TS Core APIs for setting up Azure cloud connector. |
| `url` | `str` | Optional | An IOT central endpoint the user can use to see the data that is being streamed. |

## Example (as JSON)

```json
{
  "appName": "newarmapp1",
  "sharedSecret": "SharedAccessSignaturesr={client secret}",
  "url": "https://newarmapp1.azureiotcentral.com"
}
```

