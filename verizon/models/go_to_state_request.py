# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.custom_fields import CustomFields
from verizon.models.device_filter import DeviceFilter
from verizon.models.place_of_use import PlaceOfUse


class GoToStateRequest(object):

    """Implementation of the 'GoToStateRequest' model.

    Changes the provisioning state of one or more devices to a specified
    customer-defined service and state.

    Attributes:
        service_name (str): The name of a customer-defined service to push the
            devices to.
        state_name (str): The name of a customer-defined stage state to push
            the devices to.
        service_plan (str): The service plan code that you want to assign to
            all specified devices in the new state.
        mdn_zip_code (str): The Zip code of the location where the line of
            service will primarily be used, or a Zip code that you have been
            told to use with these devices. For accounts that are configured
            for geographic numbering, this is the ZIP code from which the MDN
            will be derived.
        devices (List[AccountDeviceList]): Up to 10,000 devices that you want
            to push to a different state, specified by device identifier.
        filter (DeviceFilter): Specify the kind of the device identifier, the
            type of match, and the string that you want to match.
        carrier_ip_pool_name (str): The pool from which your device IP
            addresses will be derived if the service or state change requires
            new IP addresses.If you do not include this element, the default
            pool will be used.
        public_ip_restriction (str): For devices with static IP addresses on
            the public network, this specifies whether the devices have
            general access to the Internet. Valid values are “restricted” or
            “unrestricted”.
        sku_number (str): The Stock Keeping Unit (SKU) number of a 4G device
            type with an embedded SIM. Can be used with ICCID or EID device
            identifiers in lieu of an IMEI when activating 4G devices. The
            SkuNumber will be used with all devices in the request, so all
            devices must be of the same type.
        custom_fields (List[CustomFields]): The names and values of any custom
            fields that you want to set for the devices.
        devices_with_service_address (List[object]): This is an array that
            associates an IP address with a device identifier. This variable
            is only relevant for Business Internet/Fixed Wireless Access
        ipaddress (str): The IP address of the device.
        group_name (str): The name of a device group that the devices should
            be added to.
        primary_place_of_use (PlaceOfUse): The customer name and the address
            of the device's primary place of use. Leave these fields empty to
            use the account profile address as the primary place of use. These
            values will be applied to all devices in the request.If the
            account is enabled for non-geographic MDNs and the device supports
            it, the primaryPlaceOfUse address will also be used to derive the
            MDN for the device.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "service_name": 'serviceName',
        "state_name": 'stateName',
        "service_plan": 'servicePlan',
        "mdn_zip_code": 'mdnZipCode',
        "devices": 'devices',
        "filter": 'filter',
        "carrier_ip_pool_name": 'carrierIpPoolName',
        "public_ip_restriction": 'publicIpRestriction',
        "sku_number": 'skuNumber',
        "custom_fields": 'customFields',
        "devices_with_service_address": 'devicesWithServiceAddress',
        "ipaddress": 'ipAddress',
        "group_name": 'groupName',
        "primary_place_of_use": 'primaryPlaceOfUse'
    }

    _optionals = [
        'devices',
        'filter',
        'carrier_ip_pool_name',
        'public_ip_restriction',
        'sku_number',
        'custom_fields',
        'devices_with_service_address',
        'ipaddress',
        'group_name',
        'primary_place_of_use',
    ]

    def __init__(self,
                 service_name=None,
                 state_name=None,
                 service_plan=None,
                 mdn_zip_code=None,
                 devices=APIHelper.SKIP,
                 filter=APIHelper.SKIP,
                 carrier_ip_pool_name=APIHelper.SKIP,
                 public_ip_restriction=APIHelper.SKIP,
                 sku_number=APIHelper.SKIP,
                 custom_fields=APIHelper.SKIP,
                 devices_with_service_address=APIHelper.SKIP,
                 ipaddress=APIHelper.SKIP,
                 group_name=APIHelper.SKIP,
                 primary_place_of_use=APIHelper.SKIP):
        """Constructor for the GoToStateRequest class"""

        # Initialize members of the class
        self.service_name = service_name 
        self.state_name = state_name 
        self.service_plan = service_plan 
        self.mdn_zip_code = mdn_zip_code 
        if devices is not APIHelper.SKIP:
            self.devices = devices 
        if filter is not APIHelper.SKIP:
            self.filter = filter 
        if carrier_ip_pool_name is not APIHelper.SKIP:
            self.carrier_ip_pool_name = carrier_ip_pool_name 
        if public_ip_restriction is not APIHelper.SKIP:
            self.public_ip_restriction = public_ip_restriction 
        if sku_number is not APIHelper.SKIP:
            self.sku_number = sku_number 
        if custom_fields is not APIHelper.SKIP:
            self.custom_fields = custom_fields 
        if devices_with_service_address is not APIHelper.SKIP:
            self.devices_with_service_address = devices_with_service_address 
        if ipaddress is not APIHelper.SKIP:
            self.ipaddress = ipaddress 
        if group_name is not APIHelper.SKIP:
            self.group_name = group_name 
        if primary_place_of_use is not APIHelper.SKIP:
            self.primary_place_of_use = primary_place_of_use 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        service_name = dictionary.get("serviceName") if dictionary.get("serviceName") else None
        state_name = dictionary.get("stateName") if dictionary.get("stateName") else None
        service_plan = dictionary.get("servicePlan") if dictionary.get("servicePlan") else None
        mdn_zip_code = dictionary.get("mdnZipCode") if dictionary.get("mdnZipCode") else None
        devices = None
        if dictionary.get('devices') is not None:
            devices = [AccountDeviceList.from_dictionary(x) for x in dictionary.get('devices')]
        else:
            devices = APIHelper.SKIP
        filter = DeviceFilter.from_dictionary(dictionary.get('filter')) if 'filter' in dictionary.keys() else APIHelper.SKIP
        carrier_ip_pool_name = dictionary.get("carrierIpPoolName") if dictionary.get("carrierIpPoolName") else APIHelper.SKIP
        public_ip_restriction = dictionary.get("publicIpRestriction") if dictionary.get("publicIpRestriction") else APIHelper.SKIP
        sku_number = dictionary.get("skuNumber") if dictionary.get("skuNumber") else APIHelper.SKIP
        custom_fields = None
        if dictionary.get('customFields') is not None:
            custom_fields = [CustomFields.from_dictionary(x) for x in dictionary.get('customFields')]
        else:
            custom_fields = APIHelper.SKIP
        devices_with_service_address = dictionary.get("devicesWithServiceAddress") if dictionary.get("devicesWithServiceAddress") else APIHelper.SKIP
        ipaddress = dictionary.get("ipAddress") if dictionary.get("ipAddress") else APIHelper.SKIP
        group_name = dictionary.get("groupName") if dictionary.get("groupName") else APIHelper.SKIP
        primary_place_of_use = PlaceOfUse.from_dictionary(dictionary.get('primaryPlaceOfUse')) if 'primaryPlaceOfUse' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(service_name,
                   state_name,
                   service_plan,
                   mdn_zip_code,
                   devices,
                   filter,
                   carrier_ip_pool_name,
                   public_ip_restriction,
                   sku_number,
                   custom_fields,
                   devices_with_service_address,
                   ipaddress,
                   group_name,
                   primary_place_of_use)
