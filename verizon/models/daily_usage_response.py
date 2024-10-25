# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.daily_usage_history import DailyUsageHistory
from verizon.models.gio_device_id import GIODeviceId


class DailyUsageResponse(object):

    """Implementation of the 'dailyUsageResponse' model.

    TODO: type model description here.

    Attributes:
        has_more_data (bool): A flag set to indicate if there is more than one
            page of data returned by the query (true) or if only one page of
            data returned (false)
        device_id (GIODeviceId): TODO: type description here.
        usage_history (List[DailyUsageHistory]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "has_more_data": 'hasMoreData',
        "device_id": 'deviceId',
        "usage_history": 'usageHistory'
    }

    _optionals = [
        'has_more_data',
        'device_id',
        'usage_history',
    ]

    def __init__(self,
                 has_more_data=APIHelper.SKIP,
                 device_id=APIHelper.SKIP,
                 usage_history=APIHelper.SKIP):
        """Constructor for the DailyUsageResponse class"""

        # Initialize members of the class
        if has_more_data is not APIHelper.SKIP:
            self.has_more_data = has_more_data 
        if device_id is not APIHelper.SKIP:
            self.device_id = device_id 
        if usage_history is not APIHelper.SKIP:
            self.usage_history = usage_history 

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
        has_more_data = dictionary.get("hasMoreData") if "hasMoreData" in dictionary.keys() else APIHelper.SKIP
        device_id = GIODeviceId.from_dictionary(dictionary.get('deviceId')) if 'deviceId' in dictionary.keys() else APIHelper.SKIP
        usage_history = None
        if dictionary.get('usageHistory') is not None:
            usage_history = [DailyUsageHistory.from_dictionary(x) for x in dictionary.get('usageHistory')]
        else:
            usage_history = APIHelper.SKIP
        # Return an object of this model
        return cls(has_more_data,
                   device_id,
                   usage_history)