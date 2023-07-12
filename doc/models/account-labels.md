
# Account Labels

Maximum of 2,000 objects are allowed in the array.

## Structure

`AccountLabels`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List of DeviceList`](../../doc/models/device-list.md) | Optional | - |
| `label` | [`List of DeviceLabels`](../../doc/models/device-labels.md) | Optional | - |

## Example (as JSON)

```json
{
  "devices": [
    {
      "deviceIds": [
        {
          "id": "id6",
          "kind": "imei"
        },
        {
          "id": "id7",
          "kind": "eid"
        },
        {
          "id": "id8",
          "kind": "esn"
        }
      ]
    },
    {
      "deviceIds": [
        {
          "id": "id7",
          "kind": "eid"
        }
      ]
    }
  ],
  "label": [
    {
      "name": "name5",
      "value": "value7"
    },
    {
      "name": "name6",
      "value": "value8"
    }
  ]
}
```

