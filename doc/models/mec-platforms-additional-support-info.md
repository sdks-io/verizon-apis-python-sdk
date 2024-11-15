
# MEC Platforms Additional Support Info

Additional service support information for the MEC platform.

## Structure

`MECPlatformsAdditionalSupportInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | Type of additional service support information for the MEC platform.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `data` | [`MECPlatformsAdditionalSupportInfoData`](../../doc/models/mec-platforms-additional-support-info-data.md) | Optional | Data about additional service support information for the MEC platform. |

## Example (as JSON)

```json
{
  "type": "type8",
  "data": {
    "additionalInfo": "additionalInfo2"
  }
}
```

