
# Profile Request

## Structure

`ProfileRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List of DeviceList`](../../doc/models/device-list.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `carrier_name` | `string` | Optional | - |
| `account_name` | `string` | Optional | - |
| `service_plan` | `string` | Optional | - |
| `mdn_zip_code` | `string` | Optional | - |
| `primary_place_of_use` | [`List of PrimaryPlaceOfUse`](../../doc/models/primary-place-of-use.md) | Optional | **Constraints**: *Maximum Items*: `25` |

## Example (as JSON)

```json
{
  "carrierName": "the name of the mobile service provider",
  "accountName": "0000123456-00001",
  "servicePlan": "The service plan name",
  "mdnZipCode": "five digit zip code",
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
  ]
}
```

