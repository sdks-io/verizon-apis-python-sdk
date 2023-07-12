# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class StopMonitorRequest(object):

    """Implementation of the 'StopMonitorRequest' model.

    TODO: type model description here.

    Attributes:
        account_name (string): TODO: type description here.
        monitor_ids (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "monitor_ids": 'monitorIds'
    }

    def __init__(self,
                 account_name=None,
                 monitor_ids=None):
        """Constructor for the StopMonitorRequest class"""

        # Initialize members of the class
        self.account_name = account_name 
        self.monitor_ids = monitor_ids 

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

        account_name = dictionary.get("accountName") if dictionary.get("accountName") else None
        monitor_ids = dictionary.get("monitorIds") if dictionary.get("monitorIds") else None
        # Return an object of this model
        return cls(account_name,
                   monitor_ids)
