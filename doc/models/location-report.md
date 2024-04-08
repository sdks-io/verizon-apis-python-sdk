
# Location Report

Location information for up to 1,000 devices.

## Structure

`LocationReport`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dev_location_list` | [`List[Location]`](../../doc/models/location.md) | Optional | Device location information. |
| `has_more_data` | `bool` | Optional | True if there are more device locations to retrieve. |
| `start_index` | `str` | Optional | The zero-based number of the first record to return. Set startIndex=0 for the first request. If there are more than 1,000 devices to be returned (hasMoreData=true), set startIndex=1000 for the second request, 2000 for the third request, etc. |
| `total_count` | `int` | Optional | The total number of devices in the original request and in the report. |
| `txid` | `str` | Optional | The transaction ID of the report. |

## Example (as JSON)

```json
{
  "startIndex": "0",
  "txid": "2017-12-11Te8b47da2-3a45-46cf-9903-61815e1e97e9",
  "totalCount": 3,
  "hasMoreData": false,
  "devLocationList": [
    {
      "error": {
        "time": "time4",
        "utcoffset": "utcoffset4",
        "type": "type6",
        "info": "info4"
      },
      "msid": "7892345678",
      "pd": {
        "qos": false,
        "radius": "5571",
        "time": "20170520004421",
        "x": "33.45324",
        "y": "-84.59621",
        "utcoffset": "utcoffset2"
      }
    },
    {
      "error": {
        "time": "time4",
        "utcoffset": "utcoffset4",
        "type": "type6",
        "info": "info4"
      },
      "msid": "8583239709",
      "pd": {
        "qos": false,
        "radius": "3866",
        "time": "20170525214342",
        "x": "38.8408694",
        "y": "-105.0422583",
        "utcoffset": "utcoffset2"
      }
    },
    {
      "error": {
        "time": "20170525214342",
        "type": "POSITION METHOD FAILURE",
        "info": "Exception code=ABSENT SUBSCRIBER",
        "utcoffset": "utcoffset4"
      },
      "msid": "7897654321",
      "pd": {
        "time": "time2",
        "utcoffset": "utcoffset2",
        "x": "x8",
        "y": "y6",
        "radius": "radius0"
      }
    }
  ]
}
```

