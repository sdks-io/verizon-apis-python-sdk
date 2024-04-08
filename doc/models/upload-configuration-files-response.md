
# Upload Configuration Files Response

## Structure

`UploadConfigurationFilesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file_name` | `str` | Optional | The name of the file you are upgrading to. |
| `file_version` | `str` | Optional | The version of the file you are upgrading to. |
| `launch_date` | `date` | Optional | Software launch date. |
| `release_note` | `str` | Optional | Software release note. |
| `model` | `str` | Optional | Software applicable device model. |
| `make` | `str` | Optional | Software applicable device make. |
| `distribution_type` | `str` | Optional | LWM2M, OMD-DM or HTTP. |
| `device_platform_id` | `str` | Optional | The platform (Android, iOS, etc.) that the software can be applied to. |
| `local_target_path` | `str` | Optional | Local target path on the device. |

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

