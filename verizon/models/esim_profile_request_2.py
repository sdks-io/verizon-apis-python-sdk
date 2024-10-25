# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.esim_device_list import ESIMDeviceList


class ESIMProfileRequest2(object):

    """Implementation of the 'eSIMProfileRequest2' model.

    TODO: type model description here.

    Attributes:
        devices (List[ESIMDeviceList]): TODO: type description here.
        account_name (str): TODO: type description here.
        service_plan (str): TODO: type description here.
        mdn_zip_code (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "devices": 'devices',
        "account_name": 'accountName',
        "service_plan": 'servicePlan',
        "mdn_zip_code": 'mdnZipCode'
    }

    _optionals = [
        'devices',
        'account_name',
        'service_plan',
        'mdn_zip_code',
    ]

    def __init__(self,
                 devices=APIHelper.SKIP,
                 account_name=APIHelper.SKIP,
                 service_plan=APIHelper.SKIP,
                 mdn_zip_code=APIHelper.SKIP):
        """Constructor for the ESIMProfileRequest2 class"""

        # Initialize members of the class
        if devices is not APIHelper.SKIP:
            self.devices = devices 
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if service_plan is not APIHelper.SKIP:
            self.service_plan = service_plan 
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
        devices = None
        if dictionary.get('devices') is not None:
            devices = [ESIMDeviceList.from_dictionary(x) for x in dictionary.get('devices')]
        else:
            devices = APIHelper.SKIP
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        service_plan = dictionary.get("servicePlan") if dictionary.get("servicePlan") else APIHelper.SKIP
        mdn_zip_code = dictionary.get("mdnZipCode") if dictionary.get("mdnZipCode") else APIHelper.SKIP
        # Return an object of this model
        return cls(devices,
                   account_name,
                   service_plan,
                   mdn_zip_code)
