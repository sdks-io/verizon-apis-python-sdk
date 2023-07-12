# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class SelectedService(object):

    """Implementation of the 'SelectedService' model.

    Service which is selected.

    Attributes:
        name (string): Name of the service needs to be deployed.
        version (string): Name of the service user is created.
        state (ServiceStateEnum): Can have any value as - DRAFT, DESIGN,
            TESTING, PUBLISH, CERTIFY, READY_TO_USE, DEPRECATE, DELETED.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "version": 'version',
        "state": 'state'
    }

    _optionals = [
        'name',
        'version',
        'state',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 version=APIHelper.SKIP,
                 state=APIHelper.SKIP):
        """Constructor for the SelectedService class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if version is not APIHelper.SKIP:
            self.version = version 
        if state is not APIHelper.SKIP:
            self.state = state 

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
        version = dictionary.get("version") if dictionary.get("version") else APIHelper.SKIP
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   version,
                   state)