# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.metadata import Metadata
from verizon.models.node_status import NodeStatus
from verizon.models.service_launch_cluster_additional_params import ServiceLaunchClusterAdditionalParams


class NodeStatusItem(object):

    """Implementation of the 'NodeStatusItem' model.

    TODO: type model description here.

    Attributes:
        metadata (Metadata): TODO: type description here.
        spec (ServiceLaunchClusterAdditionalParams): TODO: type description
            here.
        status (NodeStatus): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "metadata": 'metadata',
        "spec": 'spec',
        "status": 'status'
    }

    _optionals = [
        'metadata',
        'spec',
        'status',
    ]

    def __init__(self,
                 metadata=APIHelper.SKIP,
                 spec=APIHelper.SKIP,
                 status=APIHelper.SKIP):
        """Constructor for the NodeStatusItem class"""

        # Initialize members of the class
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata 
        if spec is not APIHelper.SKIP:
            self.spec = spec 
        if status is not APIHelper.SKIP:
            self.status = status 

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

        metadata = Metadata.from_dictionary(dictionary.get('metadata')) if 'metadata' in dictionary.keys() else APIHelper.SKIP
        spec = ServiceLaunchClusterAdditionalParams.from_dictionary(dictionary.get('spec')) if 'spec' in dictionary.keys() else APIHelper.SKIP
        status = NodeStatus.from_dictionary(dictionary.get('status')) if 'status' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(metadata,
                   spec,
                   status)
