# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class ServiceLaunchClusterAdditionalParams(object):

    """Implementation of the 'ServiceLaunchClusterAdditionalParams' model.

    TODO: type model description here.

    Attributes:
        additional_properties (object): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "additional_properties": 'additionalProperties'
    }

    _optionals = [
        'additional_properties',
    ]

    def __init__(self,
                 additional_properties=APIHelper.SKIP):
        """Constructor for the ServiceLaunchClusterAdditionalParams class"""

        # Initialize members of the class
        if additional_properties is not APIHelper.SKIP:
            self.additional_properties = additional_properties 

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

        additional_properties = dictionary.get("additionalProperties") if dictionary.get("additionalProperties") else APIHelper.SKIP
        # Return an object of this model
        return cls(additional_properties)
