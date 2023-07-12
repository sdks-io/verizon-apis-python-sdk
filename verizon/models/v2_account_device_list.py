# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.v2_account_device import V2AccountDevice


class V2AccountDeviceList(object):

    """Implementation of the 'V2AccountDeviceList' model.

    List of device information for an account.

    Attributes:
        account_name (string): Account name.
        has_more_data (bool): Has more device flag?
        last_seen_device_id (string): Last seen device identifier.
        max_page_size (int): Maximum page size.
        device_list (list of V2AccountDevice): Account device list.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "has_more_data": 'hasMoreData',
        "max_page_size": 'maxPageSize',
        "device_list": 'deviceList',
        "last_seen_device_id": 'lastSeenDeviceId'
    }

    _optionals = [
        'last_seen_device_id',
    ]

    def __init__(self,
                 account_name=None,
                 has_more_data=None,
                 max_page_size=None,
                 device_list=None,
                 last_seen_device_id=APIHelper.SKIP):
        """Constructor for the V2AccountDeviceList class"""

        # Initialize members of the class
        self.account_name = account_name 
        self.has_more_data = has_more_data 
        if last_seen_device_id is not APIHelper.SKIP:
            self.last_seen_device_id = last_seen_device_id 
        self.max_page_size = max_page_size 
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

        account_name = dictionary.get("accountName") if dictionary.get("accountName") else None
        has_more_data = dictionary.get("hasMoreData") if "hasMoreData" in dictionary.keys() else None
        max_page_size = dictionary.get("maxPageSize") if dictionary.get("maxPageSize") else None
        device_list = None
        if dictionary.get('deviceList') is not None:
            device_list = [V2AccountDevice.from_dictionary(x) for x in dictionary.get('deviceList')]
        last_seen_device_id = dictionary.get("lastSeenDeviceId") if dictionary.get("lastSeenDeviceId") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   has_more_data,
                   max_page_size,
                   device_list,
                   last_seen_device_id)
