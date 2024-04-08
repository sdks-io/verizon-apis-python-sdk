# Diagnostics Settings

```python
diagnostics_settings_controller = client.diagnostics_settings
```

## Class Name

`DiagnosticsSettingsController`


# List Diagnostics Settings

This endpoint retrieves diagnostics settings synchronously.

```python
def list_diagnostics_settings(self,
                             account_name,
                             devices)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Query, Required | Account identifier. |
| `devices` | `str` | Query, Required | Devices list format: [{"id":"{imei1}","kind":"imei"},{"id":"{imei2}","kind":"imei"}]. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[DiagnosticObservationSetting]`](../../doc/models/diagnostic-observation-setting.md).

## Example Usage

```python
account_name = '0000123456-00001'

devices = '[{"id":"864508030026238","kind":"IMEI"},{"id":"864508030026238","kind":"IMEI"}]'

result = diagnostics_settings_controller.list_diagnostics_settings(
    account_name,
    devices
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "accountName": "string",
    "device": {
      "id": "864508030026238",
      "kind": "IMEI"
    },
    "attributes": [
      {
        "name": "MANUFACTURER",
        "value": "string",
        "createdOn": "2019-09-07T23:08:03.532Z",
        "isObservable": true,
        "isObserving": true,
        "frequency": {
          "value": 5,
          "unit": "SECOND"
        }
      }
    ]
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response. | [`DeviceDiagnosticsResultException`](../../doc/models/device-diagnostics-result-exception.md) |

