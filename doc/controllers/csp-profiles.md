# CSP Profiles

```python
csp_profiles_controller = client.csp_profiles
```

## Class Name

`CSPProfilesController`

## Methods

* [Fetch Cloud Credential Details](../../doc/controllers/csp-profiles.md#fetch-cloud-credential-details)
* [Create Cloud Credential](../../doc/controllers/csp-profiles.md#create-cloud-credential)
* [Remove Cloud Credential](../../doc/controllers/csp-profiles.md#remove-cloud-credential)


# Fetch Cloud Credential Details

Fetch available cloud credentials within user's organization.

```python
def fetch_cloud_credential_details(self,
                                  account_name,
                                  correlation_id=None,
                                  q=None,
                                  limit=None,
                                  off_set=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |
| `q` | `string` | Query, Optional | Use the coloumn (:) character to separate multiple query params eg type=AWS:awsCspProfile.credType=ACCESS_KEY,ROLE_ARN:state=UNVERIFIED,VERIFIED.<br>**Constraints**: *Maximum Length*: `2048`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!\/,+\-=_:.&*%\s]+$` |
| `limit` | `long\|int` | Query, Optional | Number of items to return.<br>**Constraints**: `>= 0`, `<= 1024` |
| `off_set` | `long\|int` | Query, Optional | Id of the last respose value in the previous list.<br>**Constraints**: `>= 0`, `<= 1024` |

## Response Type

[`CSPProfileData`](../../doc/models/csp-profile-data.md)

## Example Usage

```python
account_name = 'test_account1'

correlation_id = '9958f2f8-c4e3-46e0-8982-356de6515ae9'

q = 'cspProfileName=dev-api-csp-profile-mdp'

limit = 256

off_set = 255

result = csp_profiles_controller.fetch_cloud_credential_details(
    account_name,
    correlation_id,
    q,
    limit,
    off_set
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "count": 1,
  "cspProfileList": [
    {
      "awsCspProfile": {
        "accessKey": "XXXXX",
        "credType": "ACCESS_KEY",
        "secretKey": "XXXXX"
      },
      "createdBy": "acme-user",
      "createdDate": "2022-08-03T13:59:51.000Z",
      "cspProfileName": "dev-api-csp-profile-mdp",
      "customerID": "acme",
      "id": "72e35c51-098e-4388-9055-2967bbd9be48",
      "lastModifiedBy": "acme-user",
      "lastModifiedDate": "2022-08-03T13:59:51.000Z",
      "projectName": "vz-cve",
      "type": "AWS"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 403 | Forbidden. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 404 | Not found. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 429 | Too many requests. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| Default | Forbidden. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |


# Create Cloud Credential

Create a new cloud credential within user's organization.

```python
def create_cloud_credential(self,
                           account_name,
                           body,
                           correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `body` | [`CSPProfile`](../../doc/models/csp-profile.md) | Body, Required | - |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`CSPProfile`](../../doc/models/csp-profile.md)

## Example Usage

```python
account_name = 'test_account1'

body = CSPProfile(
    csp_profile_name='dev-api-csp-profile-mdp',
    project_name='vz-cve',
    mtype=CSPProfileTypeEnum.AWS,
    aws_csp_profile=AwsCspProfile(
        cred_type=AwsCspProfileCredTypeEnum.ACCESS_KEY,
        access_key='XXXXX',
        secret_key='XXXXX'
    )
)

correlation_id = '9958f2f8-c4e3-46e0-8982-356de6515ae9'

result = csp_profiles_controller.create_cloud_credential(
    account_name,
    body,
    correlation_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "awsCspProfile": {
    "accessKey": "XXXXX",
    "credType": "ACCESS_KEY",
    "secretKey": "XXXXX"
  },
  "createdBy": "acme-user",
  "createdDate": "2022-08-03T13:59:51.000Z",
  "cspProfileName": "dev-api-csp-profile-mdp",
  "customerID": "acme",
  "id": "72e35c51-098e-4388-9055-2967bbd9be48",
  "lastModifiedBy": "acme-user",
  "lastModifiedDate": "2022-08-03T13:59:51.000Z",
  "projectName": "vz-cve",
  "type": "AWS"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 401 | Unauthorized. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 403 | Forbidden. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 429 | Too many requests. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| Default | Forbidden. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |


# Remove Cloud Credential

Remove a cloud credential from user's organization.

```python
def remove_cloud_credential(self,
                           account_name,
                           id,
                           correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `id` | `string` | Template, Required | CSP Profile Id. |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`EdgeServiceOnboardingDeleteResult`](../../doc/models/edge-service-onboarding-delete-result.md)

## Example Usage

```python
account_name = 'test_account1'

id = '72e35c51-098e-4388-9055-2967bbd9be48'

correlation_id = '9958f2f8-c4e3-46e0-8982-356de6515ae9'

result = csp_profiles_controller.remove_cloud_credential(
    account_name,
    id,
    correlation_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "message": "Csp Profile deleted Successfully",
  "subStatus": "Csp Profile Delete - success"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 404 | Not Found. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |

