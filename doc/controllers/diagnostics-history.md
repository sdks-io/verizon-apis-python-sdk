# Diagnostics History

```python
diagnostics_history_controller = client.diagnostics_history
```

## Class Name

`DiagnosticsHistoryController`


# Get Diagnostics History

This endpoint allows the user to get the history data.

```python
def get_diagnostics_history(self,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`HistorySearchRequest`](../../doc/models/history-search-request.md) | Body, Required | History data information. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[History]`](../../doc/models/history.md).

## Example Usage

```python
body = HistorySearchRequest(
    filter=HistorySearchFilter(
        account_name='0000123456-00001',
        device=Device(
            id='15-digit IMEI',
            kind='IMEI'
        ),
        attributes=HistorySearchFilterAttributes(
            name=AttributeIdentifierEnum.LINK_QUALITY
        )
    )
)

result = diagnostics_history_controller.get_diagnostics_history(body)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "accountName": "0000123456-00001",
    "attributes": {
      "createdOn": "2022-02-10T16:02:21.406Z",
      "name": "LINK_QUALITY",
      "value": "47"
    },
    "device": {
      "id": "15-digit IMEI",
      "kind": "IMEI"
    }
  },
  {
    "accountName": "0000123456-00001",
    "attributes": {
      "createdOn": "2022-02-10T16:02:05.316Z",
      "name": "LINK_QUALITY",
      "value": "47"
    },
    "device": {
      "id": "15-digit IMEI",
      "kind": "IMEI"
    }
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response. | [`DeviceDiagnosticsResultException`](../../doc/models/device-diagnostics-result-exception.md) |

