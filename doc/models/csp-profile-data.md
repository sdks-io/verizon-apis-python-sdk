
# CSP Profile Data

Response to CSP profile list.

## Structure

`CSPProfileData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | Total number of records available.<br>**Constraints**: `<= 1024` |
| `csp_profile_list` | [`List of CSPProfile`](../../doc/models/csp-profile.md) | Optional | List of all available CSP profile available within the user's organization.<br>**Constraints**: *Maximum Items*: `2048` |

## Example (as JSON)

```json
{
  "count": 1,
  "cspProfileList": [
    {
      "awsCspProfile": {
        "accessKey": "XXXXX",
        "credType": "ACCESS_KEY",
        "secretKey": "XXXXX"
      },
      "createdBy": "acme-user",
      "createdDate": "2022-08-03T13:59:51.000Z",
      "cspProfileName": "dev-api-csp-profile-mdp",
      "customerID": "acme",
      "id": "72e35c51-098e-4388-9055-2967bbd9be48",
      "lastModifiedBy": "acme-user",
      "lastModifiedDate": "2022-08-03T13:59:51.000Z",
      "projectName": "vz-cve",
      "type": "AWS",
      "usage": 183
    }
  ]
}
```

