# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.service_instance import ServiceInstance


class ServiceInstancesResultSetItem(object):

    """Implementation of the 'ServiceInstancesResultSetItem' model.

    TODO: type model description here.

    Attributes:
        status_url (string): URL to check the status of the add service.
        request_id (string): A unique Id assigned to the request by system
            calling API.
        correlation_id (string): TODO: type description here.
        status (string): Status of the added service.
        state (string): State of the service instance.
        service (ServiceInstance): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status_url": 'statusUrl',
        "request_id": 'requestId',
        "correlation_id": 'correlationId',
        "status": 'status',
        "state": 'state',
        "service": 'service'
    }

    _optionals = [
        'status_url',
        'request_id',
        'correlation_id',
        'status',
        'state',
        'service',
    ]

    def __init__(self,
                 status_url=APIHelper.SKIP,
                 request_id=APIHelper.SKIP,
                 correlation_id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 state=APIHelper.SKIP,
                 service=APIHelper.SKIP):
        """Constructor for the ServiceInstancesResultSetItem class"""

        # Initialize members of the class
        if status_url is not APIHelper.SKIP:
            self.status_url = status_url 
        if request_id is not APIHelper.SKIP:
            self.request_id = request_id 
        if correlation_id is not APIHelper.SKIP:
            self.correlation_id = correlation_id 
        if status is not APIHelper.SKIP:
            self.status = status 
        if state is not APIHelper.SKIP:
            self.state = state 
        if service is not APIHelper.SKIP:
            self.service = service 

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

        status_url = dictionary.get("statusUrl") if dictionary.get("statusUrl") else APIHelper.SKIP
        request_id = dictionary.get("requestId") if dictionary.get("requestId") else APIHelper.SKIP
        correlation_id = dictionary.get("correlationId") if dictionary.get("correlationId") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        service = ServiceInstance.from_dictionary(dictionary.get('service')) if 'service' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(status_url,
                   request_id,
                   correlation_id,
                   status,
                   state,
                   service)
