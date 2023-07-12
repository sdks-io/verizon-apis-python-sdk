# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class DevicesConsentResult(object):

    """Implementation of the 'DevicesConsentResult' model.

    TODO: type model description here.

    Attributes:
        account_name (string): Account identifier in "##########-#####".
        all_device (bool): Exclude all devices or not?
        has_more_data (bool): Are there more devices to retrieve or not?
        total_count (int): Total number of excluded devices in the account.
        update_time (string): Last update time.
        exclusion (list of string): Device ID list.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "all_device": 'allDevice',
        "has_more_data": 'hasMoreData',
        "total_count": 'totalCount',
        "update_time": 'updateTime',
        "exclusion": 'exclusion'
    }

    _optionals = [
        'account_name',
        'all_device',
        'has_more_data',
        'total_count',
        'update_time',
        'exclusion',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 all_device=APIHelper.SKIP,
                 has_more_data=APIHelper.SKIP,
                 total_count=APIHelper.SKIP,
                 update_time=APIHelper.SKIP,
                 exclusion=APIHelper.SKIP):
        """Constructor for the DevicesConsentResult class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if all_device is not APIHelper.SKIP:
            self.all_device = all_device 
        if has_more_data is not APIHelper.SKIP:
            self.has_more_data = has_more_data 
        if total_count is not APIHelper.SKIP:
            self.total_count = total_count 
        if update_time is not APIHelper.SKIP:
            self.update_time = update_time 
        if exclusion is not APIHelper.SKIP:
            self.exclusion = exclusion 

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
        all_device = dictionary.get("allDevice") if "allDevice" in dictionary.keys() else APIHelper.SKIP
        has_more_data = dictionary.get("hasMoreData") if "hasMoreData" in dictionary.keys() else APIHelper.SKIP
        total_count = dictionary.get("totalCount") if dictionary.get("totalCount") else APIHelper.SKIP
        update_time = dictionary.get("updateTime") if dictionary.get("updateTime") else APIHelper.SKIP
        exclusion = dictionary.get("exclusion") if dictionary.get("exclusion") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   all_device,
                   has_more_data,
                   total_count,
                   update_time,
                   exclusion)