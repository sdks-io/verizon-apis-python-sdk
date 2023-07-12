# 5G Edge Platforms

```python
m_5g_edge_platforms_controller = client.m_5g_edge_platforms
```

## Class Name

`M5gEdgePlatformsController`

## Methods

* [List MEC Platforms](../../doc/controllers/5g-edge-platforms.md#list-mec-platforms)
* [List Regions](../../doc/controllers/5g-edge-platforms.md#list-regions)


# List MEC Platforms

Returns a list of optimal MEC Platforms where you can register your deployed application. **Note:** If a query is sent with all of the parameters, it will fail with a "400" error. You can search based on the following parameter combinations - region plus Service Profile ID and subscriber density (density is optional but recommended), region plus UEIdentity(Including UEIdentity Type) or Service Profile ID plus UEIdentity(Including UEIdentity Type).

```python
def list_mec_platforms(self,
                      region=None,
                      service_profile_id=None,
                      subscriber_density=None,
                      ue_identity_type=None,
                      ue_identity=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `region` | `string` | Query, Optional | MEC region name. Current valid values are US_WEST_2 and US_EAST_1. |
| `service_profile_id` | `string` | Query, Optional | Unique identifier of the service profile.<br>**Constraints**: *Maximum Length*: `36`, *Pattern*: `^[a-zA-Z0-9!@#$&()\-`.+,/"]{3,36}$` |
| `subscriber_density` | `int` | Query, Optional | Minimum number of 4G/5G subscribers per square kilometer.<br>**Constraints**: `>= 1`, `<= 100` |
| `ue_identity_type` | [`UserEquipmentIdentityTypeEnum`](../../doc/models/user-equipment-identity-type-enum.md) | Query, Optional | Type of User Equipment identifier used in `UEIdentity`. |
| `ue_identity` | `string` | Query, Optional | The identifier value for User Equipment. The type of identifier is defined by the 'UEIdentityType' parameter. The`IPAddress`format can be IPv4 or IPv6. |

## Requires scope

`EDGEDISCOVERYREAD`, `EDGESERVICEPROFILEREAD`, `EDGESERVICEPROFILEWRITE`, `EDGESERVICEREGISTRYREAD`, `EDGESERVICEREGISTRYWRITE`, `TS_APPLICATION_RO`, `TS_MEC_FULLACCESS`, `TS_MEC_LIMITACCESS`

## Response Type

[`ListMECPlatformsResult`](../../doc/models/list-mec-platforms-result.md)

## Example Usage

```python
region = 'US_WEST_2'

ue_identity_type = UserEquipmentIdentityTypeEnum.IPADDRESS

ue_identity = '2600:1010:b1d0:0000:0000:0000:0000:0012'

result = m_5g_edge_platforms_controller.list_mec_platforms(
    region,
    ue_identity_type,
    ue_identity
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "MECPlatforms": [
    {
      "ern": "5x4VBwmfZbzSL3",
      "zone": "e5oV52kMGjDLhnJSsLJZL",
      "region": "US_WEST_2",
      "status": "unknown"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |
| 401 | HTTP 401 Unauthorized. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |
| Default | HTTP 500 Internal Server Error. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |


# List Regions

List the geographical regions available, based on the user's bearer token. **Note:** Country code, Metropolitan area, Area and Zone are future functionality and will currently return a "null" value.

```python
def list_regions(self)
```

## Requires scope

`EDGEDISCOVERYREAD`, `EDGESERVICEPROFILEREAD`, `EDGESERVICEPROFILEWRITE`, `EDGESERVICEREGISTRYREAD`, `EDGESERVICEREGISTRYWRITE`, `TS_APPLICATION_RO`, `TS_MEC_FULLACCESS`, `TS_MEC_LIMITACCESS`

## Response Type

[`ListRegionsResult`](../../doc/models/list-regions-result.md)

## Example Usage

```python
result = m_5g_edge_platforms_controller.list_regions()
print(result)
```

## Example Response *(as JSON)*

```json
{
  "regions": [
    {
      "regionId": "consectetur",
      "name": "US_EAST_1",
      "countryCode": "nr",
      "metro": "e1D",
      "area": "IdUESF"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |
| 401 | HTTP 401 Unauthorized. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |
| Default | HTTP 500 Internal Server Error. | [`EdgeDiscoveryResultException`](../../doc/models/edge-discovery-result-exception.md) |

