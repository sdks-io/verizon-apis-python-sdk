# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class DeviceFirmwareVersionUpdateResult(object):

    """Implementation of the 'DeviceFirmwareVersionUpdateResult' model.

    Device firmware version update response.

    Attributes:
        account_name (string): Account identifier.
        request_id (string): Request identifier.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "request_id": 'requestId'
    }

    def __init__(self,
                 account_name=None,
                 request_id=None):
        """Constructor for the DeviceFirmwareVersionUpdateResult class"""

        # Initialize members of the class
        self.account_name = account_name 
        self.request_id = request_id 

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
        request_id = dictionary.get("requestId") if dictionary.get("requestId") else None
        # Return an object of this model
        return cls(account_name,
                   request_id)