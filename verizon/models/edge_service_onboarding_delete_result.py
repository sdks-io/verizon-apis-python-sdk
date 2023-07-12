# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class EdgeServiceOnboardingDeleteResult(object):

    """Implementation of the 'EdgeServiceOnboardingDeleteResult' model.

    Response to delete a service.

    Attributes:
        message (string): Message confirms if the action was success or
            failure.
        status (string): Will provide the current status of the action.
        sub_status (string): Displays the proper response with status.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message": 'message',
        "status": 'status',
        "sub_status": 'subStatus'
    }

    _optionals = [
        'message',
        'status',
        'sub_status',
    ]

    def __init__(self,
                 message=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 sub_status=APIHelper.SKIP):
        """Constructor for the EdgeServiceOnboardingDeleteResult class"""

        # Initialize members of the class
        if message is not APIHelper.SKIP:
            self.message = message 
        if status is not APIHelper.SKIP:
            self.status = status 
        if sub_status is not APIHelper.SKIP:
            self.sub_status = sub_status 

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

        message = dictionary.get("message") if dictionary.get("message") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        sub_status = dictionary.get("subStatus") if dictionary.get("subStatus") else APIHelper.SKIP
        # Return an object of this model
        return cls(message,
                   status,
                   sub_status)
