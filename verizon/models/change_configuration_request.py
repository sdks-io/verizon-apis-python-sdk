# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.account_identifier import AccountIdentifier
from verizon.models.configuration import Configuration
from verizon.models.resource_identifier import ResourceIdentifier


class ChangeConfigurationRequest(object):

    """Implementation of the 'ChangeConfigurationRequest' model.

    The request body identifies the device and the values to set.

    Attributes:
        accountidentifier (AccountIdentifier): The ID of the authenticating
            billing account, in the format
            `{"billingaccountid":"1234567890-12345"}`.
        resourceidentifier (ResourceIdentifier): The ID of the target to
            delete, in the format {"id":
            "dd1682d3-2d80-cefc-f3ee-25154800beff"}.
        configuration (Configuration): List of the field names and values to
            set.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "accountidentifier": 'accountidentifier',
        "resourceidentifier": 'resourceidentifier',
        "configuration": 'configuration'
    }

    _optionals = [
        'accountidentifier',
        'resourceidentifier',
        'configuration',
    ]

    def __init__(self,
                 accountidentifier=APIHelper.SKIP,
                 resourceidentifier=APIHelper.SKIP,
                 configuration=APIHelper.SKIP):
        """Constructor for the ChangeConfigurationRequest class"""

        # Initialize members of the class
        if accountidentifier is not APIHelper.SKIP:
            self.accountidentifier = accountidentifier 
        if resourceidentifier is not APIHelper.SKIP:
            self.resourceidentifier = resourceidentifier 
        if configuration is not APIHelper.SKIP:
            self.configuration = configuration 

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

        accountidentifier = AccountIdentifier.from_dictionary(dictionary.get('accountidentifier')) if 'accountidentifier' in dictionary.keys() else APIHelper.SKIP
        resourceidentifier = ResourceIdentifier.from_dictionary(dictionary.get('resourceidentifier')) if 'resourceidentifier' in dictionary.keys() else APIHelper.SKIP
        configuration = Configuration.from_dictionary(dictionary.get('configuration')) if 'configuration' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(accountidentifier,
                   resourceidentifier,
                   configuration)