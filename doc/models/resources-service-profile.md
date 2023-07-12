
# Resources Service Profile

Information about the resource requirements and service characteristics of an edge application. The `maxLatencyMs` and `clientType` parameters are both required in the request body. **Note:** The `maxLatencyMs` value must be submitted in multiples of 5. Does not include serviceProfileId

## Structure

`ResourcesServiceProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_type` | [`ClientTypeEnum`](../../doc/models/client-type-enum.md) | Required | The category of application client. |
| `ecsp_filter` | `string` | Optional | Identity of the preferred Edge Computing Service Provider.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `client_schedule` | `string` | Optional | The expected operation schedule of the application client (e.g. time windows).<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9 ]{3,32}$` |
| `client_service_area` | `string` | Optional | The expected location(s) (e.g. route) of the hosting UE during the Client's operation schedule.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9 ]{3,32}$` |
| `network_resources` | [`NetworkResourcesType`](../../doc/models/network-resources-type.md) | Optional | Network resources of a service profile. |
| `compute_resources` | [`ComputeResourcesType`](../../doc/models/compute-resources-type.md) | Optional | Compute resources of a service profile. |
| `properties` | [`MECPlatformsAdditionalSupportInfo`](../../doc/models/mec-platforms-additional-support-info.md) | Optional | Additional service support information for the MEC platform. |

## Example (as JSON)

```json
{
  "clientType": "IoT",
  "ecspFilter": "Verizon",
  "clientSchedule": "time windows",
  "clientServiceArea": "BAY AREA",
  "networkResources": {
    "minBandwidthKbits": 252,
    "serviceContinuitySupport": false,
    "maxRequestRate": 138,
    "maxLatencyMs": 146,
    "minAvailability": 194
  },
  "computeResources": {
    "GPU": {
      "minCoreClockMHz": 222,
      "minMemoryClockMHz": 62,
      "minBandwidthGBs": 54,
      "minTFLOPS": 198
    },
    "minRAMGB": 192,
    "minStorageGB": 190
  }
}
```

