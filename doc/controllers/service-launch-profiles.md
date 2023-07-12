# Service Launch Profiles

```python
service_launch_profiles_controller = client.service_launch_profiles
```

## Class Name

`ServiceLaunchProfilesController`

## Methods

* [Create Service Profile](../../doc/controllers/service-launch-profiles.md#create-service-profile)
* [Update Service Profile](../../doc/controllers/service-launch-profiles.md#update-service-profile)
* [Submit Service Profile](../../doc/controllers/service-launch-profiles.md#submit-service-profile)


# Create Service Profile

Creates a service profile that describes the resource requirements of a service.

```python
def create_service_profile(self,
                          account_name,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9]` |
| `body` | [`CreateServiceProfileRequest`](../../doc/models/create-service-profile-request.md) | Body, Required | Request for creation of a service profile. |

## Response Type

[`ServicesProfileRegistration`](../../doc/models/services-profile-registration.md)

## Example Usage

```python
account_name = 'test_account1'

body = CreateServiceProfileRequest(
    name='mongo-pmec-profile-mdp7',
    service_name='mongodb-customer-prerun',
    service_version='1.0.0'
)

result = service_launch_profiles_controller.create_service_profile(
    account_name,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 401 | HTTP 401 Unauthorized. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| Default | HTTP 500 Internal Server Error. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |


# Update Service Profile

Update the definition of a service profile.

```python
def update_service_profile(self,
                          id,
                          body,
                          account_name=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | Unique ID of the service profile.<br>**Constraints**: *Maximum Length*: `36`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `body` | [`CreateServiceProfileRequest`](../../doc/models/create-service-profile-request.md) | Body, Required | Request with new information for updating the service profile. |
| `account_name` | `string` | Header, Optional | User account name.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9]` |

## Response Type

`string`

## Example Usage

```python
id = 'eda2cb4e-50ef-4ae8-b304-7d2f0f7a21c1'

body = CreateServiceProfileRequest(
    name='mongo-pmec-profile-mdp7',
    service_name='mongodb-customer-prerun',
    service_version='1.0.0'
)

account_name = 'test_account1'

result = service_launch_profiles_controller.update_service_profile(
    id,
    body,
    account_name
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 401 | HTTP 401 Unauthorized. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| Default | HTTP 500 Internal Server Error. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |


# Submit Service Profile

Helps register a service profile.

```python
def submit_service_profile(self,
                          id,
                          body,
                          account_name=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | Unique service profile ID.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9]` |
| `body` | [`ServicesProfileRegistration`](../../doc/models/services-profile-registration.md) | Body, Required | Request for registration of a service profile. |
| `account_name` | `string` | Header, Optional | User account name.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9]` |

## Response Type

[`ServicesProfileRegistrationResult`](../../doc/models/services-profile-registration-result.md)

## Example Usage

```python
id = 'eda2cb4e-50ef-4ae8-b304-7d2f0f7a21c1'

body = ServicesProfileRegistration(
    id='6789409c-12c3-4fc9-b64f-71d1611c4f09',
    name='mongo-pmec-profile-mdp7',
    service_name='mongodb-customer-prerun',
    service_version='1.0.0',
    version='1.0.0',
    state=ServicesProfileRegistrationStateEnum.DRAFT,
    customer_id='acme',
    created_by='acme-user',
    created_at='2022-08-03T03:43:17.504Z',
    last_updated_at='2022-08-03T03:43:17.504Z',
    linked_service_instances=[],
    access_intents=AccessIntents(),
    placement_intents=PlacementIntents(
        intent_chain=[
            IntentChainItem(
                name='Compliance',
                input={"deploymentLocations":[{"csp":"AWS_WL","region":"US_WEST_2","zoneId":["us-west-2-wl1-den-wlz-1"]}]}
            )
        ]
    ),
    deployment_locations=[]
)

account_name = 'test_account1'

result = service_launch_profiles_controller.submit_service_profile(
    id,
    body,
    account_name
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 401 | HTTP 401 Unauthorized. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 412 | Precondition Failed. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| Default | HTTP 500 Internal Server Error. | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |

