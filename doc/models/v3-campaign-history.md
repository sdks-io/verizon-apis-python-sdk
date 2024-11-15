
# V3 Campaign History

Campaign history.

## Structure

`V3CampaignHistory`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_more_data` | `bool` | Required | Has more report flag? |
| `last_seen_campaign_id` | `str` | Optional | Campaign identifier. |
| `campaign_list` | [`List[V3CampaignMetaInfo]`](../../doc/models/v3-campaign-meta-info.md) | Required | Firmware upgrade list. |

## Example (as JSON)

```json
{
  "hasMoreData": true,
  "lastSeenCampaignId": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
  "campaignList": [
    {
      "accountName": "0000123456-00001",
      "id": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
      "campaignName": "FOTA_Verizon_Upgrade",
      "make": "Verizon",
      "model": "Model-A",
      "status": "CampaignEnded",
      "startDate": "2020-08-21",
      "endDate": "2020-08-22",
      "campaignTimeWindowList": [
        {
          "startTime": 20,
          "endTime": 21
        }
      ],
      "firmwareName": "firmwareName6",
      "firmwareFrom": "firmwareFrom6",
      "firmwareTo": "firmwareTo6",
      "protocol": "LWM2M"
    }
  ]
}
```

