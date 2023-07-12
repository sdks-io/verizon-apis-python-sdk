
# Service Launch Requests Result

## Structure

`ServiceLaunchRequestsResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `result_set` | [`List of ServiceLaunchRequestResult`](../../doc/models/service-launch-request-result.md) | Optional | **Constraints**: *Maximum Items*: `1000` |

## Example (as JSON)

```json
{
  "resultSet": [
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
  ],
  "count": 60,
  "next": "next2",
  "previous": "previous8"
}
```

