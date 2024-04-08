# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.account_service import AccountService


class Engagement(object):

    """Implementation of the 'Engagement' model.

    The engagements associated with the account.

    Attributes:
        engagement_id (str): The engagement ID.
        charging_group (str): The charging group name.
        services (List[AccountService]): The services associated with the
            account.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "engagement_id": 'engagementId',
        "charging_group": 'chargingGroup',
        "services": 'services'
    }

    _optionals = [
        'engagement_id',
        'charging_group',
        'services',
    ]

    def __init__(self,
                 engagement_id=APIHelper.SKIP,
                 charging_group=APIHelper.SKIP,
                 services=APIHelper.SKIP):
        """Constructor for the Engagement class"""

        # Initialize members of the class
        if engagement_id is not APIHelper.SKIP:
            self.engagement_id = engagement_id 
        if charging_group is not APIHelper.SKIP:
            self.charging_group = charging_group 
        if services is not APIHelper.SKIP:
            self.services = services 

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
        engagement_id = dictionary.get("engagementId") if dictionary.get("engagementId") else APIHelper.SKIP
        charging_group = dictionary.get("chargingGroup") if dictionary.get("chargingGroup") else APIHelper.SKIP
        services = None
        if dictionary.get('services') is not None:
            services = [AccountService.from_dictionary(x) for x in dictionary.get('services')]
        else:
            services = APIHelper.SKIP
        # Return an object of this model
        return cls(engagement_id,
                   charging_group,
                   services)
