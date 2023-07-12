
# Common Configuration

## Structure

`CommonConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cloud_credentials` | [`CloudCredential`](../../doc/models/cloud-credential.md) | Optional | - |
| `k_8_s_version` | [`K8sVersionEnum`](../../doc/models/k8-s-version-enum.md) | Optional | Version of K8s platform.<br>**Default**: `'1.18'` |
| `blueprint` | [`Blueprint`](../../doc/models/blueprint.md) | Optional | - |

## Example (as JSON)

```json
{
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
        "accountId": "accountId2",
        "externalId": "externalId6",
        "roleARN": "roleARN0"
      }
    },
    "name": "acme-aws-qa-mdp-5",
    "dataBackup": {
      "provider": "AWS",
      "accessKey": {
        "accessId": "accessId8",
        "secretKey": "secretKey8",
        "sessionToken": "sessionToken0"
      },
      "role": {
        "accountId": "accountId4",
        "externalId": "externalId0",
        "roleARN": "roleARN6"
      }
    }
  },
  "k8sVersion": "1.21"
}
```

