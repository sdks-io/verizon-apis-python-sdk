# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.sms_message import SMSMessage


class SMSMessagesQueryResult(object):

    """Implementation of the 'SMSMessagesQueryResult' model.

    Response to SMS messages sent by all M2M devices associated with a billing
    account.

    Attributes:
        has_more_data (bool): False for a status 200 response.True for a
            status 202 response, indicating that there is more data to be
            retrieved.
        messages (list of SMSMessage): An array of up to 100 SMS messages that
            were sent by devices in the account.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "has_more_data": 'hasMoreData',
        "messages": 'messages'
    }

    _optionals = [
        'has_more_data',
        'messages',
    ]

    def __init__(self,
                 has_more_data=APIHelper.SKIP,
                 messages=APIHelper.SKIP):
        """Constructor for the SMSMessagesQueryResult class"""

        # Initialize members of the class
        if has_more_data is not APIHelper.SKIP:
            self.has_more_data = has_more_data 
        if messages is not APIHelper.SKIP:
            self.messages = messages 

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
        messages = None
        if dictionary.get('messages') is not None:
            messages = [SMSMessage.from_dictionary(x) for x in dictionary.get('messages')]
        else:
            messages = APIHelper.SKIP
        # Return an object of this model
        return cls(has_more_data,
                   messages)
