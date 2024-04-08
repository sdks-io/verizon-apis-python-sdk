
# Devices Consent Result

## Structure

`DevicesConsentResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Account identifier in "##########-#####". |
| `all_device` | `bool` | Optional | Exclude all devices or not? |
| `has_more_data` | `bool` | Optional | Are there more devices to retrieve or not? |
| `total_count` | `int` | Optional | Total number of excluded devices in the account. |
| `update_time` | `str` | Optional | Last update time. |
| `exclusion` | `List[str]` | Optional | Device ID list. |

## Example (as JSON)

```json
{
  "accountName": "2024009649-00001",
  "allDevice": false,
  "hasMoreData": false,
  "totalCount": 4,
  "updateTime": "2018-05-18 19:20:50.076 +0000 UTC",
  "exclusion": [
    "990003420535375",
    "420535399000375",
    "A100003861E585",
    "205353759900034"
  ]
}
```

