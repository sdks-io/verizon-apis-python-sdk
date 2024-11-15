# Exclusions

Excluding or including devices (by consent) for location service

```python
exclusions_controller = client.exclusions
```

## Class Name

`ExclusionsController`


# Devices Location Give Consent Async

Create a consent record to use location services as an asynchronous request.

```python
def devices_location_give_consent_async(self,
                                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AccountConsentCreate`](../../doc/models/account-consent-create.md) | Body, Optional | Account details to create a consent record. |

## Response Type

[`ConsentTransactionID`](../../doc/models/consent-transaction-id.md)

## Example Usage

```python
result = exclusions_controller.devices_location_give_consent_async()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error. | [`DeviceLocationResultException`](../../doc/models/device-location-result-exception.md) |

