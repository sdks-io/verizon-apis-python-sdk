
# Consent Request

## Structure

`ConsentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Optional | Account identifier in "##########-#####". |
| `all_device` | `bool` | Optional | Exclude all devices or not. |
| `mtype` | `string` | Optional | The change to make: append or replace. |
| `exclusion` | `List of string` | Optional | Device ID list. |

## Example (as JSON)

```json
{
  "accountName": "1234567890-00001",
  "type": "replace",
  "allDevice": false,
  "exclusion": [
    "980003420535573",
    "375535024300089",
    "A100003861E585"
  ]
}
```

