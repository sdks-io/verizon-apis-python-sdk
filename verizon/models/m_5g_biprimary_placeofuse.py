# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.m_5g_bi_address import M5gBiAddress
from verizon.models.m_5g_bi_customer_name import M5gBiCustomerName


class M5gBiprimaryPlaceofuse(object):

    """Implementation of the '5gbiprimaryPlaceofuse' model.

    TODO: type model description here.

    Attributes:
        address (M5gBiAddress): TODO: type description here.
        customer_name (M5gBiCustomerName): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address": 'address',
        "customer_name": 'customerName'
    }

    _optionals = [
        'address',
        'customer_name',
    ]

    def __init__(self,
                 address=APIHelper.SKIP,
                 customer_name=APIHelper.SKIP):
        """Constructor for the M5gBiprimaryPlaceofuse class"""

        # Initialize members of the class
        if address is not APIHelper.SKIP:
            self.address = address 
        if customer_name is not APIHelper.SKIP:
            self.customer_name = customer_name 

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
        address = M5gBiAddress.from_dictionary(dictionary.get('address')) if 'address' in dictionary.keys() else APIHelper.SKIP
        customer_name = M5gBiCustomerName.from_dictionary(dictionary.get('customerName')) if 'customerName' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(address,
                   customer_name)
