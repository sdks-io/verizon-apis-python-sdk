
# Attribute Setting

Describes an attribute being observed and the frequency with which the attribute is being observed.

## Structure

`AttributeSetting`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | [`AttributeIdentifierEnum`](../../doc/models/attribute-identifier-enum.md) | Optional | Attribute identifier. |
| `value` | `str` | Optional | Attribute value. |
| `created_on` | `datetime` | Optional | Date and time request was created. |
| `is_observable` | `bool` | Optional | Is the attribute observable? |
| `is_observing` | `bool` | Optional | Is the attribute being observed? |
| `frequency` | [`NumericalData`](../../doc/models/numerical-data.md) | Optional | Describes value and unit of time. |

## Example (as JSON)

```json
{
  "name": "MANUFACTURER",
  "value": "string",
  "createdOn": "2019-09-07T23:08:03.532Z",
  "isObservable": true,
  "isObserving": true,
  "frequency": {
    "value": 5,
    "unit": "SECOND"
  }
}
```

