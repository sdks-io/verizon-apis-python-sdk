# Device Groups

```python
device_groups_controller = client.device_groups
```

## Class Name

`DeviceGroupsController`

## Methods

* [Create Device Group](../../doc/controllers/device-groups.md#create-device-group)
* [List Device Groups](../../doc/controllers/device-groups.md#list-device-groups)
* [Get Device Group Information](../../doc/controllers/device-groups.md#get-device-group-information)
* [Update Device Group](../../doc/controllers/device-groups.md#update-device-group)
* [Delete Device Group](../../doc/controllers/device-groups.md#delete-device-group)


# Create Device Group

Create a new device group and optionally add devices to the group. Device groups can make it easier to manage similar devices and to get reports on their usage.

```python
def create_device_group(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateDeviceGroupRequest`](../../doc/models/create-device-group-request.md) | Body, Required | A request to create a new device group. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ConnectivityManagementSuccessResult`](../../doc/models/connectivity-management-success-result.md).

## Example Usage

```python
body = CreateDeviceGroupRequest(
    account_name='0000123456-00001',
    group_description='descriptive string',
    group_name='group name',
    devices_to_add=[
        DeviceId(
            id='15-digit IMEI',
            kind='imei'
        )
    ]
)

result = device_groups_controller.create_device_group(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "success": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# List Device Groups

Returns a list of all device groups in a specified account.

```python
def list_device_groups(self,
                      aname)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `str` | Template, Required | Account name. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[DeviceGroup]`](../../doc/models/device-group.md).

## Example Usage

```python
aname = '0252012345-00001'

result = device_groups_controller.list_device_groups(aname)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "name": "Unassigned Devices",
    "description": "All devices that are not in another device group.",
    "isDefaultGroup": true,
    "extendedAttributes": []
  },
  {
    "name": "West Coast Devices",
    "description": "",
    "isDefaultGroup": false,
    "extendedAttributes": []
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# Get Device Group Information

When HTTP status is 202, a URL will be returned in the Location header of the form /groups/{aname}/name/{gname}/?next={token}. This URL can be used to request the next set of groups.

```python
def get_device_group_information(self,
                                aname,
                                gname,
                                next=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `str` | Template, Required | Account name. |
| `gname` | `str` | Template, Required | Group name. |
| `next` | `long\|int` | Query, Optional | Continue the previous query from the pageUrl pagetoken. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`DeviceGroupDevicesData`](../../doc/models/device-group-devices-data.md).

## Example Usage

```python
aname = '0252012345-00001'

gname = 'gname2'

result = device_groups_controller.get_device_group_information(
    aname,
    gname
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "name": "Nebraska Trucks",
  "description": "All service trucks in Nebraska.",
  "hasMoreData": false,
  "devices": [
    {
      "deviceIds": [
        {
          "id": "12345",
          "kind": "meid"
        },
        {
          "id": "54321",
          "kind": "mdn"
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


# Update Device Group

Make changes to a device group, including changing the name and description, and adding or removing devices.

```python
def update_device_group(self,
                       aname,
                       gname,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `str` | Template, Required | Account name. |
| `gname` | `str` | Template, Required | Group name. |
| `body` | [`DeviceGroupUpdateRequest`](../../doc/models/device-group-update-request.md) | Body, Required | Request to update device group. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ConnectivityManagementSuccessResult`](../../doc/models/connectivity-management-success-result.md).

## Example Usage

```python
aname = '0252012345-00001'

gname = 'gname2'

body = DeviceGroupUpdateRequest(
    devices_to_add=[
        DeviceId(
            id='990003420535537',
            kind='imei'
        )
    ],
    new_group_description='All western region tank level monitors.',
    new_group_name='Western region tanks'
)

result = device_groups_controller.update_device_group(
    aname,
    gname,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "success": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# Delete Device Group

Deletes a device group from the account. Devices in the group are moved to the default device group and are not deleted from the account.

```python
def delete_device_group(self,
                       aname,
                       gname)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `str` | Template, Required | Account name. |
| `gname` | `str` | Template, Required | Group name. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ConnectivityManagementSuccessResult`](../../doc/models/connectivity-management-success-result.md).

## Example Usage

```python
aname = '0252012345-00001'

gname = 'gname2'

result = device_groups_controller.delete_device_group(
    aname,
    gname
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "success": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |

