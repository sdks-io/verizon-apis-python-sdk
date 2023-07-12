
# List Optimal Service Endpoints Result

Response on successful retrieval of optimal service endpoints for clients.

## Structure

`ListOptimalServiceEndpointsResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_endpoints` | [`List of ResourcesEdgeHostedService`](../../doc/models/resources-edge-hosted-service.md) | Optional | An array of optimal Service Endpoint IDs for clients to connect to.<br>**Constraints**: *Maximum Items*: `100` |

## Example (as JSON)

```json
{
  "serviceEndpoints": [
    {
      "ern": "ern7",
      "serviceEndpoint": {
        "URI": "URI7",
        "FQDN": "FQDN3",
        "IPv4Address": "IPv4Address3",
        "IPv6Address": "IPv6Address9",
        "port": 199
      },
      "applicationServerProviderId": "applicationServerProviderId9",
      "applicationId": "applicationId1",
      "serviceDescription": "serviceDescription5"
    },
    {
      "ern": "ern8",
      "serviceEndpoint": {
        "URI": "URI8",
        "FQDN": "FQDN4",
        "IPv4Address": "IPv4Address2",
        "IPv6Address": "IPv6Address0",
        "port": 200
      },
      "applicationServerProviderId": "applicationServerProviderId0",
      "applicationId": "applicationId2",
      "serviceDescription": "serviceDescription4"
    }
  ]
}
```

