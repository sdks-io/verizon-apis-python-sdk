# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.models.activate import Activate
from verizon.models.pwn_device_list import PWNDeviceList


class ChangePWNDeviceStateActivateRequest(object):

    """Implementation of the 'ChangePWNDeviceState-ActivateRequest' model.

    TODO: type model description here.

    Attributes:
        account_name (str): TODO: type description here.
        device_list (List[PWNDeviceList]): TODO: type description here.
        activate (Activate): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "device_list": 'deviceList',
        "activate": 'activate'
    }

    def __init__(self,
                 account_name=None,
                 device_list=None,
                 activate=None):
        """Constructor for the ChangePWNDeviceStateActivateRequest class"""

        # Initialize members of the class
        self.account_name = account_name 
        self.device_list = device_list 
        self.activate = activate 

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
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else None
        device_list = None
        if dictionary.get('deviceList') is not None:
            device_list = [PWNDeviceList.from_dictionary(x) for x in dictionary.get('deviceList')]
        activate = Activate.from_dictionary(dictionary.get('activate')) if dictionary.get('activate') else None
        # Return an object of this model
        return cls(account_name,
                   device_list,
                   activate)
