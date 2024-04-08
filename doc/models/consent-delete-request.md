
# Consent Delete Request

## Structure

`ConsentDeleteRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Account identifier. |
| `device_list` | `List[str]` | Optional | Device ID list. |

## Example (as JSON)

```json
{
  "accountName": "MyAccount-1",
  "deviceList": [
    "deviceList2",
    "deviceList3"
  ]
}
```

