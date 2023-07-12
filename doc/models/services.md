
# Services

Response to get all services.

## Structure

`Services`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_records` | `int` | Optional | Will display the total number of records fetched.<br>**Constraints**: `<= 20480` |
| `service_res_list` | [`List of Service`](../../doc/models/service.md) | Optional | Response to fetch all services.<br>**Constraints**: *Maximum Items*: `2048` |

## Example (as JSON)

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
      ],
      "description": "description9",
      "metadata": [
        {
          "key": "key6",
          "value": "value8"
        },
        {
          "key": "key5",
          "value": "value7"
        },
        {
          "key": "key4",
          "value": "value6"
        }
      ]
    }
  ]
}
```

