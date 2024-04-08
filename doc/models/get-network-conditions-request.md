
# Get Network Conditions Request

Get network conditions.

## Structure

`GetNetworkConditionsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account name.<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9-]{3,32}$` |
| `location_type` | `str` | Required | Type of location detail.<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `10`, *Pattern*: `^[A-Za-z]{3,10}$` |
| `coordinates` | [`Coordinates`](../../doc/models/coordinates.md) | Required | Coordinates information. |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "locationType": "LONGLAT",
  "coordinates": {
    "latitude": "-33.84819",
    "longitude": "151.22049"
  }
}
```

