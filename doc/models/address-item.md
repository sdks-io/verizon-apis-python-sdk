
# Address Item

Address details.

## Structure

`AddressItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_line_1` | `str` | Optional | Street Address.<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9 ,]{3,32}$` |
| `address_line_2` | `str` | Optional | Optional address information.<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9 ,]{3,32}$` |
| `city` | `str` | Optional | Name of the city.<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9 ]{3,32}$` |
| `state` | `str` | Optional | State code.<br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `3`, *Pattern*: `^[A-Za-z]{2,3}$` |
| `country` | `str` | Optional | Country.<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3`, *Pattern*: `^[A-Za-z]{3,3}$` |
| `zip` | `str` | Optional | Five digit zipcode.<br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `5`, *Pattern*: `^[0-9]{5,5}$` |
| `zip_4` | `str` | Optional | Four digit zip code.<br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `4`, *Pattern*: `^[0-9]{4,4}$` |

## Example (as JSON)

```json
{
  "addressLine1": "street number and name",
  "addressLine2": "optional address information",
  "city": "name of the city",
  "state": "NY",
  "country": "USA",
  "zip": "10001",
  "zip4": "0727"
}
```

