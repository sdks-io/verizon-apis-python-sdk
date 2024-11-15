
# Associate Label Request

## Structure

`AssociateLabelRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | The name of a billing account. An account name is usually numeric, and must include any leading zeros. |
| `labels` | [`AccountLabels`](../../doc/models/account-labels.md) | Required | Maximum of 2,000 objects are allowed in the array. |

## Example (as JSON)

```json
{
  "accountName": "1223334444-00001",
  "labels": {
    "devices": [
      {
        "deviceIds": [
          {
            "id": "id0",
            "kind": "kind8"
          }
        ]
      }
    ],
    "label": [
      {
        "name": "name0",
        "value": "value2"
      },
      {
        "name": "name0",
        "value": "value2"
      },
      {
        "name": "name0",
        "value": "value2"
      }
    ]
  }
}
```

