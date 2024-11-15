
# List Optimal Service Endpoints Result

Response on successful retrieval of optimal service endpoints for clients.

## Structure

`ListOptimalServiceEndpointsResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_endpoints` | [`List[ResourcesEdgeHostedService]`](../../doc/models/resources-edge-hosted-service.md) | Optional | An array of optimal Service Endpoint IDs for clients to connect to.<br>**Constraints**: *Maximum Items*: `100` |

## Example (as JSON)

```json
{
  "serviceEndpoints": [
    {
      "ern": "ern0",
      "serviceEndpoint": {
        "URI": "URI6",
        "FQDN": "FQDN2",
        "IPv4Address": "IPv4Address4",
        "IPv6Address": "IPv6Address8",
        "port": 16
      },
      "applicationServerProviderId": "applicationServerProviderId2",
      "applicationId": "applicationId4",
      "serviceDescription": "serviceDescription2"
    }
  ]
}
```

