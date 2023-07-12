
# Associate Cloud Credential Result

Response to associate an existing cloud credential to a service's claim. System will use the associated claim for deploying the service into the target platform.

## Structure

`AssociateCloudCredentialResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `string` | Optional | Brief description of the response in the form of a message.<br>**Constraints**: *Maximum Length*: `200`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]!,+\-=_:.&*%\s]+$` |

## Example (as JSON)

```json
{
  "message": "CSP Profile got associated with current claim successfully"
}
```

