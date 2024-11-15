
# Daily Usage History

## Structure

`DailyUsageHistory`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bytes_used` | `str` | Optional | the total data usage recorded in Bytes<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `32`, *Pattern*: `^[0-9]{1,32}$` |
| `extended_attributes` | [`List[ExtendedAttribute]`](../../doc/models/extended-attribute.md) | Optional | - |
| `service_plan` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `sms_used` | `str` | Optional | The total number of SMS messages from and to the device<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `32`, *Pattern*: `^[0-9]{1,32}$` |
| `source` | `str` | Optional | Where the collected data is being gathered from<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `timestamp` | `str` | Optional | Timestamp of when the retrieved record was completed ($datetime)<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |

## Example (as JSON)

```json
{
  "bytesUsed": "123456",
  "smsUsed": "5",
  "extendedAttributes": [
    {
      "key": "key8",
      "value": "value0"
    },
    {
      "key": "key8",
      "value": "value0"
    },
    {
      "key": "key8",
      "value": "value0"
    }
  ],
  "servicePlan": "servicePlan6",
  "source": "source2"
}
```

