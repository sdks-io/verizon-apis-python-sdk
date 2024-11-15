# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.m_5g_biprimary_placeofuse import M5gBiprimaryPlaceofuse


class M5gBiaddressAndcustomerinfo(object):

    """Implementation of the '5gbiaddressAndcustomerinfo' model.

    TODO: type model description here.

    Attributes:
        primary_placeofuse (M5gBiprimaryPlaceofuse): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "primary_placeofuse": 'primaryPlaceofuse'
    }

    _optionals = [
        'primary_placeofuse',
    ]

    def __init__(self,
                 primary_placeofuse=APIHelper.SKIP):
        """Constructor for the M5gBiaddressAndcustomerinfo class"""

        # Initialize members of the class
        if primary_placeofuse is not APIHelper.SKIP:
            self.primary_placeofuse = primary_placeofuse 

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
        primary_placeofuse = M5gBiprimaryPlaceofuse.from_dictionary(dictionary.get('primaryPlaceofuse')) if 'primaryPlaceofuse' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(primary_placeofuse)
