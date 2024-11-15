
# Triggervalues 2

## Structure

`Triggervalues2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `str` | Optional | - |
| `trigger_name` | `str` | Optional | - |
| `account_name` | `str` | Optional | - |
| `organization_name` | `str` | Optional | - |
| `trigger_category` | `str` | Optional | - |
| `promo_alerts` | [`List[PromoAlert]`](../../doc/models/promo-alert.md) | Optional | - |
| `active` | `bool` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `modified_at` | `datetime` | Optional | - |

## Example (as JSON)

```json
{
  "triggerId": "2874DEC7-26CF-4797-9C6A-B5A2AC72D526",
  "triggerName": "PromoAlerts_0000000000-00001_23456789",
  "accountName": "0000123456-000001",
  "organizationName": "Optional group name",
  "triggerCategory": "PromoAlerts"
}
```

