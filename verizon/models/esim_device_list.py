# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.device_id_2 import DeviceId2


class ESIMDeviceList(object):

    """Implementation of the 'eSIMDeviceList' model.

    TODO: type model description here.

    Attributes:
        device_ids (List[DeviceId2]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_ids": 'deviceIds'
    }

    _optionals = [
        'device_ids',
    ]

    def __init__(self,
                 device_ids=APIHelper.SKIP):
        """Constructor for the ESIMDeviceList class"""

        # Initialize members of the class
        if device_ids is not APIHelper.SKIP:
            self.device_ids = device_ids 

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
            device_ids = [DeviceId2.from_dictionary(x) for x in dictionary.get('deviceIds')]
        else:
            device_ids = APIHelper.SKIP
        # Return an object of this model
        return cls(device_ids)
