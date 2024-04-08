# Service Profiles

```python
service_profiles_controller = client.service_profiles
```

## Class Name

`ServiceProfilesController`

## Methods

* [Create Service Profile](../../doc/controllers/service-profiles.md#create-service-profile)
* [List Service Profiles](../../doc/controllers/service-profiles.md#list-service-profiles)
* [Get Service Profile](../../doc/controllers/service-profiles.md#get-service-profile)
* [Update Service Profile](../../doc/controllers/service-profiles.md#update-service-profile)
* [Delete Service Profile](../../doc/controllers/service-profiles.md#delete-service-profile)


# Create Service Profile

Creates a service profile that describes the resource requirements of a service.

```python
def create_service_profile(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ResourcesServiceProfile`](../../doc/models/resources-service-profile.md) | Body, Required | The request body passes all of the needed parameters to create a service profile. Parameters will be edited here rather than the **Parameters** section above. The `maxLatencyMs` and `clientType` parameters are both required in the request body. **Note:** The `maxLatencyMs` value must be submitted in multiples of 5. Additionally, "GPU" is future functionality and the values are not captured. |

## Requires scope

### oAuth2

`discovery:read`, `serviceprofile:read`, `serviceprofile:write`, `serviceregistry:read`, `serviceregistry:write`, `ts.application.ro`, `ts.mec.fullaccess`, `ts.mec.limitaccess`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`CreateServiceProfileResult`](../../doc/models/create-service-profile-result.md).

## Example Usage

```python
body = ResourcesServiceProfile(
    client_type=ClientTypeEnum.V2_X,
    ecsp_filter='Verizon',
    client_schedule='time windows',
    client_service_area='BAY AREA',
    network_resources=NetworkResourcesType(
        max_latency_ms=20,
        min_bandwidth_kbits=1,
        service_continuity_support=True,
        max_request_rate=15,
        min_availability=1
    ),
    compute_resources=ComputeResourcesType(
        gpu=GPU(
            min_core_clock_m_hz=1,
            min_memory_clock_m_hz=35740,
            min_bandwidth_g_bs=588,
            min_tflops=33
        ),
        min_ramgb=1,
        min_storage_gb=1
    )
)

result = service_profiles_controller.create_service_profile(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |
| 401 | HTTP 401 Unauthorized. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |
| Default | HTTP 500 Internal Server Error. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |


# List Service Profiles

List all service profiles registered under your API key.

```python
def list_service_profiles(self)
```

## Requires scope

### oAuth2

`discovery:read`, `serviceprofile:read`, `serviceprofile:write`, `serviceregistry:read`, `serviceregistry:write`, `ts.application.ro`, `ts.mec.fullaccess`, `ts.mec.limitaccess`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ListServiceProfilesResult`](../../doc/models/list-service-profiles-result.md).

## Example Usage

```python
result = service_profiles_controller.list_service_profiles()
print(result)
```

## Example Response *(as JSON)*

```json
{
  "status": "Success",
  "data": [
    "serviceProfileId"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |
| 401 | HTTP 401 Unauthorized. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |
| Default | HTTP 500 Internal Server Error. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |


# Get Service Profile

Returns a specified service profile.

```python
def get_service_profile(self,
                       service_profile_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_profile_id` | `str` | Template, Required | - |

## Requires scope

### oAuth2

`discovery:read`, `serviceprofile:read`, `serviceprofile:write`, `serviceregistry:read`, `serviceregistry:write`, `ts.application.ro`, `ts.mec.fullaccess`, `ts.mec.limitaccess`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ResourcesServiceProfileWithId`](../../doc/models/resources-service-profile-with-id.md).

## Example Usage

```python
service_profile_id = 'serviceProfileId2'

result = service_profiles_controller.get_service_profile(service_profile_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "serviceProfileId": "4054ea9a-593e-4776-b488-697b1bfa4f3b",
  "ecspFilter": "Verizon",
  "clientSchedule": "time windows",
  "clientServiceArea": "BAY AREA",
  "clientType": "V2X",
  "networkResources": {
    "minBandwidthKbits": 1,
    "serviceContinuitySupport": true,
    "maxRequestRate": 15,
    "maxLatencyMs": 20,
    "minAvailability": 1
  },
  "computeResources": {
    "GPU": {
      "minCoreClockMHz": 1,
      "minMemoryClockMHz": 35740,
      "minBandwidthGBs": 588,
      "minTFLOPS": 33
    },
    "minRAMGB": 1,
    "minStorageGB": 1
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |
| 401 | HTTP 401 Unauthorized. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |
| Default | HTTP 500 Internal Server Error. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |


# Update Service Profile

Update the definition of a Service Profile.

```python
def update_service_profile(self,
                          service_profile_id,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_profile_id` | `str` | Template, Required | - |
| `body` | [`ResourcesServiceProfile`](../../doc/models/resources-service-profile.md) | Body, Required | The request body passes the rest of the needed parameters to create a service profile. The `maxLatencyMs` and `clientType` parameters are both required in the request body. **Note:** The `maxLatencyMs` value must be submitted in multiples of 5. Additionally, "GPU" is future functionality and the values are not captured. Default values to use are shown. |

## Requires scope

### oAuth2

`discovery:read`, `serviceprofile:read`, `serviceprofile:write`, `serviceregistry:read`, `serviceregistry:write`, `ts.application.ro`, `ts.mec.fullaccess`, `ts.mec.limitaccess`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`UpdateServiceProfileResult`](../../doc/models/update-service-profile-result.md).

## Example Usage

```python
service_profile_id = 'serviceProfileId2'

body = ResourcesServiceProfile(
    client_type=ClientTypeEnum.V2_X,
    ecsp_filter='Verizon',
    client_schedule='time windows',
    client_service_area='BAY AREA',
    network_resources=NetworkResourcesType(
        max_latency_ms=20,
        min_bandwidth_kbits=1,
        service_continuity_support=True,
        max_request_rate=15,
        min_availability=1
    ),
    compute_resources=ComputeResourcesType(
        gpu=GPU(
            min_core_clock_m_hz=1
        ),
        min_ramgb=1,
        min_storage_gb=1
    )
)

result = service_profiles_controller.update_service_profile(
    service_profile_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "status": "Success",
  "message": "Service Profile Updated"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |
| 401 | HTTP 401 Unauthorized. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |
| Default | HTTP 500 Internal Server Error. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |


# Delete Service Profile

Delete Service Profile based on unique service profile ID.

```python
def delete_service_profile(self,
                          service_profile_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_profile_id` | `str` | Template, Required | - |

## Requires scope

### oAuth2

`discovery:read`, `serviceprofile:read`, `serviceprofile:write`, `serviceregistry:read`, `serviceregistry:write`, `ts.application.ro`, `ts.mec.fullaccess`, `ts.mec.limitaccess`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeleteServiceProfileResult`](../../doc/models/delete-service-profile-result.md).

## Example Usage

```python
service_profile_id = 'serviceProfileId2'

result = service_profiles_controller.delete_service_profile(service_profile_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "status": "Success",
  "message": "Service Profile Deleted"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |
| 401 | HTTP 401 Unauthorized. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |
| Default | HTTP 500 Internal Server Error. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |

