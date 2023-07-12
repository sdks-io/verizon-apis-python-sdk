
# Intent Chain Item

## Structure

`IntentChainItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | - |
| `input` | `object` | Optional | - |

## Example (as JSON)

```json
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
```

