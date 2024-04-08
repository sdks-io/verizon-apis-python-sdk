# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.ready_sim_device_id import ReadySimDeviceId


class UsageRequestBody(object):

    """Implementation of the 'Usage Request Body' model.

    TODO: type model description here.

    Attributes:
        account_id (str): TODO: type description here.
        device_id (List[ReadySimDeviceId]): TODO: type description here.
        start_time (datetime): TODO: type description here.
        end_time (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id": 'accountId',
        "device_id": 'deviceId',
        "start_time": 'startTime',
        "end_time": 'endTime'
    }

    _optionals = [
        'account_id',
        'device_id',
        'start_time',
        'end_time',
    ]

    def __init__(self,
                 account_id=APIHelper.SKIP,
                 device_id=APIHelper.SKIP,
                 start_time=APIHelper.SKIP,
                 end_time=APIHelper.SKIP):
        """Constructor for the UsageRequestBody class"""

        # Initialize members of the class
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if device_id is not APIHelper.SKIP:
            self.device_id = device_id 
        if start_time is not APIHelper.SKIP:
            self.start_time = APIHelper.apply_datetime_converter(start_time, APIHelper.RFC3339DateTime) if start_time else None 
        if end_time is not APIHelper.SKIP:
            self.end_time = APIHelper.apply_datetime_converter(end_time, APIHelper.RFC3339DateTime) if end_time else None 

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
        account_id = dictionary.get("accountId") if dictionary.get("accountId") else APIHelper.SKIP
        device_id = None
        if dictionary.get('deviceId') is not None:
            device_id = [ReadySimDeviceId.from_dictionary(x) for x in dictionary.get('deviceId')]
        else:
            device_id = APIHelper.SKIP
        start_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("startTime")).datetime if dictionary.get("startTime") else APIHelper.SKIP
        end_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("endTime")).datetime if dictionary.get("endTime") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_id,
                   device_id,
                   start_time,
                   end_time)
