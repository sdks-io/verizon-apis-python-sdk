# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.models.device_list import DeviceList


class DeviceUploadRequest(object):

    """Implementation of the 'DeviceUploadRequest' model.

    TODO: type model description here.

    Attributes:
        account_name (str): TODO: type description here.
        devices (List[DeviceList]): TODO: type description here.
        email_address (str): TODO: type description here.
        device_sku (str): TODO: type description here.
        upload_type (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "devices": 'devices',
        "email_address": 'emailAddress',
        "device_sku": 'deviceSku',
        "upload_type": 'uploadType'
    }

    def __init__(self,
                 account_name=None,
                 devices=None,
                 email_address=None,
                 device_sku=None,
                 upload_type=None):
        """Constructor for the DeviceUploadRequest class"""

        # Initialize members of the class
        self.account_name = account_name 
        self.devices = devices 
        self.email_address = email_address 
        self.device_sku = device_sku 
        self.upload_type = upload_type 

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
        devices = None
        if dictionary.get('devices') is not None:
            devices = [DeviceList.from_dictionary(x) for x in dictionary.get('devices')]
        email_address = dictionary.get("emailAddress") if dictionary.get("emailAddress") else None
        device_sku = dictionary.get("deviceSku") if dictionary.get("deviceSku") else None
        upload_type = dictionary.get("uploadType") if dictionary.get("uploadType") else None
        # Return an object of this model
        return cls(account_name,
                   devices,
                   email_address,
                   device_sku,
                   upload_type)
