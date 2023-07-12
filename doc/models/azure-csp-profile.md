
# Azure Csp Profile

Information related to manage resources in Azure infrastructure.

## Structure

`AzureCspProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tenant_id` | `string` | Optional | Azure tenant ID.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `subscription_id` | `string` | Optional | Azure subscription ID.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `client_id` | `string` | Optional | Azure client ID.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `client_secret` | `string` | Optional | Azure client secret.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_ ]+$` |

## Example (as JSON)

```json
{
  "tenantID": "uuid",
  "subscriptionID": "uuid",
  "clientId": "uuid",
  "clientSecret": "Client Secret Example"
}
```

