
# ESIM Provhistory Request

## Structure

`ESIMProvhistoryRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | - |
| `device_filter` | [`List[DeviceId2]`](../../doc/models/device-id-2.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `earliest` | `datetime` | Optional | - |
| `latest` | `datetime` | Optional | - |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "earliest": "10/15/2021 04:49:35",
  "latest": "10/15/2021 04:49:49",
  "deviceFilter": [
    {
      "id": "id4",
      "kind": "kind2"
    },
    {
      "id": "id4",
      "kind": "kind2"
    },
    {
      "id": "id4",
      "kind": "kind2"
    }
  ]
}
```

