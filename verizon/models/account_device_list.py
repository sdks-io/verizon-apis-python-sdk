# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.device_id import DeviceId


class AccountDeviceList(object):

    """Implementation of the 'AccountDeviceList' model.

    A list of deviceId objects to use when requesting information from
    multiple devices.

    Attributes:
        device_ids (List[DeviceId]): All identifiers for the device.
        ipaddress (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_ids": 'deviceIds',
        "ipaddress": 'ipAddress'
    }

    _optionals = [
        'ipaddress',
    ]

    def __init__(self,
                 device_ids=None,
                 ipaddress=APIHelper.SKIP):
        """Constructor for the AccountDeviceList class"""

        # Initialize members of the class
        self.device_ids = device_ids 
        if ipaddress is not APIHelper.SKIP:
            self.ipaddress = ipaddress 

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
        device_ids = None
        if dictionary.get('deviceIds') is not None:
            device_ids = [DeviceId.from_dictionary(x) for x in dictionary.get('deviceIds')]
        ipaddress = dictionary.get("ipAddress") if dictionary.get("ipAddress") else APIHelper.SKIP
        # Return an object of this model
        return cls(device_ids,
                   ipaddress)
