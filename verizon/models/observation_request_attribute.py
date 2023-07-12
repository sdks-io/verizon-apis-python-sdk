# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class ObservationRequestAttribute(object):

    """Implementation of the 'ObservationRequestAttribute' model.

    Streaming RF parameter that you want to observe.

    Attributes:
        name (AttributeIdentifierEnum): Attribute identifier.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name'
    }

    _optionals = [
        'name',
    ]

    def __init__(self,
                 name=APIHelper.SKIP):
        """Constructor for the ObservationRequestAttribute class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 

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

        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        # Return an object of this model
        return cls(name)
