# Accounts

Get information about an account or account leads.

```python
accounts_controller = client.accounts
```

## Class Name

`AccountsController`

## Methods

* [Get Account Information](../../doc/controllers/accounts.md#get-account-information)
* [List Account States and Services](../../doc/controllers/accounts.md#list-account-states-and-services)
* [List Account Leads](../../doc/controllers/accounts.md#list-account-leads)


# Get Account Information

Returns information about a specified account.

```python
def get_account_information(self,
                           aname)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `str` | Template, Required | Account name. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Account`](../../doc/models/account.md).

## Example Usage

```python
aname = 'Chintan_CPNStaticBulk'

result = accounts_controller.get_account_information(aname)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "Chintan_CPNStaticBulk",
  "accountNumber": "1234567890-77777",
  "organizationName": "ChintanCPNBulk",
  "isProvisioningAllowed": true,
  "carriers": [
    "Verizon Wireless"
  ],
  "features": [
    "Static IP",
    "Dynamic IP",
    "Customer PN"
  ],
  "iPPools": [
    {
      "poolName": "ACMESTATIC001",
      "poolType": "Static IP",
      "isDefaultPool": true
    },
    {
      "poolName": "ACMEDYNAMIC001",
      "poolType": "Dynamic IP",
      "isDefaultPool": false
    }
  ],
  "servicePlans": [
    {
      "name": "",
      "code": "92876",
      "sizeKb": 1,
      "carrierServicePlanCode": "",
      "extendedAttributes": []
    },
    {
      "name": "",
      "code": "92876",
      "sizeKb": 1,
      "carrierServicePlanCode": "",
      "extendedAttributes": []
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# List Account States and Services

Returns a list and details of all custom services and states defined for a specified account.

```python
def list_account_states_and_services(self,
                                    aname)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `str` | Template, Required | Account name. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`AccountStatesAndServices`](../../doc/models/account-states-and-services.md).

## Example Usage

```python
aname = '0252012345-00001'

result = accounts_controller.list_account_states_and_services(aname)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "engagement": [
    {
      "engagementId": "1234",
      "chargingGroup": "Engagement1234",
      "services": [
        {
          "name": "Svc1",
          "description": "Usage Segmentation - Main Line.",
          "states": [
            {
              "name": "Svc1 Activate",
              "workflowSequenceNumber": 1,
              "servicePlans": [
                "4523aef7250f67205fd5",
                "4d4090c0f2d48814c94d"
              ]
            },
            {
              "name": "Svc1 No Telematics",
              "workflowSequenceNumber": 3,
              "servicePlans": [
                "4523aef7250f67205fd5",
                "4d4090c0f2d48814c94d"
              ]
            },
            {
              "name": "Svc1 Deactivate",
              "workflowSequenceNumber": 2,
              "servicePlans": [
                "4523aef7250f67205fd5",
                "4d4090c0f2d48814c94d"
              ]
            }
          ]
        },
        {
          "name": "WIFI",
          "description": "Usage Segmentation - WiFi.",
          "states": [
            {
              "name": "WIFI Redirect",
              "workflowSequenceNumber": 2,
              "servicePlans": [
                "4d4090c0f2d48814c94d"
              ]
            },
            {
              "name": "WIFI Trial",
              "workflowSequenceNumber": 4,
              "servicePlans": [
                "4d4090c0f2d48814c94d"
              ]
            },
            {
              "name": "WIFI Goodwill",
              "workflowSequenceNumber": 6,
              "servicePlans": [
                "4d4090c0f2d48814c94d"
              ]
            },
            {
              "name": "WIFI Disable",
              "workflowSequenceNumber": 3,
              "servicePlans": [
                "4d4090c0f2d48814c94d"
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# List Account Leads

When HTTP status is 202, a URL will be returned in the Location header of the form /leads/{aname}?next={token}. This URL can be used to request the next set of leads.

```python
def list_account_leads(self,
                      aname,
                      next=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `str` | Template, Required | Account name. |
| `next` | `long\|int` | Query, Optional | Continue the previous query from the pageUrl in Location Header. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`AccountLeadsResult`](../../doc/models/account-leads-result.md).

## Example Usage

```python
aname = '0252012345-00001'

result = accounts_controller.list_account_leads(aname)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "leads": [
    {
      "leadId": "L-10001",
      "leadState": "Qualified",
      "address": {
        "addressLine1": "1600 Pennsylvania Avenue",
        "addressLine2": "",
        "city": "Washington",
        "state": "DC",
        "zip": "20500",
        "country": "USA"
      }
    }
  ],
  "hasMoreData": false
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |

