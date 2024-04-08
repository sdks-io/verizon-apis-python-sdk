
# V1 Account Subscription

Account subscription information.

## Structure

`V1AccountSubscription`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Account identifier in "##########-#####". |
| `purchase_type` | `str` | Optional | Subscription models used by the account. |
| `license_count` | `int` | Optional | Number of monthly licenses in an MRC subscription. |
| `license_used_count` | `int` | Optional | Number of licenses currently assigned to devices. |
| `update_time` | `str` | Optional | The date and time of when the subscription was last updated. |

## Example (as JSON)

```json
{
  "accountName": "0402196254-00001",
  "purchaseType": "TS-HFOTA-EVNT,TS-HFOTA-MRC",
  "licenseCount": 9000,
  "licenseUsedCount": 1000,
  "updateTime": "2018-03-02T16:03:06.000Z"
}
```

