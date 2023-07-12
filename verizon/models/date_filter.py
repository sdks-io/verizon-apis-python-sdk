# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class DateFilter(object):

    """Implementation of the 'DateFilter' model.

    Filter out the dates.

    Attributes:
        earliest (string): Only include devices that were added after this
            date and time.
        latest (string): Only include devices that were added before this date
            and time.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "earliest": 'earliest',
        "latest": 'latest'
    }

    _optionals = [
        'earliest',
        'latest',
    ]

    def __init__(self,
                 earliest=APIHelper.SKIP,
                 latest=APIHelper.SKIP):
        """Constructor for the DateFilter class"""

        # Initialize members of the class
        if earliest is not APIHelper.SKIP:
            self.earliest = earliest 
        if latest is not APIHelper.SKIP:
            self.latest = latest 

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

        earliest = dictionary.get("earliest") if dictionary.get("earliest") else APIHelper.SKIP
        latest = dictionary.get("latest") if dictionary.get("latest") else APIHelper.SKIP
        # Return an object of this model
        return cls(earliest,
                   latest)
