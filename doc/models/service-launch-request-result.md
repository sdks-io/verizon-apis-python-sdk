
# Service Launch Request Result

## Structure

`ServiceLaunchRequestResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Optional | Unique service profile ID. |
| `name` | `string` | Optional | Service request name.<br>**Constraints**: *Maximum Length*: `50`, *Pattern*: `^(.*)$` |
| `service_name` | `string` | Optional | Service being deployed.<br>**Constraints**: *Maximum Length*: `50`, *Pattern*: `^(.*)$` |
| `state` | [`ServiceLaunchStateEnum`](../../doc/models/service-launch-state-enum.md) | Optional | **Constraints**: *Maximum Length*: `60`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `service_version` | `string` | Optional | Service version being deployed.<br>**Constraints**: *Maximum Length*: `50`, *Pattern*: `^(.*)$` |
| `service_id` | `string` | Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^(.*)$` |
| `service_profile_id` | `string` | Optional | The service profile ID that is created during the post-service API.<br>**Constraints**: *Maximum Length*: `50`, *Pattern*: `^(.*)$` |
| `csp_profile_id` | `string` | Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^(.*)$` |
| `config_files` | [`List of ConfigFileItem`](../../doc/models/config-file-item.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `linked_service_instances` | [`List of LinkedServiceInstance`](../../doc/models/linked-service-instance.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `updated_by` | `string` | Optional | **Constraints**: *Maximum Length*: `500`, *Pattern*: `^(.*)$` |

## Example (as JSON)

```json
{
  "createdAt": "2022-08-19T13:06:26.541Z",
  "id": "f865bb78-dd8b-4261-83ed-c3e3e081fe50",
  "linkedServiceInstances": [
    {
      "id": "e0abe65f-b294-4673-a60c-d31f26ca7a8c"
    }
  ],
  "name": "mdp_launch_request_908762",
  "serviceId": "8a29c449-f88e-4b79-8248-2c2e5e86fd98",
  "serviceName": "mongodb-customer-prerun-2",
  "serviceProfileId": "2c5c1fb6-a1fe-4de3-8a6e-e2d0663eacf5",
  "serviceVersion": "2.3.4",
  "state": "INSTANTIATED",
  "updatedAt": "2022-08-19T13:07:36.242Z"
}
```

