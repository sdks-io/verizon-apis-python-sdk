# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class CarrierServicePlan(object):

    """Implementation of the 'CarrierServicePlan' model.

    TODO: type model description here.

    Attributes:
        name (str): The name of the service plan
        code (str): The inventory name or system name of the service plan
        size_kb (str): The ammount of space the service plan will occupy on
            the Subscriber Information Module (SIM)
        carrier_service_plan_code (str): The billing record ID. This can be
            numeric, alpha or alphanumeric.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "code": 'code',
        "size_kb": 'sizeKb',
        "carrier_service_plan_code": 'carrierServicePlanCode'
    }

    _optionals = [
        'name',
        'code',
        'size_kb',
        'carrier_service_plan_code',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 code=APIHelper.SKIP,
                 size_kb=APIHelper.SKIP,
                 carrier_service_plan_code=APIHelper.SKIP):
        """Constructor for the CarrierServicePlan class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if code is not APIHelper.SKIP:
            self.code = code 
        if size_kb is not APIHelper.SKIP:
            self.size_kb = size_kb 
        if carrier_service_plan_code is not APIHelper.SKIP:
            self.carrier_service_plan_code = carrier_service_plan_code 

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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        code = dictionary.get("code") if dictionary.get("code") else APIHelper.SKIP
        size_kb = dictionary.get("sizeKb") if dictionary.get("sizeKb") else APIHelper.SKIP
        carrier_service_plan_code = dictionary.get("carrierServicePlanCode") if dictionary.get("carrierServicePlanCode") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   code,
                   size_kb,
                   carrier_service_plan_code)