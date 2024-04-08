# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class ServiceUsage(object):

    """Implementation of the 'ServiceUsage' model.

    TODO: type model description here.

    Attributes:
        account_name (str): Account identifier.
        transactions_count (str): Total requests for the account during the
            reporting period.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "transactions_count": 'transactionsCount'
    }

    _optionals = [
        'account_name',
        'transactions_count',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 transactions_count=APIHelper.SKIP):
        """Constructor for the ServiceUsage class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if transactions_count is not APIHelper.SKIP:
            self.transactions_count = transactions_count 

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
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        transactions_count = dictionary.get("transactionsCount") if dictionary.get("transactionsCount") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   transactions_count)
