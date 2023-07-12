
# Retrieves Available Files Response List

## Structure

`RetrievesAvailableFilesResponseList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `available_files_response` | [`List of RetrievesAvailableFilesResponse`](../../doc/models/retrieves-available-files-response.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example (as JSON)

```json
{
  "AvailableFilesResponse": [
    {
      "fileName": "fileName8",
      "fileVersion": "fileVersion0",
      "releaseNote": "releaseNote6",
      "make": "make6",
      "model": "model2"
    },
    {
      "fileName": "fileName9",
      "fileVersion": "fileVersion1",
      "releaseNote": "releaseNote7",
      "make": "make5",
      "model": "model3"
    },
    {
      "fileName": "fileName0",
      "fileVersion": "fileVersion2",
      "releaseNote": "releaseNote8",
      "make": "make4",
      "model": "model4"
    }
  ]
}
```

