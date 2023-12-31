# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.claim import Claim


class ServiceClaims(object):

    """Implementation of the 'ServiceClaims' model.

    Response to get all claims.

    Attributes:
        count (int): Count for all the claims returned after hitting the API.
        claims_res_list (list of Claim): List of all claims.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "count": 'count',
        "claims_res_list": 'claimsResList'
    }

    _optionals = [
        'count',
        'claims_res_list',
    ]

    def __init__(self,
                 count=APIHelper.SKIP,
                 claims_res_list=APIHelper.SKIP):
        """Constructor for the ServiceClaims class"""

        # Initialize members of the class
        if count is not APIHelper.SKIP:
            self.count = count 
        if claims_res_list is not APIHelper.SKIP:
            self.claims_res_list = claims_res_list 

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

        count = dictionary.get("count") if dictionary.get("count") else APIHelper.SKIP
        claims_res_list = None
        if dictionary.get('claimsResList') is not None:
            claims_res_list = [Claim.from_dictionary(x) for x in dictionary.get('claimsResList')]
        else:
            claims_res_list = APIHelper.SKIP
        # Return an object of this model
        return cls(count,
                   claims_res_list)
