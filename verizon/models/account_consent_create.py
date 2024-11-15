# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class AccountConsentCreate(object):

    """Implementation of the 'AccountConsentCreate' model.

    TODO: type model description here.

    Attributes:
        device_list (List[object]): An array of device identifiers
        account_name (str): The numeric name of the account, including leading
            zeros.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_list": 'deviceList',
        "account_name": 'accountName'
    }

    _optionals = [
        'device_list',
        'account_name',
    ]

    def __init__(self,
                 device_list=APIHelper.SKIP,
                 account_name=APIHelper.SKIP):
        """Constructor for the AccountConsentCreate class"""

        # Initialize members of the class
        if device_list is not APIHelper.SKIP:
            self.device_list = device_list 
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 

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
        device_list = dictionary.get("deviceList") if dictionary.get("deviceList") else APIHelper.SKIP
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        # Return an object of this model
        return cls(device_list,
                   account_name)
