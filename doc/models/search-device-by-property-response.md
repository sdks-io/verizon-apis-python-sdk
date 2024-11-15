
# Search Device by Property Response

The device identifier and fields to match in the search.

## Structure

`SearchDeviceByPropertyResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billingaccountid` | `str` | Optional | Billing account ID of the resource. |
| `createdon` | `str` | Optional | The date the resource was created. |
| `eventretention` | `str` | Optional | - |
| `fields` | [`Fields1`](../../doc/models/fields-1.md) | Optional | - |
| `iccid` | `str` | Optional | Cellular SIM card identifier. |
| `id` | `str` | Optional | ThingSpace unique ID for the device that was added. |
| `imei` | `str` | Optional | 4G hardware device identifier. |
| `kind` | `str` | Optional | Identifies the resource kind. |
| `lastupdated` | `str` | Optional | The date the resource was last updated. |
| `providerid` | `str` | Optional | The device’s service provider. |
| `refid` | `str` | Optional | The value of the refidtype identifier. |
| `refidtype` | `str` | Optional | The device identifier type used to refer to this device. |
| `state` | `str` | Optional | Service state of the device. |
| `version` | `str` | Optional | Version of the underlying schema resource. |
| `versionid` | `str` | Optional | The version of the resource. |

## Example (as JSON)

```json
{
  "billingaccountid": "1223334444-00001",
  "createdon": "12/19/2018 06:45:41",
  "eventretention": "90",
  "iccid": "20332350053095597842",
  "id": "64612cb3-3685-6dad-fd2b-ea1adeb5a269",
  "imei": "320778042285497",
  "kind": "ts.device",
  "lastupdated": "12/19/2018 06:45:41",
  "providerid": "8a314f07-849e-6568-e3c1-8381c1f61bfc",
  "refid": "20332350053095597842",
  "refidtype": "iccid",
  "state": "registered",
  "version": "1.0",
  "versionid": "b3cdaddb-0359-11e9-aba2-02420a4e1b0a",
  "fields": {
    "item": {
      "acceleration": {
        "x": "x6",
        "y": "y4",
        "z": "z6"
      },
      "battery": "battery0",
      "humidity": "humidity4",
      "light": "light6",
      "pressure": "pressure2"
    }
  }
}
```

