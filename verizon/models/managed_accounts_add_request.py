# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ManagedAccountsAddRequest(object):

    """Implementation of the 'ManagedAccountsAddRequest' model.

    TODO: type model description here.

    Attributes:
        account_name (string): Account identifier
        service_name (ServiceNameEnum): Service name
        mtype (string): SKU name
        managed_acc_list (list of string): managed account list

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "service_name": 'serviceName',
        "mtype": 'type',
        "managed_acc_list": 'managedAccList'
    }

    def __init__(self,
                 account_name=None,
                 service_name='Location',
                 mtype=None,
                 managed_acc_list=None):
        """Constructor for the ManagedAccountsAddRequest class"""

        # Initialize members of the class
        self.account_name = account_name 
        self.service_name = service_name 
        self.mtype = mtype 
        self.managed_acc_list = managed_acc_list 

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
        service_name = dictionary.get("serviceName") if dictionary.get("serviceName") else 'Location'
        mtype = dictionary.get("type") if dictionary.get("type") else None
        managed_acc_list = dictionary.get("managedAccList") if dictionary.get("managedAccList") else None
        # Return an object of this model
        return cls(account_name,
                   service_name,
                   mtype,
                   managed_acc_list)