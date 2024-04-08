# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class ConsentDeleteRequest(object):

    """Implementation of the 'ConsentDeleteRequest' model.

    TODO: type model description here.

    Attributes:
        account_name (str): Account identifier.
        device_list (List[str]): Device ID list.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "device_list": 'deviceList'
    }

    _optionals = [
        'account_name',
        'device_list',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 device_list=APIHelper.SKIP):
        """Constructor for the ConsentDeleteRequest class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if device_list is not APIHelper.SKIP:
            self.device_list = device_list 

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
        device_list = dictionary.get("deviceList") if dictionary.get("deviceList") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   device_list)
