# Service Onboarding

```python
service_onboarding_controller = client.service_onboarding
```

## Class Name

`ServiceOnboardingController`

## Methods

* [Upload Service Workload File](../../doc/controllers/service-onboarding.md#upload-service-workload-file)
* [List Services](../../doc/controllers/service-onboarding.md#list-services)
* [Register Service](../../doc/controllers/service-onboarding.md#register-service)
* [List Service Details](../../doc/controllers/service-onboarding.md#list-service-details)
* [Remove Service](../../doc/controllers/service-onboarding.md#remove-service)
* [Start Service Onboarding](../../doc/controllers/service-onboarding.md#start-service-onboarding)
* [Get Service Job Status](../../doc/controllers/service-onboarding.md#get-service-job-status)
* [Start Service Claim Sand Box Testing](../../doc/controllers/service-onboarding.md#start-service-claim-sand-box-testing)
* [Start Service Publishing](../../doc/controllers/service-onboarding.md#start-service-publishing)
* [Stop Service Testing](../../doc/controllers/service-onboarding.md#stop-service-testing)
* [Mark Service as Ready for Public Use](../../doc/controllers/service-onboarding.md#mark-service-as-ready-for-public-use)


# Upload Service Workload File

Upload workload payload/package in the MEC platform.

```python
def upload_service_workload_file(self,
                                account_name,
                                service_name,
                                version,
                                category_type,
                                category_name,
                                payload,
                                correlation_id=None,
                                category_version=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `service_name` | `string` | Template, Required | Service name to which the file is going to be associated.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `version` | `string` | Template, Required | Version of the service being used.<br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9\.]+$` |
| `category_type` | [`CategoryTypeEnum`](../../doc/models/category-type-enum.md) | Query, Required | Type of the file being uploaded.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `category_name` | `string` | Query, Required | `workloadName` used in the service while creation.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `payload` | `typing.BinaryIO` | Form, Required | Payload/file which is to be uploaded should be provided in formData. |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |
| `category_version` | `string` | Query, Optional | It is mandatory for only service file, not mandatory for workload and workflow file.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[0-9\.]+$` |

## Response Type

[`ServiceFile`](../../doc/models/service-file.md)

## Example Usage

```python
account_name = 'test_account1'

service_name = 'doccheck'

version = '1.0.0'

category_type = CategoryTypeEnum.GENERAL_VALIDATION

category_name = 'gst-server-workload'

payload = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

correlation_id = '9958f2f8-c4e3-46e0-8982-356de6515ae9'

category_version = '1.0.0'

result = service_onboarding_controller.upload_service_workload_file(
    account_name,
    service_name,
    version,
    category_type,
    category_name,
    payload,
    correlation_id,
    category_version
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "uuid",
  "serviceName": "gst-server",
  "serviceVersion": "1.0.0",
  "file": "values.yaml",
  "categoryName": "gst-server-workload",
  "categoryVersion": "1.0.0",
  "categoryType": "WORKLOAD_VALUES",
  "validationStatus": "Validation Success",
  "createdDate": "2006-01-02T15:04:05Z",
  "lastModifiedDate": "2006-01-02T15:04:05Z",
  "createdBy": "User",
  "updatedBy": "User"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 401 | Unauthorized. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 404 | Not found. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |


# List Services

Fetch all organizational services in the platform.

```python
def list_services(self,
                 account_name,
                 correlation_id=None,
                 name=None,
                 q=None,
                 limit=None,
                 off_set=None,
                 sort_key='createdDate',
                 sort_dir=None,
                 details_flag=True)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |
| `name` | `string` | Query, Optional | Name of the service whose information needs to be fetched.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `q` | `string` | Query, Optional | Use the comma (:) character to separate multiple values eg type=myService:workloads.packageType=Helm,YAML:state=DRAFTED,VALIDATION_COMPLETED.<br>**Constraints**: *Maximum Length*: `2048`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!\/,+\-=_:.&*%\s]+$` |
| `limit` | `long\|int` | Query, Optional | Number of items to return.<br>**Constraints**: `>= 0`, `<= 1024` |
| `off_set` | `long\|int` | Query, Optional | Id of the last respose value in the previous list.<br>**Constraints**: `>= 0`, `<= 1024` |
| `sort_key` | `string` | Query, Optional | Sorts the response by an attribute. Default is createdDate.<br>**Default**: `'createdDate'`<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `sort_dir` | [`SortDirectionEnum`](../../doc/models/sort-direction-enum.md) | Query, Optional | Sorts the response. Use asc for ascending or desc for descending order. The default is desc.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `details_flag` | `bool` | Query, Optional | Default as true. If it is true, then it will return all details.<br>**Default**: `True` |

## Response Type

[`Services`](../../doc/models/services.md)

## Example Usage

```python
account_name = 'test_account1'

correlation_id = '9958f2f8-c4e3-46e0-8982-356de6515ae9'

name = 'dev-api-test-service-mdp-1'

q = 'type=myService:workloads.packageType=Helm,YAML:state=DRAFTED,VALIDATION_COMPLETED'

limit = 256

off_set = 255

sort_key = 'createdDate'

sort_dir = SortDirectionEnum.DESC

details_flag = True

result = service_onboarding_controller.list_services(
    account_name,
    correlation_id,
    name,
    q,
    limit,
    off_set,
    sort_key,
    sort_dir,
    details_flag
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "totalRecords": 1,
  "serviceResList": [
    {
      "boundaries": [],
      "categories": [
        "MongodbSensor"
      ],
      "compatibility": [
        {
          "csp": "AWS_WL"
        }
      ],
      "createdBy": "acme-user",
      "createdDate": "2022-08-03T13:31:52.000Z",
      "error": {},
      "errorResponse": {},
      "id": "b32321d2-4ee3-458b-a70b-e956525d46c9",
      "lastModifiedBy": "acme-user",
      "lastModifiedDate": "2022-08-03T13:31:52.000Z",
      "name": "dev-api-test-service-mdp-1",
      "state": "DRAFT",
      "status": "DRAFT_INPROGRESS",
      "tags": [
        {
          "key": "vnsp.mec.verizon.com/servicetype",
          "value": "My service"
        }
      ],
      "type": "MY_SERVICE",
      "version": "1.0.0",
      "workloads": [
        {
          "createdBy": "acme-user",
          "createdDate": "2022-08-03T13:31:52.000Z",
          "description": "MEC SD Workload.",
          "files": [],
          "helmHelmrepo": {
            "helmChartName": "mongodb",
            "helmChartVersion": "12.1.10"
          },
          "id": "cf5e0af0-0dfc-4b6b-be95-08fc28e5f4ad",
          "lastModifiedDte": "0001-01-01T00:00:00.000Z",
          "name": "dev-api-demo-repo",
          "packageType": "HELM",
          "repositoryType": "HELM",
          "updatedBy": "acme-user",
          "uploadType": "PULL_FROM_REPO"
        }
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 401 | Unauthorized. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 404 | Not Found. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |


# Register Service

Create a new service within user's organization.

```python
def register_service(self,
                    account_name,
                    body,
                    correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `body` | [`Service`](../../doc/models/service.md) | Body, Required | - |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`Service`](../../doc/models/service.md)

## Example Usage

```python
account_name = 'test_account1'

body = Service(
    name='dev-api-test-service-mdp-1',
    version='1.0.0',
    tags=[
        ServiceTag(
            key='vnsp.mec.verizon.com/servicetype',
            value='My service'
        )
    ],
    categories=[
        'MongodbSensor'
    ],
    compatibility=[
        Compatibility(
            csp=CSPCompatibilityEnum.AWS_WL
        )
    ],
    mtype=ServiceTypeEnum.MY_SERVICE,
    workloads=[
        Workload(
            name='dev-api-demo-repo',
            description='MEC SD Workload.',
            package_type=ServiceDependencyPackageTypeEnum.HELM,
            upload_type=UploadTypeEnum.PULL_FROM_REPO,
            repository_type=WorkloadRepositoryTypeEnum.HELM,
            helm_helmrepo=ServiceOnboardingHelmHelmrepo(
                helm_chart_name='mongodb',
                helm_chart_version='12.1.10'
            )
        )
    ]
)

correlation_id = '9958f2f8-c4e3-46e0-8982-356de6515ae9'

result = service_onboarding_controller.register_service(
    account_name,
    body,
    correlation_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "categories": [
    "MongodbSensor"
  ],
  "compatibility": [
    {
      "csp": "AWS_WL"
    }
  ],
  "createdBy": "acme-user",
  "createdDate": "2022-08-03T13:31:52.000Z",
  "error": {},
  "errorResponse": {},
  "id": "b32321d2-4ee3-458b-a70b-e956525d46c9",
  "lastModifiedBy": "acme-user",
  "lastModifiedDate": "2022-08-03T13:31:52.000Z",
  "name": "dev-api-test-service-mdp-1",
  "tags": [
    {
      "key": "services.mec.verizon.com/servicetype",
      "value": "My service"
    }
  ],
  "type": "MY_SERVICE",
  "version": "1.0.0",
  "workloads": [
    {
      "createdBy": "acme-user",
      "createdDate": "2022-08-03T13:31:52.000Z",
      "description": "MEC SD Workload.",
      "helmHelmrepo": {
        "helmChartName": "mongodb",
        "helmChartVersion": "12.1.10"
      },
      "id": "cf5e0af0-0dfc-4b6b-be95-08fc28e5f4ad",
      "lastModifiedDte": "2022-08-03T13:31:52.000Z",
      "name": "dev-api-demo-repo",
      "packageType": "HELM",
      "repositoryType": "HELM",
      "updatedBy": "acme-user",
      "uploadType": "PULL_FROM_REPO"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 401 | Unauthorized. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 403 | Forbidden. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 404 | Not found. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 415 | Unsupported media type. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 429 | Too many requests. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |


# List Service Details

Fetch a service details within user's organization using service name and version.

```python
def list_service_details(self,
                        account_name,
                        service_name,
                        version,
                        correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `service_name` | `string` | Template, Required | Name of the service whose information needs to be fetched.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `version` | `string` | Template, Required | Version of service whose information needs to be fetched.<br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9\.]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`Service`](../../doc/models/service.md)

## Example Usage

```python
account_name = 'test_account1'

service_name = 'dev-api-test-service-mdp-1'

version = '1.0.0'

correlation_id = '9958f2f8-c4e3-46e0-8982-356de6515ae9'

result = service_onboarding_controller.list_service_details(
    account_name,
    service_name,
    version,
    correlation_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "categories": [
    "MongodbSensor"
  ],
  "compatibility": [
    {
      "csp": "AWS_WL"
    }
  ],
  "createdBy": "acme-user",
  "createdDate": "2022-08-03T13:31:52.000Z",
  "error": {},
  "errorResponse": {},
  "id": "b32321d2-4ee3-458b-a70b-e956525d46c9",
  "lastModifiedBy": "acme-user",
  "lastModifiedDate": "2022-08-03T13:31:52.000Z",
  "name": "dev-api-test-service-mdp-1",
  "tags": [
    {
      "key": "services.mec.verizon.com/servicetype",
      "value": "My service"
    }
  ],
  "type": "MY_SERVICE",
  "version": "1.0.0",
  "workloads": [
    {
      "createdBy": "acme-user",
      "createdDate": "2022-08-03T13:31:52.000Z",
      "description": "MEC SD Workload.",
      "helmHelmrepo": {
        "helmChartName": "mongodb",
        "helmChartVersion": "12.1.10"
      },
      "id": "cf5e0af0-0dfc-4b6b-be95-08fc28e5f4ad",
      "lastModifiedDte": "2022-08-03T13:31:52.000Z",
      "name": "dev-api-demo-repo",
      "packageType": "HELM",
      "repositoryType": "HELM",
      "updatedBy": "acme-user",
      "uploadType": "PULL_FROM_REPO"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 401 | Unauthorized. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 404 | Not Found. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| Default | Unexpected error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |


# Remove Service

Remove a service from user's organization.

```python
def remove_service(self,
                  account_name,
                  service_name,
                  version,
                  correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `service_name` | `string` | Template, Required | Name of the service which is about to be deleted.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `version` | `string` | Template, Required | Version of the service which is about to be deleted.<br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9\.]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`EdgeServiceOnboardingDeleteResult`](../../doc/models/edge-service-onboarding-delete-result.md)

## Example Usage

```python
account_name = 'test_account1'

service_name = 'dev-api-test-service-mdp-1'

version = '1.0.0'

correlation_id = '9958f2f8-c4e3-46e0-8982-356de6515ae9'

result = service_onboarding_controller.remove_service(
    account_name,
    service_name,
    version,
    correlation_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "message": "service deleted succesfully",
  "subStatus": "service delete - success"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 404 | Not found. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |


# Start Service Onboarding

Start service onboarding process to kick off service artifact validation and making the service ready for sandbox testing. On successful completion of this process system will generate claims for each selected cloud provider using which user can start sandbox testing.

```python
def start_service_onboarding(self,
                            account_name,
                            service_name,
                            version,
                            correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `service_name` | `string` | Template, Required | Name of the service which is to be onboarded.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `version` | `string` | Template, Required | Version of service which is to be onboarded.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9\.]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`ServiceManagementResult`](../../doc/models/service-management-result.md)

## Example Usage

```python
account_name = 'test_account1'

service_name = 'dev-api-test-service-mdp-1'

version = '1.0.0'

correlation_id = '9958f2f8-c4e3-46e0-8982-356de6515ae9'

result = service_onboarding_controller.start_service_onboarding(
    account_name,
    service_name,
    version,
    correlation_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "jobId": "0c6e8560-e154-40f9-961e-28da3698436d",
  "status": "Inprogress",
  "state": "DRAFT"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 401 | Unauthorized. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 403 | Forbidden. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 404 | Not found. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 415 | Unsupported media type. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 429 | Too many requests. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |


# Get Service Job Status

Check current status of job for a service using job ID.

```python
def get_service_job_status(self,
                          account_name,
                          job_id,
                          correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `job_id` | `string` | Template, Required | Auto-generated Id of the job.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9_-]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`CurrentStatus`](../../doc/models/current-status.md)

## Example Usage

```python
account_name = 'test_account1'

job_id = '0c6e8560-e154-40f9-961e-28da3698436d'

correlation_id = '9958f2f8-c4e3-46e0-8982-356de6515ae9'

result = service_onboarding_controller.get_service_job_status(
    account_name,
    job_id,
    correlation_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "status": "STARTED"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 404 | Not found. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |


# Start Service Claim Sand Box Testing

Initiate testing of a service in sandbox environment per claim based on service's compatibility(s).

```python
def start_service_claim_sand_box_testing(self,
                                        account_name,
                                        service_id,
                                        claim_id,
                                        body,
                                        correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `service_id` | `string` | Template, Required | An id of the service created e.g. UUID.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `claim_id` | `string` | Template, Required | Id of the claim created e.g. UUID.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `body` | [`ClusterInfoDetails`](../../doc/models/cluster-info-details.md) | Body, Required | - |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`ServiceManagementResult`](../../doc/models/service-management-result.md)

## Example Usage

```python
account_name = 'test_account1'

service_id = 'b32321d2-4ee3-458b-a70b-e956525d46c9'

claim_id = '58296746-57ee-44f8-8107-399b61d58356'

body = ClusterInfoDetails(
    cluster_name='ctc-1',
    namespace='default'
)

correlation_id = '9958f2f8-c4e3-46e0-8982-356de6515ae9'

result = service_onboarding_controller.start_service_claim_sand_box_testing(
    account_name,
    service_id,
    claim_id,
    body,
    correlation_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "jobId": "0c6e8560-e154-40f9-961e-28da3698436d",
  "status": "Inprogress",
  "state": "DRAFT"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 401 | Unauthorized. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| Default | Unexpected error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |


# Start Service Publishing

Start publishing a service. On successful completion, service's status can be marked as Publish.

```python
def start_service_publishing(self,
                            account_name,
                            service_name,
                            version,
                            correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `service_name` | `string` | Template, Required | Name of the service e.g. any sub string of serviceName.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `version` | `string` | Template, Required | Version of service which is to be published.<br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9\.]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`ServiceManagementResult`](../../doc/models/service-management-result.md)

## Example Usage

```python
account_name = 'test_account1'

service_name = 'dev-api-test-service-mdp-1'

version = '1.0.0'

correlation_id = '9958f2f8-c4e3-46e0-8982-356de6515ae9'

result = service_onboarding_controller.start_service_publishing(
    account_name,
    service_name,
    version,
    correlation_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "jobId": "0c6e8560-e154-40f9-961e-28da3698436d",
  "status": "Inprogress",
  "state": "DRAFT"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 401 | Unauthorized. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| Default | Unexpected error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |


# Stop Service Testing

Start service certification process. On successful completion of this process, service's status will change to certified.

```python
def stop_service_testing(self,
                        account_name,
                        service_name,
                        version,
                        correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `service_name` | `string` | Template, Required | Name of the service e.g. any sub string of serviceName.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `version` | `string` | Template, Required | Version of service which is to be certified.<br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9\.]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`ServiceManagementResult`](../../doc/models/service-management-result.md)

## Example Usage

```python
account_name = 'test_account1'

service_name = 'dev-api-test-service-mdp-1'

version = '1.0.0'

correlation_id = '9958f2f8-c4e3-46e0-8982-356de6515ae9'

result = service_onboarding_controller.stop_service_testing(
    account_name,
    service_name,
    version,
    correlation_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "jobId": "0c6e8560-e154-40f9-961e-28da3698436d",
  "status": "Inprogress",
  "state": "DRAFT"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 401 | Unauthorized. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| Default | Unexpected error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |


# Mark Service as Ready for Public Use

Start the process to change a service's status to "Ready to Use". On success, service's status will be changed to "Ready to Use". Only a ready to use service can be deployed in production environment.

```python
def mark_service_as_ready_for_public_use(self,
                                        account_name,
                                        service_name,
                                        version,
                                        correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `service_name` | `string` | Template, Required | Name of the service e.g. any sub string of serviceName.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `version` | `string` | Template, Required | Version of the service which is already certified and is ready for public use.<br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9\.]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`ServiceManagementResult`](../../doc/models/service-management-result.md)

## Example Usage

```python
account_name = 'test_account1'

service_name = 'dev-api-test-service-mdp-1'

version = '1.0.0'

correlation_id = '9958f2f8-c4e3-46e0-8982-356de6515ae9'

result = service_onboarding_controller.mark_service_as_ready_for_public_use(
    account_name,
    service_name,
    version,
    correlation_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "jobId": "0c6e8560-e154-40f9-961e-28da3698436d",
  "status": "Inprogress",
  "state": "DRAFT"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 401 | Unauthorized. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| 500 | Internal Server Error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |
| Default | Unexpected error. | [`EdgeServiceOnboardingResultErrorException`](../../doc/models/edge-service-onboarding-result-error-exception.md) |

