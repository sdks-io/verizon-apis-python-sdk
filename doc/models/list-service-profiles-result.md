
# List Service Profiles Result

Response on successful retrieval of service profiles.

## Structure

`ListServiceProfilesResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Optional | HTTP status code.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `data` | `List[str]` | Optional | A comma delimited list of all the service profiles registered under your API key.<br>**Constraints**: *Maximum Items*: `100`, *Maximum Length*: `32` |

## Example (as JSON)

```json
{
  "status": "Success",
  "data": [
    "data3",
    "data4",
    "data5"
  ]
}
```

