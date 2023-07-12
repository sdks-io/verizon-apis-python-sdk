
# Software Package

Software package information.

## Structure

`SoftwarePackage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `software_name` | `string` | Required | Software name. |
| `launch_date` | `date` | Required | Software launch date. |
| `release_note` | `string` | Optional | Software release note reserved for future use. |
| `model` | `string` | Required | Software applicable device model. |
| `make` | `string` | Required | Software applicable device make. |
| `distribution_type` | `string` | Required | LWM2M, OMD-DM or HTTP. |
| `device_platform_id` | `string` | Required | The platform (Android, iOS, etc.) that the software can be applied to. |

## Example (as JSON)

```json
{
  "softwareName": "FOTA_Verizon_Model-A_02To03_HF",
  "launchDate": "2020-08-31",
  "releaseNote": "",
  "model": "Model-A",
  "make": "Verizon",
  "distributionType": "HTTP",
  "devicePlatformId": "IoT"
}
```

