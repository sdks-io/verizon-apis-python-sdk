
# Data Center

## Structure

`DataCenter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `package_type` | [`DataCenterPackageTypeEnum`](../../doc/models/data-center-package-type-enum.md) | Optional | Packages are optimized for various operating environments. Prepackaged images are available in OVA and QCOW formats. |
| `distribution` | [`DataCenterDistributionEnum`](../../doc/models/data-center-distribution-enum.md) | Optional | Supported Kubernetes distribution for the selected cloud provider. |
| `location` | `string` | Optional | Indicate geo-location of cluster if you wish to use location based policies. |
| `k_8_s_version` | [`K8sVersionEnum`](../../doc/models/k8-s-version-enum.md) | Optional | Version of K8s platform.<br>**Default**: `'1.18'` |
| `operating_system` | `string` | Optional | Operating System for the master and worker nodes. |
| `tags` | [`List of EdgeServiceLaunchParams`](../../doc/models/edge-service-launch-params.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example (as JSON)

```json
{
  "packageType": "Linux",
  "distribution": "Upstream Kubernetes",
  "k8sVersion": "1.18",
  "tags": [
    {
      "key": "key",
      "value": "value"
    }
  ],
  "location": "location4",
  "operatingSystem": "operatingSystem4"
}
```

