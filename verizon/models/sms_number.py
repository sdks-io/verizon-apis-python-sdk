# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class SMSNumber(object):

    """Implementation of the 'SMSNumber' model.

    Notification SMS details.

    Attributes:
        carrier (str): TODO: type description here.
        number (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "carrier": 'carrier',
        "number": 'number'
    }

    _optionals = [
        'carrier',
        'number',
    ]

    def __init__(self,
                 carrier=APIHelper.SKIP,
                 number=APIHelper.SKIP):
        """Constructor for the SMSNumber class"""

        # Initialize members of the class
        if carrier is not APIHelper.SKIP:
            self.carrier = carrier 
        if number is not APIHelper.SKIP:
            self.number = number 

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
        carrier = dictionary.get("carrier") if dictionary.get("carrier") else APIHelper.SKIP
        number = dictionary.get("number") if dictionary.get("number") else APIHelper.SKIP
        # Return an object of this model
        return cls(carrier,
                   number)
