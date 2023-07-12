# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.diagnostics_category import DiagnosticsCategory


class DeviceExtendedDiagnosticsResult(object):

    """Implementation of the 'DeviceExtendedDiagnosticsResult' model.

    Result for a request to obtain device extended diagnostics.

    Attributes:
        categories (list of DiagnosticsCategory): The response includes
            various types of information about the device, grouped into
            categories. Each category object contains the category name and a
            list of Extended Attribute objects as key-value pairs.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "categories": 'categories'
    }

    _optionals = [
        'categories',
    ]

    def __init__(self,
                 categories=APIHelper.SKIP):
        """Constructor for the DeviceExtendedDiagnosticsResult class"""

        # Initialize members of the class
        if categories is not APIHelper.SKIP:
            self.categories = categories 

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

        categories = None
        if dictionary.get('categories') is not None:
            categories = [DiagnosticsCategory.from_dictionary(x) for x in dictionary.get('categories')]
        else:
            categories = APIHelper.SKIP
        # Return an object of this model
        return cls(categories)
