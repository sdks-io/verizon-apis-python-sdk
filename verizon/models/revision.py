# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.edge_service_launch_params import EdgeServiceLaunchParams


class Revision(object):

    """Implementation of the 'Revision' model.

    TODO: type model description here.

    Attributes:
        version (string): TODO: type description here.
        additional_params (list of EdgeServiceLaunchParams): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "version": 'version',
        "additional_params": 'additionalParams'
    }

    _optionals = [
        'additional_params',
    ]

    _nullables = [
        'additional_params',
    ]

    def __init__(self,
                 version=None,
                 additional_params=APIHelper.SKIP):
        """Constructor for the Revision class"""

        # Initialize members of the class
        self.version = version 
        if additional_params is not APIHelper.SKIP:
            self.additional_params = additional_params 

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

        version = dictionary.get("version") if dictionary.get("version") else None
        if 'additionalParams' in dictionary.keys():
            additional_params = [EdgeServiceLaunchParams.from_dictionary(x) for x in dictionary.get('additionalParams')] if dictionary.get('additionalParams') else None
        else:
            additional_params = APIHelper.SKIP
        # Return an object of this model
        return cls(version,
                   additional_params)
