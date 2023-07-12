
# Service Resource

Resource of the service.

## Structure

`ServiceResource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `compute_resources` | [`ResourceBase`](../../doc/models/resource-base.md) | Optional | Resource Base of the service. |
| `gpu_required` | `bool` | Optional | GPU required or not for onboarding service.<br>**Default**: `False` |
| `gpu` | [`ResourceBase`](../../doc/models/resource-base.md) | Optional | Resource Base of the service. |
| `storage` | [`ResourceBase`](../../doc/models/resource-base.md) | Optional | Resource Base of the service. |
| `memory` | [`ResourceBase`](../../doc/models/resource-base.md) | Optional | Resource Base of the service. |
| `latency` | [`ResourceBase`](../../doc/models/resource-base.md) | Optional | Resource Base of the service. |
| `request_rate` | [`ResourceBase`](../../doc/models/resource-base.md) | Optional | Resource Base of the service. |
| `bandwidth` | [`ResourceBase`](../../doc/models/resource-base.md) | Optional | Resource Base of the service. |

## Example (as JSON)

```json
{
  "storage": {
    "unit": "MB",
    "value": 512,
    "max": 1024,
    "min": 256
  },
  "memory": {
    "unit": "MB",
    "value": 200,
    "max": 400,
    "min": 10
  },
  "computeResources": {
    "unit": "unit6",
    "value": 34,
    "max": 64,
    "min": 146
  },
  "gpuRequired": false,
  "gpu": {
    "unit": "unit0",
    "value": 44,
    "max": 74,
    "min": 156
  }
}
```

