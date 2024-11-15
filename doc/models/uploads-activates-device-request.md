
# Uploads Activates Device Request

The request body identifies the devices to upload.

## Structure

`UploadsActivatesDeviceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | The name of a billing account. An account name is usually numeric, and must include any leading zeros. |
| `email_address` | `str` | Required | The email address that the report should be sent to when the upload is complete. |
| `device_sku` | `str` | Required | The stock keeping unit that identifies the type of devices in the upload and activation. |
| `upload_type` | `str` | Required | The format of the device identifiers in the upload and activation. |
| `service_plan` | `str` | Required | The service plan code that you want to assign to all specified devices. |
| `carrier_ip_pool_name` | `str` | Optional | The pool from which your device IP addresses is derived. |
| `mdn_zip_code` | `str` | Required | The Zip code of the location where the line of service is primarily used, or a Zip code that you have been told to use with these devices. |
| `devices` | [`List[DeviceList]`](../../doc/models/device-list.md) | Required | The devices to upload, specified by device IDs in a format matching uploadType. |

## Example (as JSON)

```json
{
  "accountName": "1223334444-00001",
  "emailAddress": "bob@mycompany.com",
  "deviceSku": "VZW123456",
  "uploadType": "IMEI ICCID Pair",
  "servicePlan": "15MBShr",
  "carrierIpPoolName": "The carrier pool name",
  "mdnZipCode": "92222",
  "devices": [
    {
      "deviceIds": [
        {
          "id": "id0",
          "kind": "kind8"
        }
      ]
    }
  ]
}
```

