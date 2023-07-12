
# Upload Configuration Files Response

## Structure

`UploadConfigurationFilesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file_name` | `string` | Optional | The name of the file you are upgrading to. |
| `file_version` | `string` | Optional | The version of the file you are upgrading to. |
| `launch_date` | `date` | Optional | Software launch date. |
| `release_note` | `string` | Optional | Software release note. |
| `model` | `string` | Optional | Software applicable device model. |
| `make` | `string` | Optional | Software applicable device make. |
| `distribution_type` | `string` | Optional | LWM2M, OMD-DM or HTTP. |
| `device_platform_id` | `string` | Optional | The platform (Android, iOS, etc.) that the software can be applied to. |
| `local_target_path` | `string` | Optional | Local target path on the device. |

## Example (as JSON)

```json
{
  "fileName": "hello-world.txt",
  "fileVersion": "1.0",
  "launchDate": "2020-08-31",
  "releaseNote": "note",
  "model": "Model-A",
  "make": "Verizon",
  "distributionType": "HTTP",
  "devicePlatformId": "IoT",
  "localTargetPath": "IoT"
}
```

