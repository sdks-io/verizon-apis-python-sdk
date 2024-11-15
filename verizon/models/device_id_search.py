# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class DeviceIdSearch(object):

    """Implementation of the 'DeviceIdSearch' model.

    Search by device id.

    Attributes:
        contains (str): The string appears anywhere in the identifer.
        startswith (str): The identifer must start with the specified string.
        endswith (str): The identifier must end with the specified string.
        kind (str): The type of the device identifier. Valid types of
            identifiers are:ESN (decimal),EID,ICCID (up to 20 digits),IMEI (up
            to 16 digits),MDN,MEID (hexadecimal),MSISDN.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "contains": 'contains',
        "kind": 'kind',
        "startswith": 'startswith',
        "endswith": 'endswith'
    }

    _optionals = [
        'startswith',
        'endswith',
    ]

    def __init__(self,
                 contains=None,
                 kind=None,
                 startswith=APIHelper.SKIP,
                 endswith=APIHelper.SKIP):
        """Constructor for the DeviceIdSearch class"""

        # Initialize members of the class
        self.contains = contains 
        if startswith is not APIHelper.SKIP:
            self.startswith = startswith 
        if endswith is not APIHelper.SKIP:
            self.endswith = endswith 
        self.kind = kind 

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
        contains = dictionary.get("contains") if dictionary.get("contains") else None
        kind = dictionary.get("kind") if dictionary.get("kind") else None
        startswith = dictionary.get("startswith") if dictionary.get("startswith") else APIHelper.SKIP
        endswith = dictionary.get("endswith") if dictionary.get("endswith") else APIHelper.SKIP
        # Return an object of this model
        return cls(contains,
                   kind,
                   startswith,
                   endswith)