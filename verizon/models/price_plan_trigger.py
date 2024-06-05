# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.account_group_share import AccountGroupShare


class PricePlanTrigger(object):

    """Implementation of the 'PricePlanTrigger' model.

    TODO: type model description here.

    Attributes:
        account_group_share (AccountGroupShare): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_group_share": 'accountGroupShare'
    }

    _optionals = [
        'account_group_share',
    ]

    def __init__(self,
                 account_group_share=APIHelper.SKIP):
        """Constructor for the PricePlanTrigger class"""

        # Initialize members of the class
        if account_group_share is not APIHelper.SKIP:
            self.account_group_share = account_group_share 

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
        account_group_share = AccountGroupShare.from_dictionary(dictionary.get('accountGroupShare')) if 'accountGroupShare' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(account_group_share)
