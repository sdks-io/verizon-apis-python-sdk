# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class IntentChainItem(object):

    """Implementation of the 'IntentChainItem' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        input (object): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "input": 'input'
    }

    _optionals = [
        'name',
        'input',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 input=APIHelper.SKIP):
        """Constructor for the IntentChainItem class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if input is not APIHelper.SKIP:
            self.input = input 

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
        input = dictionary.get("input") if dictionary.get("input") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   input)
