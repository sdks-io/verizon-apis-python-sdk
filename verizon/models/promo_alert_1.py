# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.keyschunk_2 import Keyschunk2


class PromoAlert1(object):

    """Implementation of the 'PromoAlert1' model.

    TODO: type model description here.

    Attributes:
        filter_criteria (List[object]): TODO: type description here.
        condition (List[Keyschunk2]): TODO: type description here.
        enable_promo_exp (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "filter_criteria": 'filterCriteria',
        "condition": 'condition',
        "enable_promo_exp": 'enablePromoExp'
    }

    _optionals = [
        'filter_criteria',
        'condition',
        'enable_promo_exp',
    ]

    def __init__(self,
                 filter_criteria=APIHelper.SKIP,
                 condition=APIHelper.SKIP,
                 enable_promo_exp=APIHelper.SKIP):
        """Constructor for the PromoAlert1 class"""

        # Initialize members of the class
        if filter_criteria is not APIHelper.SKIP:
            self.filter_criteria = filter_criteria 
        if condition is not APIHelper.SKIP:
            self.condition = condition 
        if enable_promo_exp is not APIHelper.SKIP:
            self.enable_promo_exp = enable_promo_exp 

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
        filter_criteria = dictionary.get("filterCriteria") if dictionary.get("filterCriteria") else APIHelper.SKIP
        condition = None
        if dictionary.get('condition') is not None:
            condition = [Keyschunk2.from_dictionary(x) for x in dictionary.get('condition')]
        else:
            condition = APIHelper.SKIP
        enable_promo_exp = dictionary.get("enablePromoExp") if "enablePromoExp" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(filter_criteria,
                   condition,
                   enable_promo_exp)