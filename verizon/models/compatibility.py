# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class Compatibility(object):

    """Implementation of the 'Compatibility' model.

    Compatibility would have the attribute CSP which is Cloud service provider
    e.g. AWS_PUBLIC_CLOUD, AWS_WL, AWS_OUTPOST, AZURE_EDGE,
    AZURE_PUBLIC_CLOUD.

    Attributes:
        csp (CSPCompatibilityEnum): Cloud service provider e.g.
            AWS_PUBLIC_CLOUD, AWS_WL, AWS_OUTPOST, AZURE_EDGE,
            AZURE_PUBLIC_CLOUD.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "csp": 'csp'
    }

    _optionals = [
        'csp',
    ]

    def __init__(self,
                 csp='AWS_WL'):
        """Constructor for the Compatibility class"""

        # Initialize members of the class
        self.csp = csp 

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

        csp = dictionary.get("csp") if dictionary.get("csp") else 'AWS_WL'
        # Return an object of this model
        return cls(csp)
