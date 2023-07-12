# Repositories

```python
repositories_controller = client.repositories
```

## Class Name

`RepositoriesController`

## Methods

* [List Repositories](../../doc/controllers/repositories.md#list-repositories)
* [Create Repository](../../doc/controllers/repositories.md#create-repository)
* [Delete Repository](../../doc/controllers/repositories.md#delete-repository)


# List Repositories

Get all repositories in the platform.

```python
def list_repositories(self,
                     account_name,
                     correlation_id=None,
                     mtype=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |
| `mtype` | `string` | Query, Optional | Repository type.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`List of Repository`](../../doc/models/repository.md)

## Example Usage

```python
account_name = 'test_account1'

correlation_id = '9958f2f8-c4e3-46e0-8982-356de6515ae9'

mtype = 'GIT'

result = repositories_controller.list_repositories(
    account_name,
    correlation_id,
    mtype
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "name": "myRepo"
  },
  {
    "name": "anotherRepo"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 404 | Not found. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |


# Create Repository

Create a repository within user's organziation.

```python
def create_repository(self,
                     account_name,
                     body,
                     correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `body` | [`Repository`](../../doc/models/repository.md) | Body, Required | - |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`Repository`](../../doc/models/repository.md)

## Example Usage

```python
account_name = 'test_account1'

body = Repository(
    name='myRepo',
    description='My organization repository.',
    mtype=EdgeServiceRepositoryTypeEnum.GIT,
    tag='myTag',
    endpoint='https://charts.bitnami.com/bitnami'
)

correlation_id = '9958f2f8-c4e3-46e0-8982-356de6515ae9'

result = repositories_controller.create_repository(
    account_name,
    body,
    correlation_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "createdBy": "dev-api-user",
  "createdDate": "2022-08-25T11:38:06.000Z",
  "endpoint": "https://charts.bitnami.com/bitnami",
  "id": "60d0a7f0-1811-43fd-be4a-b47e5fe2c755",
  "lastModifiedDate": "2022-08-25T11:38:06.000Z",
  "name": "dev-api-demo-repo-1",
  "type": "Helm",
  "updatedBy": "dev-api-user"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 401 | Unauthorized. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |


# Delete Repository

Delete the repository.

```python
def delete_repository(self,
                     account_name,
                     repository_name,
                     correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `repository_name` | `string` | Template, Required | Name of the repository which is about to be deleted.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9-]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`EdgeServiceOnboardingDeleteResult`](../../doc/models/edge-service-onboarding-delete-result.md)

## Example Usage

```python
account_name = 'test_account1'

repository_name = 'dev-api-demo-repo-mdp'

correlation_id = '9958f2f8-c4e3-46e0-8982-356de6515ae9'

result = repositories_controller.delete_repository(
    account_name,
    repository_name,
    correlation_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "message": "service deleted succesfully",
  "status": "success",
  "subStatus": "service delete - success"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 401 | Unauthorized. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 404 | Not found. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |

