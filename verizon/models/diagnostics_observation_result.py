# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class DiagnosticsObservationResult(object):

    """Implementation of the 'DiagnosticsObservationResult' model.

    A success response containing the current status of the request.

    Attributes:
        transaction_id (string): Transaction identifier.
        status (string): Status of the request.
        created_on (datetime): The date and time of when this request was
            created.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "transaction_id": 'transactionID',
        "status": 'status',
        "created_on": 'createdOn'
    }

    def __init__(self,
                 transaction_id=None,
                 status=None,
                 created_on=None):
        """Constructor for the DiagnosticsObservationResult class"""

        # Initialize members of the class
        self.transaction_id = transaction_id 
        self.status = status 
        self.created_on = APIHelper.RFC3339DateTime(created_on) if created_on else None 

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

        transaction_id = dictionary.get("transactionID") if dictionary.get("transactionID") else None
        status = dictionary.get("status") if dictionary.get("status") else None
        created_on = APIHelper.RFC3339DateTime.from_value(dictionary.get("createdOn")).datetime if dictionary.get("createdOn") else None
        # Return an object of this model
        return cls(transaction_id,
                   status,
                   created_on)