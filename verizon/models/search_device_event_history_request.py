# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.account_identifier import AccountIdentifier
from verizon.models.resource_identifier import ResourceIdentifier


class SearchDeviceEventHistoryRequest(object):

    """Implementation of the 'SearchDeviceEventHistoryRequest' model.

    Search Device By Property resource definition.

    Attributes:
        accountidentifier (AccountIdentifier): The ID of the authenticating
            billing account, in the format
            `{"billingaccountid":"1234567890-12345"}`.
        selection (Dict[str, str]): A comma-separated list of properties and
            comparator values to match against subscriptions in the ThingSpace
            account. See Working with Query Filters for more information. If
            the request does not include `$selection`, the response will
            include all subscriptions to which the requesting user has access.
        resourceidentifier (ResourceIdentifier): The ID of the target to
            delete, in the format {"id":
            "dd1682d3-2d80-cefc-f3ee-25154800beff"}.
        limitnumber (int): The maximum number of events to include in the
            response.
        page (str): The maximum number of events to include in the response.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "accountidentifier": 'accountidentifier',
        "resourceidentifier": 'resourceidentifier',
        "selection": '$selection',
        "limitnumber": '$limitnumber',
        "page": '$page'
    }

    _optionals = [
        'selection',
        'limitnumber',
        'page',
    ]

    def __init__(self,
                 accountidentifier=None,
                 resourceidentifier=None,
                 selection=APIHelper.SKIP,
                 limitnumber=APIHelper.SKIP,
                 page=APIHelper.SKIP):
        """Constructor for the SearchDeviceEventHistoryRequest class"""

        # Initialize members of the class
        self.accountidentifier = accountidentifier 
        if selection is not APIHelper.SKIP:
            self.selection = selection 
        self.resourceidentifier = resourceidentifier 
        if limitnumber is not APIHelper.SKIP:
            self.limitnumber = limitnumber 
        if page is not APIHelper.SKIP:
            self.page = page 

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
        accountidentifier = AccountIdentifier.from_dictionary(dictionary.get('accountidentifier')) if dictionary.get('accountidentifier') else None
        resourceidentifier = ResourceIdentifier.from_dictionary(dictionary.get('resourceidentifier')) if dictionary.get('resourceidentifier') else None
        selection = dictionary.get("$selection") if dictionary.get("$selection") else APIHelper.SKIP
        limitnumber = dictionary.get("$limitnumber") if dictionary.get("$limitnumber") else APIHelper.SKIP
        page = dictionary.get("$page") if dictionary.get("$page") else APIHelper.SKIP
        # Return an object of this model
        return cls(accountidentifier,
                   resourceidentifier,
                   selection,
                   limitnumber,
                   page)
