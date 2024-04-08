
# V2 Add or Remove Device Result

Add or remove devices from the existing software upgrade information.

## Structure

`V2AddOrRemoveDeviceResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account identifier. |
| `campaign_id` | `str` | Required | Campaign identifier. |
| `request_id` | `str` | Required | Request identifier. |

## Example (as JSON)

```json
{
  "accountName": "0402196254-00001",
  "campaignId": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
  "requestId": "requestId6"
}
```

