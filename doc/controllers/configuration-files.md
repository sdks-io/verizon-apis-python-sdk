# Configuration Files

```python
configuration_files_controller = client.configuration_files
```

## Class Name

`ConfigurationFilesController`

## Methods

* [Get List of Files](../../doc/controllers/configuration-files.md#get-list-of-files)
* [Upload Config File](../../doc/controllers/configuration-files.md#upload-config-file)


# Get List of Files

You can retrieve a list of configuration or supplementary of files for an account.

```python
def get_list_of_files(self,
                     acc,
                     distribution_type)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `str` | Template, Required | Account identifier. |
| `distribution_type` | `str` | Query, Required | Filter the distributionType to only retrieve files for a specific distribution type. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`RetrievesAvailableFilesResponseList`](../../doc/models/retrieves-available-files-response-list.md).

## Example Usage

```python
acc = '0402196254-00001'

distribution_type = 'HTTP'

result = configuration_files_controller.get_list_of_files(
    acc,
    distribution_type
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# Upload Config File

Uploads a configuration/supplementary file for an account. ThingSpace generates a fileName after the upload and is returned in the response.

```python
def upload_config_file(self,
                      acc,
                      fileupload=None,
                      file_version=None,
                      make=None,
                      model=None,
                      local_target_path=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `str` | Template, Required | Account identifier. |
| `fileupload` | `typing.BinaryIO` | Form, Optional | The file to upload. |
| `file_version` | `str` | Form, Optional | Version of the file. |
| `make` | `str` | Form, Optional | The software-applicable device make. |
| `model` | `str` | Form, Optional | The software-applicable device model. |
| `local_target_path` | `str` | Form, Optional | Local target path on the device. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`UploadConfigurationFilesResponse`](../../doc/models/upload-configuration-files-response.md).

## Example Usage

```python
acc = '0402196254-00001'

file_version = '1.0'

make = 'Verizon'

model = 'VZW1'

local_target_path = '/VZWFOTA/hello-world.txt'

result = configuration_files_controller.upload_config_file(
    acc,
    file_version=file_version,
    make=make,
    model=model,
    local_target_path=local_target_path
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error. | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |

