# MEC

```python
mec_controller = client.mec
```

## Class Name

`MECController`

## Methods

* [KPI List](../../doc/controllers/mec.md#kpi-list)
* [Get Profile List](../../doc/controllers/mec.md#get-profile-list)
* [Change Pmec Device State-Activate](../../doc/controllers/mec.md#change-pmec-device-state-activate)
* [Change Pmec Device State-Bulk Deactivate](../../doc/controllers/mec.md#change-pmec-device-state-bulk-deactivate)
* [Change Pmec Device Profile](../../doc/controllers/mec.md#change-pmec-device-profile)
* [Change Pmec Device I Paddress Bulk](../../doc/controllers/mec.md#change-pmec-device-i-paddress-bulk)
* [Get MEC Performance Consent](../../doc/controllers/mec.md#get-mec-performance-consent)


# KPI List

```python
def kpi_list(self,
            aname)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `str` | Template, Required | Account name. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`KPIInfoList`](../../doc/models/kpi-info-list.md).

## Example Usage

```python
aname = '0342351414-00001'

result = mec_controller.kpi_list(aname)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "KpiInfoList": [
    {
      "name": "DOWNLINK_THROUGHPUT",
      "value": "23.2",
      "nodeName": "132924_ENB_VZ_EULESS_OLTE_RD-01",
      "nodeType": "BASEBAND",
      "description": "Downlink throughput (4G)",
      "unit": "Mbps",
      "category": "Network Performance Radio",
      "timeOfLastUpdate": "2022-12-07T08:39:59.228Z"
    }
  ]
}
```


# Get Profile List

```python
def get_profile_list(self,
                    aname)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `str` | Template, Required | Account name. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`MECProfileList`](../../doc/models/mec-profile-list.md).

## Example Usage

```python
aname = '0342351414-00001'

result = mec_controller.get_profile_list(aname)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "profiles": [
    {
      "profileId": "HSS-EsmProfile_Enterprise",
      "profileName": "HSS EsmProfile Enterprise"
    }
  ]
}
```


# Change Pmec Device State-Activate

```python
def change_pmec_device_state_activate(self,
                                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ChangePmecDeviceStateActivateRequest`](../../doc/models/change-pmec-device-state-activate-request.md) | Body, Required | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ChangeMecDeviceStateResponse`](../../doc/models/change-mec-device-state-response.md).

## Example Usage

```python
body = ChangePmecDeviceStateActivateRequest(
    account_name='0342351414-00001',
    device_list=[
        MECDeviceList(
            device_ids=[
                MECDeviceId(
                    id='99948099913024600001',
                    kind='iccid'
                )
            ]
        )
    ],
    activate=Activate(
        profile='HSS EsmProfile Enterprise 5G'
    )
)

result = mec_controller.change_pmec_device_state_activate(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "c7b45cf2-cab1-4e42-82f8-20350f4c4ea3"
}
```


# Change Pmec Device State-Bulk Deactivate

```python
def change_pmec_device_state_bulk_deactivate(self,
                                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ChangePmecDeviceStateBulkDeactivateRequest`](../../doc/models/change-pmec-device-state-bulk-deactivate-request.md) | Body, Required | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ChangeMecDeviceStateResponse`](../../doc/models/change-mec-device-state-response.md).

## Example Usage

```python
body = ChangePmecDeviceStateBulkDeactivateRequest(
    account_name='0342351414-00001',
    device_list=[
        MECDeviceList(
            device_ids=[
                MECDeviceId(
                    id='99948099913031600000',
                    kind='iccid'
                )
            ]
        ),
        MECDeviceList(
            device_ids=[
                MECDeviceId(
                    id='99948099913031700000',
                    kind='iccid'
                )
            ]
        )
    ]
)

result = mec_controller.change_pmec_device_state_bulk_deactivate(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "c7b45cf2-cab1-4e42-82f8-20350f4c4ea3"
}
```


# Change Pmec Device Profile

```python
def change_pmec_device_profile(self,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ChangePmecDeviceProfileRequest`](../../doc/models/change-pmec-device-profile-request.md) | Body, Required | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ChangeMecDeviceProfileResponse`](../../doc/models/change-mec-device-profile-response.md).

## Example Usage

```python
body = ChangePmecDeviceProfileRequest(
    account_name='0342351414-00001',
    device_list=[
        MECDeviceList(
            device_ids=[
                MECDeviceId(
                    id='99948099913024600000',
                    kind='iccid'
                )
            ]
        )
    ],
    new_profile='HSS EsmProfile Enterprise 5G internet'
)

result = mec_controller.change_pmec_device_profile(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "c7b45cf2-cab1-4e42-82f8-20350f4c4ea3"
}
```


# Change Pmec Device I Paddress Bulk

```python
def change_pmec_device_i_paddress_bulk(self,
                                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ChangePmecDeviceStateBulkDeactivateRequest`](../../doc/models/change-pmec-device-state-bulk-deactivate-request.md) | Body, Required | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ChangeMecDeviceIPAddressResponse`](../../doc/models/change-mec-device-ip-address-response.md).

## Example Usage

```python
body = ChangePmecDeviceStateBulkDeactivateRequest(
    account_name='0342351414-00001',
    device_list=[
        MECDeviceList(
            device_ids=[
                MECDeviceId(
                    id='99948099913031600000',
                    kind='iccid'
                )
            ]
        ),
        MECDeviceList(
            device_ids=[
                MECDeviceId(
                    id='99948099913031700000',
                    kind='iccid'
                )
            ]
        )
    ]
)

result = mec_controller.change_pmec_device_i_paddress_bulk(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "c7b45cf2-cab1-4e42-82f8-20350f4c4ea3"
}
```


# Get MEC Performance Consent

```python
def get_mec_performance_consent(self,
                               aname)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `str` | Template, Required | Account name. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`GetMECPerformanceConsentResponse`](../../doc/models/get-mec-performance-consent-response.md).

## Example Usage

```python
aname = '1533445500-00088'

result = mec_controller.get_mec_performance_consent(aname)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "consent": "false"
}
```

