# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class AdvanceConfiguration(object):

    """Implementation of the 'AdvanceConfiguration' model.

    TODO: type model description here.

    Attributes:
        service_role_arn (string): TODO: type description here.
        service_role_permission_boundary (string): TODO: type description
            here.
        enable_proxy (bool): TODO: type description here.
        http_proxy (string): TODO: type description here.
        https_proxy (string): TODO: type description here.
        no_proxy (string): TODO: type description here.
        proxy_root_ca (string): TODO: type description here.
        enable_tls_traffic (bool): TODO: type description here.
        enable_auto_approve (bool): TODO: type description here.
        enable_multi_master (bool): TODO: type description here.
        enable_dedicated_master (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "service_role_arn": 'serviceRoleArn',
        "service_role_permission_boundary": 'serviceRolePermissionBoundary',
        "enable_proxy": 'enableProxy',
        "http_proxy": 'httpProxy',
        "https_proxy": 'httpsProxy',
        "no_proxy": 'noProxy',
        "proxy_root_ca": 'proxyRootCA',
        "enable_tls_traffic": 'enableTlsTraffic',
        "enable_auto_approve": 'enableAutoApprove',
        "enable_multi_master": 'enableMultiMaster',
        "enable_dedicated_master": 'enableDedicatedMaster'
    }

    _optionals = [
        'service_role_arn',
        'service_role_permission_boundary',
        'enable_proxy',
        'http_proxy',
        'https_proxy',
        'no_proxy',
        'proxy_root_ca',
        'enable_tls_traffic',
        'enable_auto_approve',
        'enable_multi_master',
        'enable_dedicated_master',
    ]

    def __init__(self,
                 service_role_arn=APIHelper.SKIP,
                 service_role_permission_boundary=APIHelper.SKIP,
                 enable_proxy=False,
                 http_proxy=APIHelper.SKIP,
                 https_proxy=APIHelper.SKIP,
                 no_proxy=APIHelper.SKIP,
                 proxy_root_ca=APIHelper.SKIP,
                 enable_tls_traffic=False,
                 enable_auto_approve=False,
                 enable_multi_master=False,
                 enable_dedicated_master=False):
        """Constructor for the AdvanceConfiguration class"""

        # Initialize members of the class
        if service_role_arn is not APIHelper.SKIP:
            self.service_role_arn = service_role_arn 
        if service_role_permission_boundary is not APIHelper.SKIP:
            self.service_role_permission_boundary = service_role_permission_boundary 
        self.enable_proxy = enable_proxy 
        if http_proxy is not APIHelper.SKIP:
            self.http_proxy = http_proxy 
        if https_proxy is not APIHelper.SKIP:
            self.https_proxy = https_proxy 
        if no_proxy is not APIHelper.SKIP:
            self.no_proxy = no_proxy 
        if proxy_root_ca is not APIHelper.SKIP:
            self.proxy_root_ca = proxy_root_ca 
        self.enable_tls_traffic = enable_tls_traffic 
        self.enable_auto_approve = enable_auto_approve 
        self.enable_multi_master = enable_multi_master 
        self.enable_dedicated_master = enable_dedicated_master 

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

        service_role_arn = dictionary.get("serviceRoleArn") if dictionary.get("serviceRoleArn") else APIHelper.SKIP
        service_role_permission_boundary = dictionary.get("serviceRolePermissionBoundary") if dictionary.get("serviceRolePermissionBoundary") else APIHelper.SKIP
        enable_proxy = dictionary.get("enableProxy") if dictionary.get("enableProxy") else False
        http_proxy = dictionary.get("httpProxy") if dictionary.get("httpProxy") else APIHelper.SKIP
        https_proxy = dictionary.get("httpsProxy") if dictionary.get("httpsProxy") else APIHelper.SKIP
        no_proxy = dictionary.get("noProxy") if dictionary.get("noProxy") else APIHelper.SKIP
        proxy_root_ca = dictionary.get("proxyRootCA") if dictionary.get("proxyRootCA") else APIHelper.SKIP
        enable_tls_traffic = dictionary.get("enableTlsTraffic") if dictionary.get("enableTlsTraffic") else False
        enable_auto_approve = dictionary.get("enableAutoApprove") if dictionary.get("enableAutoApprove") else False
        enable_multi_master = dictionary.get("enableMultiMaster") if dictionary.get("enableMultiMaster") else False
        enable_dedicated_master = dictionary.get("enableDedicatedMaster") if dictionary.get("enableDedicatedMaster") else False
        # Return an object of this model
        return cls(service_role_arn,
                   service_role_permission_boundary,
                   enable_proxy,
                   http_proxy,
                   https_proxy,
                   no_proxy,
                   proxy_root_ca,
                   enable_tls_traffic,
                   enable_auto_approve,
                   enable_multi_master,
                   enable_dedicated_master)
