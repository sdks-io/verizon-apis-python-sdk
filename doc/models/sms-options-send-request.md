
# SMS Options Send Request

## Structure

`SMSOptionsSendRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_plan` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9 ]{3,32}$` |
| `sms_message` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9 ]{3,64}$` |

## Example (as JSON)

```json
{
  "servicePlan": "the name of a service plan",
  "smsMessage": "A text message"
}
```

