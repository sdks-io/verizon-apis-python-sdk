
# Claim Status Request

Current status of the claim can have only two values eg: VERIFIED/UNVERIFIED.

## Structure

`ClaimStatusRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `claim_status` | [`ClaimStatusEnum`](../../doc/models/claim-status-enum.md) | Optional | Current status of the claim can have only two values eg: VERIFIED/UNVERIFIED. |

## Example (as JSON)

```json
{
  "claimStatus": "VERIFIED"
}
```

