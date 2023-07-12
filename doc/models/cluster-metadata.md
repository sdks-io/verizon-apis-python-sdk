
# Cluster Metadata

## Structure

`ClusterMetadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | Name of the cluster to be used.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `description` | `string` | Optional | Description of the cluster.<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-\s]{1,500}$` |
| `cluster_type` | [`ClusterTypeEnum`](../../doc/models/cluster-type-enum.md) | Optional | - |
| `cloud` | [`Cloud`](../../doc/models/cloud.md) | Optional | - |
| `data_center` | [`DataCenter`](../../doc/models/data-center.md) | Optional | - |
| `labels` | [`List of EdgeServiceLaunchParams`](../../doc/models/edge-service-launch-params.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `ingress_ips` | [`ServiceLaunchClusterAdditionalParams`](../../doc/models/service-launch-cluster-additional-params.md) | Optional | - |
| `upgrade_protection` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "cloud": {
    "clusterConfig": {
      "autoCreateNetworkInfra": true,
      "networkNatMode": "single",
      "tags": {
        "key": "key8",
        "value": "value0"
      },
      "endPointAccessType": "privatePublicAccess",
      "infraIPv4range": "infraIPv4range8"
    },
    "commonConfig": {
      "blueprint": {
        "name": "default",
        "version": "latest"
      },
      "cloudCredentials": {
        "clusterProvisioning": {
          "provider": "AWS",
          "accessKey": {
            "accessId": "accessId4",
            "secretKey": "secretKey4",
            "sessionToken": "sessionToken6"
          },
          "role": {
            "accountId": "accountId8",
            "externalId": "externalId6",
            "roleARN": "roleARN0"
          }
        },
        "name": "acme-aws-qa-mdp-5",
        "dataBackup": {
          "provider": "AWS",
          "accessKey": {
            "accessId": "accessId4",
            "secretKey": "secretKey4",
            "sessionToken": "sessionToken6"
          },
          "role": {
            "accountId": "accountId8",
            "externalId": "externalId6",
            "roleARN": "roleARN0"
          }
        }
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
    ],
    "provider": "GCP",
    "nodeConfig": {
      "name": "name2",
      "isWavelengthZone": false,
      "isManagedNodeGroup": false,
      "isSpotInstanceNeeded": false,
      "endPointAccessType": "private"
    }
  },
  "clusterType": "publicCloud",
  "description": "Cluster Details.",
  "name": "dev-acme-aws-us-west-2-wl1-den-wlz-1",
  "dataCenter": {
    "packageType": "QCOW2",
    "distribution": "Upstream Kubernetes",
    "location": "location4",
    "k8sVersion": "1.18",
    "operatingSystem": "operatingSystem4"
  }
}
```

