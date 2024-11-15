
# Fall Back

## Structure

`FallBack`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List[DeviceIdarray]`](../../doc/models/device-idarray.md) | Optional | An array containing the `deviceId` array.<br>**Constraints**: *Maximum Items*: `100` |
| `account_name` | `str` | Optional | The numeric name of the account, in the format "0000123456-00001". Leading zeros must be included.<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9]{3,32}$` |

## Example (as JSON)

```json
{
  "devices": [
    [
      {
        "kind": "kind2",
        "id": "id4"
      },
      {
        "kind": "kind2",
        "id": "id4"
      }
    ],
    [
      {
        "kind": "kind2",
        "id": "id4"
      },
      {
        "kind": "kind2",
        "id": "id4"
      }
    ]
  ],
  "accountName": "accountName4"
}
```

