
# Coordinates

Coordinates information.

## Structure

`Coordinates`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `latitude` | `str` | Optional | Latitude value of location.<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `12`, *Pattern*: `^[-+]?([0-9.]{3,12})$` |
| `longitude` | `str` | Optional | Longitude value of location.<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `12`, *Pattern*: `^[-+]?([0-9.]{3,12})$` |

## Example (as JSON)

```json
{
  "latitude": "-33.84819",
  "longitude": "151.22049"
}
```

