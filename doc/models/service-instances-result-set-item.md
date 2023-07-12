
# Service Instances Result Set Item

## Structure

`ServiceInstancesResultSetItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status_url` | `string` | Optional | URL to check the status of the add service.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `request_id` | `string` | Optional | A unique Id assigned to the request by system calling API.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `correlation_id` | `string` | Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `status` | `string` | Optional | Status of the added service.<br>**Constraints**: *Maximum Length*: `50`, *Pattern*: `^[A-Za-z\s_\-]{1,50}$` |
| `state` | `string` | Optional | State of the service instance.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `service` | [`ServiceInstance`](../../doc/models/service-instance.md) | Optional | - |

## Example (as JSON)

```json
{
  "service": {
    "clusterInfo": {
      "cloud": {
        "clusterConfig": {
          "autoCreateNetworkInfra": true,
          "networkNatMode": "single"
        },
        "commonConfig": {
          "blueprint": {
            "name": "default",
            "version": "latest"
          },
          "cloudCredentials": {
            "clusterProvisioning": {
              "provider": "AWS"
            },
            "name": "acme-aws-qa-mdp-5"
          },
          "k8sVersion": "1.21"
        },
        "distribution": "AmazonEKS",
        "nodeConfigs": [
          {
            "autoCreateServiceRoles": true,
            "enableAlbAccess": true,
            "enableAppMeshAccess": true,
            "enableAsgAccess": true,
            "enableDnsAccess": true,
            "enableEfsAccess": true,
            "enableFullAccessToEcr": true,
            "endPointAccessType": "private",
            "instanceType": "m5.xlarge",
            "isManagedNodeGroup": false,
            "isSpotInstanceNeeded": false,
            "isWavelengthZone": false,
            "labels": {},
            "name": "ng-22",
            "nodeAmiFamily": "AmazonLinux2",
            "nodePrivateNetworking": false,
            "nodeVolumeSize": 80,
            "nodeVolumeType": "gp3",
            "nodes": 2,
            "nodesMax": 2,
            "nodesMin": 2,
            "tags": {},
            "useVolumeEncryption": true
          },
          {
            "autoCreateServiceRoles": true,
            "enableAlbAccess": true,
            "enableAppMeshAccess": true,
            "enableAsgAccess": true,
            "enableDnsAccess": true,
            "enableEfsAccess": true,
            "enableFullAccessToEcr": true,
            "endPointAccessType": "private",
            "instanceType": "t3.xlarge",
            "isManagedNodeGroup": false,
            "isSpotInstanceNeeded": false,
            "isWavelengthZone": true,
            "labels": {},
            "name": "ng-wavelength-test22",
            "nodeAmiFamily": "AmazonLinux2",
            "nodePrivateNetworking": false,
            "nodeVolumeSize": 80,
            "nodeVolumeType": "gp2",
            "nodes": 2,
            "nodesMax": 2,
            "nodesMin": 2,
            "subnetCidrBlock": "192.168.192.0/19",
            "tags": {},
            "useVolumeEncryption": true
          }
        ]
      },
      "clusterType": "publicCloud",
      "description": "Cluster Details.",
      "name": "dev-acme-aws-us-west-2-wl1-den-wlz-1"
    },
    "createdAt": "2022-08-19T13:07:42.560Z",
    "customerId": "acme",
    "deploymentType": "PublicMEC",
    "id": "e0abe65f-b294-4673-a60c-d31f26ca7a8c",
    "labels": {},
    "modifiedAt": "2022-08-19T13:07:42.560Z",
    "name": "mongodb-customer-prerun-2",
    "nameSpace": "default",
    "projectName": "vesa-pi7-pubmec-dev-proj",
    "revision": {
      "additionalParams": [],
      "version": "2.3.4"
    },
    "serviceName": "mongodb-customer-prerun-2",
    "solutionRegulations": [
      {
        "region": "us-west-2",
        "zones": [
          {
            "zone": "us-west-2-wl1-den-wlz-1"
          }
        ]
      }
    ],
    "userId": "acme-user",
    "workLoadType": "container"
  },
  "state": "READY",
  "status": "SERVICE_INSTANCE_LAUNCH - SUCCESS",
  "statusUrl": "statusUrl6",
  "requestId": "requestId2",
  "correlationId": "correlationId0"
}
```

