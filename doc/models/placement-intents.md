
# Placement Intents

## Structure

`PlacementIntents`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `is_placement_at_launch_enabled` | `bool` | Optional | **Default**: `False` |
| `group_id` | `string` | Optional | **Constraints**: *Maximum Length*: `500`, *Pattern*: `^(.*)$` |
| `intent_chain` | [`List of IntentChainItem`](../../doc/models/intent-chain-item.md) | Optional | - |

## Example (as JSON)

```json
{
  "intentChain": [
    {
      "input": {
        "deploymentLocations": [
          {
            "csp": "AWS_WL",
            "region": "US_WEST_2",
            "zoneId": [
              "us-west-2-wl1-den-wlz-1"
            ]
          }
        ]
      },
      "name": "Compliance"
    }
  ],
  "isPlacementAtLaunchEnabled": false,
  "groupId": "groupId2"
}
```

