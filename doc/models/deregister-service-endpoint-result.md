
# Deregister Service Endpoint Result

Response to deregister an application's Service Endpoint from one or more Multi-access Edge Compute (MEC) Platforms.

## Structure

`DeregisterServiceEndpointResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Optional | HTTP status code.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `message` | `str` | Optional | EdgeAppServicesID that are deleted or error details in case of an error.<br>**Constraints**: *Maximum Length*: `32` |

## Example (as JSON)

```json
{
  "status": "Success",
  "message": "EdgeAppServicesID Deleted"
}
```

