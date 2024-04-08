# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.custom_fields import CustomFields


class DeviceCostCenterRequest(object):

    """Implementation of the 'DeviceCostCenterRequest' model.

    Request to retrieve cost center value of a device.

    Attributes:
        account_name (str): The name of a billing account.
        cost_center (str): The new cost center code. Valid values are any
            string of up to 36 alphanumeric characters, space, dash,
            exclamation point, and pound sign.
        custom_fields (List[CustomFields]): Custom field names and values, if
            you want to only include devices that have matching values.
        devices (List[AccountDeviceList]): A list of the devices that you want
            to change, specified by device identifier. Do not include
            accountName, groupName, customFields, or servicePlan if you use
            this parameter.
        group_name (str): The name of a device group, if you want to only
            include devices in that group.
        primary_place_of_use (object): The customer name and the address of
            the device's primary place of use. These values are applied to all
            devices in the request.The Primary Place of Use location may
            affect taxation or have other legal implications. You may want to
            speak with legal and/or financial advisers before entering values
            for these fields.
        remove_cost_center (bool): Set to true to remove the cost center code
            value. This flag takes precedence over a new costCenter value. If
            this flag is true and costCenter has a value, the cost center code
            is removed. Do not include this parameter, or set it to false to
            change the costCenter value.
        service_plan (str): The name of a service plan, if you want to only
            include devices that have that service plan.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "cost_center": 'costCenter',
        "custom_fields": 'customFields',
        "devices": 'devices',
        "group_name": 'groupName',
        "primary_place_of_use": 'primaryPlaceOfUse',
        "remove_cost_center": 'removeCostCenter',
        "service_plan": 'servicePlan'
    }

    _optionals = [
        'account_name',
        'cost_center',
        'custom_fields',
        'devices',
        'group_name',
        'primary_place_of_use',
        'remove_cost_center',
        'service_plan',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 cost_center=APIHelper.SKIP,
                 custom_fields=APIHelper.SKIP,
                 devices=APIHelper.SKIP,
                 group_name=APIHelper.SKIP,
                 primary_place_of_use=APIHelper.SKIP,
                 remove_cost_center=APIHelper.SKIP,
                 service_plan=APIHelper.SKIP):
        """Constructor for the DeviceCostCenterRequest class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if cost_center is not APIHelper.SKIP:
            self.cost_center = cost_center 
        if custom_fields is not APIHelper.SKIP:
            self.custom_fields = custom_fields 
        if devices is not APIHelper.SKIP:
            self.devices = devices 
        if group_name is not APIHelper.SKIP:
            self.group_name = group_name 
        if primary_place_of_use is not APIHelper.SKIP:
            self.primary_place_of_use = primary_place_of_use 
        if remove_cost_center is not APIHelper.SKIP:
            self.remove_cost_center = remove_cost_center 
        if service_plan is not APIHelper.SKIP:
            self.service_plan = service_plan 

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
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        cost_center = dictionary.get("costCenter") if dictionary.get("costCenter") else APIHelper.SKIP
        custom_fields = None
        if dictionary.get('customFields') is not None:
            custom_fields = [CustomFields.from_dictionary(x) for x in dictionary.get('customFields')]
        else:
            custom_fields = APIHelper.SKIP
        devices = None
        if dictionary.get('devices') is not None:
            devices = [AccountDeviceList.from_dictionary(x) for x in dictionary.get('devices')]
        else:
            devices = APIHelper.SKIP
        group_name = dictionary.get("groupName") if dictionary.get("groupName") else APIHelper.SKIP
        primary_place_of_use = dictionary.get("primaryPlaceOfUse") if dictionary.get("primaryPlaceOfUse") else APIHelper.SKIP
        remove_cost_center = dictionary.get("removeCostCenter") if "removeCostCenter" in dictionary.keys() else APIHelper.SKIP
        service_plan = dictionary.get("servicePlan") if dictionary.get("servicePlan") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   cost_center,
                   custom_fields,
                   devices,
                   group_name,
                   primary_place_of_use,
                   remove_cost_center,
                   service_plan)
