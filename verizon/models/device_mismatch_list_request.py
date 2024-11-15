# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.date_filter import DateFilter


class DeviceMismatchListRequest(object):

    """Implementation of the 'DeviceMismatchListRequest' model.

    Request to list of all 4G devices with an ICCID (SIM) that was not
    activated with the expected IMEI (hardware) during a specified time frame.

    Attributes:
        filter (DateFilter): Filter out the dates.
        devices (List[AccountDeviceList]): A list of specific devices that you
            want to check, specified by ICCID or MDN.
        account_name (str): The account that you want to search for mismatched
            devices. If you don't specify an accountName, the search includes
            all devices to which you have access.
        group_name (str): The name of a device group, to only include devices
            in that group.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "filter": 'filter',
        "devices": 'devices',
        "account_name": 'accountName',
        "group_name": 'groupName'
    }

    _optionals = [
        'devices',
        'account_name',
        'group_name',
    ]

    def __init__(self,
                 filter=None,
                 devices=APIHelper.SKIP,
                 account_name=APIHelper.SKIP,
                 group_name=APIHelper.SKIP):
        """Constructor for the DeviceMismatchListRequest class"""

        # Initialize members of the class
        self.filter = filter 
        if devices is not APIHelper.SKIP:
            self.devices = devices 
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if group_name is not APIHelper.SKIP:
            self.group_name = group_name 

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
        filter = DateFilter.from_dictionary(dictionary.get('filter')) if dictionary.get('filter') else None
        devices = None
        if dictionary.get('devices') is not None:
            devices = [AccountDeviceList.from_dictionary(x) for x in dictionary.get('devices')]
        else:
            devices = APIHelper.SKIP
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        group_name = dictionary.get("groupName") if dictionary.get("groupName") else APIHelper.SKIP
        # Return an object of this model
        return cls(filter,
                   devices,
                   account_name,
                   group_name)
