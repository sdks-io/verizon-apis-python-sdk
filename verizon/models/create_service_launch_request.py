# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class CreateServiceLaunchRequest(object):

    """Implementation of the 'CreateServiceLaunchRequest' model.

    TODO: type model description here.

    Attributes:
        name (string): Name of the received request.
        service_name (string): Service being deployed.
        csp_profile_id (string): TODO: type description here.
        service_profile_id (string): The service profile ID that is created
            during the post-service API.
        service_version (string): Service version being deployed.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "csp_profile_id": 'cspProfileId',
        "service_profile_id": 'serviceProfileId',
        "service_name": 'serviceName',
        "service_version": 'serviceVersion'
    }

    _optionals = [
        'service_name',
        'service_version',
    ]

    def __init__(self,
                 name=None,
                 csp_profile_id=None,
                 service_profile_id=None,
                 service_name=APIHelper.SKIP,
                 service_version=APIHelper.SKIP):
        """Constructor for the CreateServiceLaunchRequest class"""

        # Initialize members of the class
        self.name = name 
        if service_name is not APIHelper.SKIP:
            self.service_name = service_name 
        self.csp_profile_id = csp_profile_id 
        self.service_profile_id = service_profile_id 
        if service_version is not APIHelper.SKIP:
            self.service_version = service_version 

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

        name = dictionary.get("name") if dictionary.get("name") else None
        csp_profile_id = dictionary.get("cspProfileId") if dictionary.get("cspProfileId") else None
        service_profile_id = dictionary.get("serviceProfileId") if dictionary.get("serviceProfileId") else None
        service_name = dictionary.get("serviceName") if dictionary.get("serviceName") else APIHelper.SKIP
        service_version = dictionary.get("serviceVersion") if dictionary.get("serviceVersion") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   csp_profile_id,
                   service_profile_id,
                   service_name,
                   service_version)