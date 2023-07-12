
# Service Delete Result

Response to delete a service.

## Structure

`ServiceDeleteResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `selected_service` | [`SelectedService`](../../doc/models/selected-service.md) | Optional | Service which is selected. |
| `dependent_service` | [`List of DependentService`](../../doc/models/dependent-service.md) | Optional | List of dependent services.<br>**Constraints**: *Maximum Items*: `2048` |
| `running_instances` | [`List of RunningInstance`](../../doc/models/running-instance.md) | Optional | List of running Instance.<br>**Constraints**: *Maximum Items*: `2048` |
| `error_details` | [`EdgeServiceOnboardingResult`](../../doc/models/edge-service-onboarding-result.md) | Optional | Error response attribute of a service. |

## Example (as JSON)

```json
{
  "selectedService": {
    "name": "MyService",
    "version": "1.0.0",
    "state": "TESTING"
  },
  "dependentService": [
    {
      "name": "MyService",
      "version": "1.0.0",
      "status": "DRAFT_INPROGRESS",
      "type": "MY_SERVICE",
      "createdBy": "User",
      "lastModifiedBy": "User",
      "Instances": 10
    }
  ],
  "runningInstances": [
    {
      "instanceName": "gst-server",
      "instanceID": "fce1f1eb-a832-4a1f-9883-b324c6fb55bc",
      "CSP": "AWS_PUBLIC_CLOUD",
      "status": "DRAFT_INPROGRESS"
    }
  ],
  "errorDetails": {
    "code": "SDMS_001_001",
    "message": "Service does not exist",
    "remedyMessage": "Create a new service serviceName and version"
  }
}
```

