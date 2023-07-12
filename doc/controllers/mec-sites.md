# MEC Sites

```python
mec_sites_controller = client.mec_sites
```

## Class Name

`MECSitesController`

## Methods

* [List MEC Site Locations](../../doc/controllers/mec-sites.md#list-mec-site-locations)
* [List ERN Cluster Namespaces](../../doc/controllers/mec-sites.md#list-ern-cluster-namespaces)


# List MEC Site Locations

Supports fetching MEC locations so the user can view the city.

```python
def list_mec_site_locations(self,
                           account_name=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Optional | User account name.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9]` |

## Response Type

[`MECSiteLocationsResult`](../../doc/models/mec-site-locations-result.md)

## Example Usage

```python
account_name = 'test_account1'

result = mec_sites_controller.list_mec_site_locations(
    account_name
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |


# List ERN Cluster Namespaces

Retrieve all clusters for the customer.

```python
def list_ern_cluster_namespaces(self,
                               user_id,
                               role,
                               customer_id,
                               request_id,
                               ern=None,
                               name=None,
                               offset=None,
                               limit=None,
                               correlation_id=None,
                               cluster_state=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `role` | `string` | Header, Required | **Constraints**: *Maximum Length*: `500` |
| `customer_id` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `request_id` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `ern` | `string` | Query, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `name` | `string` | Query, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `offset` | `string` | Query, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `limit` | `string` | Query, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `cluster_state` | [`ClusterStateEnum`](../../doc/models/cluster-state-enum.md) | Query, Optional | **Constraints**: *Maximum Length*: `32` |

## Response Type

[`ClustersNamespaces`](../../doc/models/clusters-namespaces.md)

## Example Usage

```python
user_id = 'userId0'

role = 'role6'

customer_id = 'customerId6'

request_id = 'requestId2'

result = mec_sites_controller.list_ern_cluster_namespaces(
    user_id,
    role,
    customer_id,
    request_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 404 | Not found. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| Default | Unexpected error. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |

