# Diagnostics Observations

```python
diagnostics_observations_controller = client.diagnostics_observations
```

## Class Name

`DiagnosticsObservationsController`

## Methods

* [Start Diagnostics Observation](../../doc/controllers/diagnostics-observations.md#start-diagnostics-observation)
* [Stop Diagnostics Observation](../../doc/controllers/diagnostics-observations.md#stop-diagnostics-observation)


# Start Diagnostics Observation

This endpoint allows the user to start or change observe diagnostics.

```python
def start_diagnostics_observation(self,
                                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ObservationRequest`](../../doc/models/observation-request.md) | Body, Required | Request for device observation information. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DiagnosticsObservationResult`](../../doc/models/diagnostics-observation-result.md).

## Example Usage

```python
body = ObservationRequest(
    account_name='TestQAAccount',
    devices=[
        Device(
            id='864508030026238',
            kind='IMEI'
        )
    ],
    attributes=[
        ObservationRequestAttribute(
            name=AttributeIdentifierEnum.RADIO_SIGNAL_STRENGTH
        ),
        ObservationRequestAttribute(
            name=AttributeIdentifierEnum.LINK_QUALITY
        ),
        ObservationRequestAttribute(
            name=AttributeIdentifierEnum.NETWORK_BEARER
        ),
        ObservationRequestAttribute(
            name=AttributeIdentifierEnum.CELL_ID
        )
    ],
    frequency=NumericalData(
        value=15,
        unit=NumericalDataUnitEnum.SECOND
    ),
    duration=NumericalData(
        value=15,
        unit=NumericalDataUnitEnum.SECOND
    )
)

result = diagnostics_observations_controller.start_diagnostics_observation(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "createdOn": "2019-09-10T19:05:33.33Z",
  "transactionID": "9c7bb124-11f5-4ff3-8a88-0eec1ba99205",
  "status": "CANCEL_OBSERVE_PENDING"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response. | [`DeviceDiagnosticsResultException`](../../doc/models/device-diagnostics-result-exception.md) |


# Stop Diagnostics Observation

This endpoint allows the user to stop or reset observe diagnostics.

```python
def stop_diagnostics_observation(self,
                                transaction_id,
                                account_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Query, Required | The ID value associated with the transaction. |
| `account_name` | `str` | Query, Required | The numeric account name. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DiagnosticsObservationResult`](../../doc/models/diagnostics-observation-result.md).

## Example Usage

```python
transaction_id = '5f4bd2ff-5d7f-444d-af17-3f6a80bb2a94'

account_name = '0000123456-00001'

result = diagnostics_observations_controller.stop_diagnostics_observation(
    transaction_id,
    account_name
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "createdOn": "2019-09-10T19:05:33.33Z",
  "transactionID": "9c7bb124-11f5-4ff3-8a88-0eec1ba99205",
  "status": "CANCEL_OBSERVE_PENDING"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response. | [`DeviceDiagnosticsResultException`](../../doc/models/device-diagnostics-result-exception.md) |

