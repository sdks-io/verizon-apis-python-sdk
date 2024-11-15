# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class M5gBiAddress(object):

    """Implementation of the '5gbiAddress' model.

    TODO: type model description here.

    Attributes:
        address_line_1 (str): TODO: type description here.
        city (str): TODO: type description here.
        state (str): TODO: type description here.
        zip (str): TODO: type description here.
        zip_4 (str): TODO: type description here.
        phone (str): TODO: type description here.
        phone_type (str): TODO: type description here.
        email_address (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address_line_1": 'addressLine1',
        "city": 'city',
        "state": 'state',
        "zip": 'zip',
        "zip_4": 'zip+4',
        "phone": 'phone',
        "phone_type": 'phoneType',
        "email_address": 'emailAddress'
    }

    _optionals = [
        'address_line_1',
        'city',
        'state',
        'zip',
        'zip_4',
        'phone',
        'phone_type',
        'email_address',
    ]

    def __init__(self,
                 address_line_1=APIHelper.SKIP,
                 city=APIHelper.SKIP,
                 state=APIHelper.SKIP,
                 zip=APIHelper.SKIP,
                 zip_4=APIHelper.SKIP,
                 phone=APIHelper.SKIP,
                 phone_type=APIHelper.SKIP,
                 email_address=APIHelper.SKIP):
        """Constructor for the M5gBiAddress class"""

        # Initialize members of the class
        if address_line_1 is not APIHelper.SKIP:
            self.address_line_1 = address_line_1 
        if city is not APIHelper.SKIP:
            self.city = city 
        if state is not APIHelper.SKIP:
            self.state = state 
        if zip is not APIHelper.SKIP:
            self.zip = zip 
        if zip_4 is not APIHelper.SKIP:
            self.zip_4 = zip_4 
        if phone is not APIHelper.SKIP:
            self.phone = phone 
        if phone_type is not APIHelper.SKIP:
            self.phone_type = phone_type 
        if email_address is not APIHelper.SKIP:
            self.email_address = email_address 

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
        address_line_1 = dictionary.get("addressLine1") if dictionary.get("addressLine1") else APIHelper.SKIP
        city = dictionary.get("city") if dictionary.get("city") else APIHelper.SKIP
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        zip = dictionary.get("zip") if dictionary.get("zip") else APIHelper.SKIP
        zip_4 = dictionary.get("zip+4") if dictionary.get("zip+4") else APIHelper.SKIP
        phone = dictionary.get("phone") if dictionary.get("phone") else APIHelper.SKIP
        phone_type = dictionary.get("phoneType") if dictionary.get("phoneType") else APIHelper.SKIP
        email_address = dictionary.get("emailAddress") if dictionary.get("emailAddress") else APIHelper.SKIP
        # Return an object of this model
        return cls(address_line_1,
                   city,
                   state,
                   zip,
                   zip_4,
                   phone,
                   phone_type,
                   email_address)
