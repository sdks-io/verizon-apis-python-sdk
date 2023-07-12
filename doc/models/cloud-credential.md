
# Cloud Credential

## Structure

`CloudCredential`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | Name of the credentials. |
| `cluster_provisioning` | [`ClusterProvisioning`](../../doc/models/cluster-provisioning.md) | Optional | - |
| `data_backup` | [`DataBackup`](../../doc/models/data-backup.md) | Optional | - |

## Example (as JSON)

```json
{
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
      "accessId": "accessId0",
      "secretKey": "secretKey0",
      "sessionToken": "sessionToken2"
    },
    "role": {
      "accountId": "accountId2",
      "externalId": "externalId2",
      "roleARN": "roleARN4"
    }
  }
}
```

