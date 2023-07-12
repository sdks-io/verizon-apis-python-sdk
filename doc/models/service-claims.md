
# Service Claims

Response to get all claims.

## Structure

`ServiceClaims`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | Count for all the claims returned after hitting the API.<br>**Constraints**: `<= 20480` |
| `claims_res_list` | [`List of Claim`](../../doc/models/claim.md) | Optional | List of all claims.<br>**Constraints**: *Maximum Items*: `2048` |

## Example (as JSON)

```json
{
  "claimsResList": [
    {
      "claimStatus": "UNVERIFIED",
      "claimType": "PUBLIC_MEC",
      "createdBy": "acme-dev-api-user1",
      "createdDate": "2022-08-03T15:21:30.000Z",
      "endTimeStamp": "0001-01-01T00:00:00.000Z",
      "environment": "AWS_WL",
      "id": "09368e8f-97b6-462f-b309-57d23fd25073",
      "lastModifiedDate": "0001-01-01T00:00:00.000Z",
      "sandBoxState": "NOT_STARTED",
      "sandBoxStatus": "NA",
      "serviceId": "b32321d2-4ee3-458b-a70b-e956525d46c9",
      "startTimeStamp": "0001-01-01T00:00:00.000Z",
      "name": "name0"
    }
  ],
  "count": 1
}
```

