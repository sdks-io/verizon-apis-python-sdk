# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ManagedAccountCancelResponse(object):

    """Implementation of the 'ManagedAccountCancelResponse' model.

    TODO: type model description here.

    Attributes:
        txid (string): Transaction identifier
        account_name (string): Managed account identifier
        paccount_name (string): Primary account identifier
        service_name (ServiceNameEnum): Service name
        status (string): Deactivate/cancel status, Success or Fail
        reason (string): Detailed reason

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "txid": 'txid',
        "account_name": 'accountName',
        "paccount_name": 'paccountName',
        "service_name": 'serviceName',
        "status": 'status',
        "reason": 'reason'
    }

    def __init__(self,
                 txid=None,
                 account_name=None,
                 paccount_name=None,
                 service_name='Location',
                 status=None,
                 reason=None):
        """Constructor for the ManagedAccountCancelResponse class"""

        # Initialize members of the class
        self.txid = txid 
        self.account_name = account_name 
        self.paccount_name = paccount_name 
        self.service_name = service_name 
        self.status = status 
        self.reason = reason 

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

        txid = dictionary.get("txid") if dictionary.get("txid") else None
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else None
        paccount_name = dictionary.get("paccountName") if dictionary.get("paccountName") else None
        service_name = dictionary.get("serviceName") if dictionary.get("serviceName") else 'Location'
        status = dictionary.get("status") if dictionary.get("status") else None
        reason = dictionary.get("reason") if dictionary.get("reason") else None
        # Return an object of this model
        return cls(txid,
                   account_name,
                   paccount_name,
                   service_name,
                   status,
                   reason)