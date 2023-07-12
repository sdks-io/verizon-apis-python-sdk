
# Aggregate Usage Item

Contains usage information per device.

## Structure

`AggregateUsageItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `imei` | `string` | Optional | International Mobile Equipment Identifier. This is the ID of the device reporting usage. |
| `number_of_sessions` | `int` | Optional | Number of sessions established by the device reporting usage. |
| `bytes_transferred` | `int` | Optional | The amount of data transferred by the device reporting usage, measured in Bytes. |
| `example` | `object` | Optional | - |

## Example (as JSON)

```json
{
  "imei": "709312034493372",
  "numberOfSessions": 1,
  "bytesTransferred": 2057,
  "example": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

