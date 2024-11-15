
# GPU

GPU resources of a service profile.

## Structure

`GPU`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `min_core_clock_m_hz` | `int` | Optional | Minimum Core Clock value in megahertz.<br>**Constraints**: `>= 1`, `<= 10000` |
| `min_memory_clock_m_hz` | `int` | Optional | Minimum Memory Clock value in megahertz.<br>**Constraints**: `>= 1`, `<= 100000` |
| `min_bandwidth_g_bs` | `int` | Optional | Minimum GPU bandwidth in GB/s.<br>**Constraints**: `>= 1`, `<= 1000` |
| `min_tflops` | `int` | Optional | Minimum Floating Point Operations Per Second in Teraflops.<br>**Constraints**: `>= 1`, `<= 100` |

## Example (as JSON)

```json
{
  "minCoreClockMHz": 1,
  "minMemoryClockMHz": 35740,
  "minBandwidthGBs": 588,
  "minTFLOPS": 33
}
```

