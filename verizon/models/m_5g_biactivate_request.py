# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.device_list_with_service_address_1 import DeviceListWithServiceAddress1


class M5gBiactivateRequest(object):

    """Implementation of the '5gbiactivateRequest' model.

    TODO: type model description here.

    Attributes:
        account_name (str): TODO: type description here.
        service_plan (str): TODO: type description here.
        device_list_with_service_address
            (List[DeviceListWithServiceAddress1]): TODO: type description here.
        public_ip_restriction (str): TODO: type description here.
        carrier_name (str): TODO: type description here.
        mdn_zip_code (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "service_plan": 'servicePlan',
        "device_list_with_service_address": 'deviceListWithServiceAddress',
        "public_ip_restriction": 'publicIpRestriction',
        "carrier_name": 'carrierName',
        "mdn_zip_code": 'mdnZipCode'
    }

    _optionals = [
        'account_name',
        'service_plan',
        'device_list_with_service_address',
        'public_ip_restriction',
        'carrier_name',
        'mdn_zip_code',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 service_plan=APIHelper.SKIP,
                 device_list_with_service_address=APIHelper.SKIP,
                 public_ip_restriction=APIHelper.SKIP,
                 carrier_name=APIHelper.SKIP,
                 mdn_zip_code=APIHelper.SKIP):
        """Constructor for the M5gBiactivateRequest class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if service_plan is not APIHelper.SKIP:
            self.service_plan = service_plan 
        if device_list_with_service_address is not APIHelper.SKIP:
            self.device_list_with_service_address = device_list_with_service_address 
        if public_ip_restriction is not APIHelper.SKIP:
            self.public_ip_restriction = public_ip_restriction 
        if carrier_name is not APIHelper.SKIP:
            self.carrier_name = carrier_name 
        if mdn_zip_code is not APIHelper.SKIP:
            self.mdn_zip_code = mdn_zip_code 

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
        service_plan = dictionary.get("servicePlan") if dictionary.get("servicePlan") else APIHelper.SKIP
        device_list_with_service_address = None
        if dictionary.get('deviceListWithServiceAddress') is not None:
            device_list_with_service_address = [DeviceListWithServiceAddress1.from_dictionary(x) for x in dictionary.get('deviceListWithServiceAddress')]
        else:
            device_list_with_service_address = APIHelper.SKIP
        public_ip_restriction = dictionary.get("publicIpRestriction") if dictionary.get("publicIpRestriction") else APIHelper.SKIP
        carrier_name = dictionary.get("carrierName") if dictionary.get("carrierName") else APIHelper.SKIP
        mdn_zip_code = dictionary.get("mdnZipCode") if dictionary.get("mdnZipCode") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   service_plan,
                   device_list_with_service_address,
                   public_ip_restriction,
                   carrier_name,
                   mdn_zip_code)