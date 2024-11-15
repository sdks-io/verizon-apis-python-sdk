
# Compute Resources Type

Compute resources of a service profile.

## Structure

`ComputeResourcesType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gpu` | [`GPU`](../../doc/models/gpu.md) | Optional | GPU resources of a service profile. |
| `min_ramgb` | `int` | Optional | Minimum RAM required in Gigabytes.<br>**Constraints**: `>= 1`, `<= 100` |
| `min_storage_gb` | `int` | Optional | Minimum storage requirement in Gigabytes.<br>**Constraints**: `>= 1`, `<= 100` |

## Example (as JSON)

```json
{
  "minRAMGB": 1,
  "minStorageGB": 1,
  "GPU": {
    "minCoreClockMHz": 76,
    "minMemoryClockMHz": 20,
    "minBandwidthGBs": 96,
    "minTFLOPS": 100
  }
}
```

