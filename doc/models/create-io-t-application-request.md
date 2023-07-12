
# Create Io T Application Request

The request body must include the UUID of the subscription that you want to update plus any properties that you want to change.

## Structure

`CreateIoTApplicationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `app_name` | `string` | Optional | A user defined name for the application being deployed in Azure IoT Central. |
| `billing_account_id` | `string` | Optional | The ThingSpace ID of the authenticating billing account |
| `client_id` | `string` | Optional | The Azure ClientID of the associated Azure target account |
| `client_secret` | `string` | Optional | The Azure Client Secret of the associated Azure target account |
| `email_i_ds` | `string` | Optional | The “email IDs” to be added to/sent to with this API. |
| `resourcegroup` | `string` | Optional | The Azure Resource group of the associated Azure target account |
| `sample_io_tc_app` | `string` | Optional | This is the reference Azure IoT Central application developed by Verizon. |
| `subscription_id` | `string` | Optional | The Azure Subscription ID of the associated Azure target account |
| `tenant_id` | `string` | Optional | The Azure Tenant ID of the associated Azure target account |

## Example (as JSON)

```json
{
  "appName": "newarmapp1",
  "billingAccountID": "0000123456-00001",
  "clientID": "UUID",
  "clientSecret": "client secret",
  "emailIDs": "email@domain.com",
  "resourcegroup": "Myresourcegroup",
  "sampleIOTcApp": "app ID",
  "subscriptionID": "subscription ID",
  "tenantID": "tenant ID"
}
```

