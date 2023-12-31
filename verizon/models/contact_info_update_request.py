# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.account_device_list import AccountDeviceList


class ContactInfoUpdateRequest(object):

    """Implementation of the 'ContactInfoUpdateRequest' model.

    Request to update contact information.

    Attributes:
        account_name (string): The name of the billing account that the
            devices belong to. An account name is usually numeric, and must
            include any leading zeros.
        devices (list of AccountDeviceList): A list of the devices that you
            want to change, specified by device identifier. You only need to
            provide one identifier per device. Do not include accountName,
            groupName, customFields, or servicePlan if you use this
            parameter.
        primary_place_of_use (object): The customer name and the address of
            the device's primary place of use. These values are applied to all
            devices in the request.The Primary Place of Use location may
            affect taxation or have other legal implications. You may want to
            speak with legal and/or financial advisers before entering values
            for these fields.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "devices": 'devices',
        "primary_place_of_use": 'primaryPlaceOfUse'
    }

    _optionals = [
        'account_name',
        'devices',
        'primary_place_of_use',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 devices=APIHelper.SKIP,
                 primary_place_of_use=APIHelper.SKIP):
        """Constructor for the ContactInfoUpdateRequest class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if devices is not APIHelper.SKIP:
            self.devices = devices 
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

        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        devices = None
        if dictionary.get('devices') is not None:
            devices = [AccountDeviceList.from_dictionary(x) for x in dictionary.get('devices')]
        else:
            devices = APIHelper.SKIP
        primary_place_of_use = dictionary.get("primaryPlaceOfUse") if dictionary.get("primaryPlaceOfUse") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   devices,
                   primary_place_of_use)
