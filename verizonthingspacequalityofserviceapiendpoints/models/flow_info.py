# -*- coding: utf-8 -*-

"""
verizonthingspacequalityofserviceapiendpoints

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizonthingspacequalityofserviceapiendpoints.api_helper import APIHelper


class FlowInfo(object):

    """Implementation of the 'FlowInfo' model.

    TODO: type model description here.

    Attributes:
        flow_server (str): The IPv6 IP address and port used to connect to the
            server
        flow_device (str): The IPv6 IP address and port used by the device
        flow_direction (str): The direction the data is flowing. UPLINK if
            from the device, DOWNLINK is to the device
        flow_protocol (str): The data protocol used for the connection
        qci_option (str): The QoS level of the connection. This will be
            Standard or Premium

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "flow_server": 'flowServer',
        "flow_device": 'flowDevice',
        "flow_direction": 'flowDirection',
        "flow_protocol": 'flowProtocol',
        "qci_option": 'qciOption'
    }

    _optionals = [
        'flow_server',
        'flow_device',
        'flow_direction',
        'flow_protocol',
        'qci_option',
    ]

    def __init__(self,
                 flow_server=APIHelper.SKIP,
                 flow_device=APIHelper.SKIP,
                 flow_direction=APIHelper.SKIP,
                 flow_protocol=APIHelper.SKIP,
                 qci_option=APIHelper.SKIP):
        """Constructor for the FlowInfo class"""

        # Initialize members of the class
        if flow_server is not APIHelper.SKIP:
            self.flow_server = flow_server 
        if flow_device is not APIHelper.SKIP:
            self.flow_device = flow_device 
        if flow_direction is not APIHelper.SKIP:
            self.flow_direction = flow_direction 
        if flow_protocol is not APIHelper.SKIP:
            self.flow_protocol = flow_protocol 
        if qci_option is not APIHelper.SKIP:
            self.qci_option = qci_option 

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
        flow_server = dictionary.get("flowServer") if dictionary.get("flowServer") else APIHelper.SKIP
        flow_device = dictionary.get("flowDevice") if dictionary.get("flowDevice") else APIHelper.SKIP
        flow_direction = dictionary.get("flowDirection") if dictionary.get("flowDirection") else APIHelper.SKIP
        flow_protocol = dictionary.get("flowProtocol") if dictionary.get("flowProtocol") else APIHelper.SKIP
        qci_option = dictionary.get("qciOption") if dictionary.get("qciOption") else APIHelper.SKIP
        # Return an object of this model
        return cls(flow_server,
                   flow_device,
                   flow_direction,
                   flow_protocol,
                   qci_option)