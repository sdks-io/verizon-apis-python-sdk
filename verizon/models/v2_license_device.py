# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class V2LicenseDevice(object):

    """Implementation of the 'V2LicenseDevice' model.

    Device IMEI list.

    Attributes:
        device_id (string): Device IMEI.
        assignment_time (string): License assignment time.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_id": 'deviceId',
        "assignment_time": 'assignmentTime'
    }

    _optionals = [
        'assignment_time',
    ]

    def __init__(self,
                 device_id=None,
                 assignment_time=APIHelper.SKIP):
        """Constructor for the V2LicenseDevice class"""

        # Initialize members of the class
        self.device_id = device_id 
        if assignment_time is not APIHelper.SKIP:
            self.assignment_time = assignment_time 

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

        device_id = dictionary.get("deviceId") if dictionary.get("deviceId") else None
        assignment_time = dictionary.get("assignmentTime") if dictionary.get("assignmentTime") else APIHelper.SKIP
        # Return an object of this model
        return cls(device_id,
                   assignment_time)
