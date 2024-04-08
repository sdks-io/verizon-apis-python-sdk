# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.mec_platform_resource import MECPlatformResource


class ListMECPlatformsResult(object):

    """Implementation of the 'ListMECPlatformsResult' model.

    Response to return the optimal 5G Edge platforms for deployment based on a
    region, service profile of the service that you want to deploy or user
    equipment.

    Attributes:
        mec_platforms (List[MECPlatformResource]): A list of optimal MEC
            Platforms where you can register your deployed application.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mec_platforms": 'MECPlatforms'
    }

    _optionals = [
        'mec_platforms',
    ]

    def __init__(self,
                 mec_platforms=APIHelper.SKIP):
        """Constructor for the ListMECPlatformsResult class"""

        # Initialize members of the class
        if mec_platforms is not APIHelper.SKIP:
            self.mec_platforms = mec_platforms 

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
        mec_platforms = None
        if dictionary.get('MECPlatforms') is not None:
            mec_platforms = [MECPlatformResource.from_dictionary(x) for x in dictionary.get('MECPlatforms')]
        else:
            mec_platforms = APIHelper.SKIP
        # Return an object of this model
        return cls(mec_platforms)
