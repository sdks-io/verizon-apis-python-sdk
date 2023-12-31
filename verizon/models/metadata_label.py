# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class MetadataLabel(object):

    """Implementation of the 'MetadataLabel' model.

    TODO: type model description here.

    Attributes:
        alpha_rafay_io_cluster_name (string): TODO: type description here.
        alpha_rafay_io_instance_id (string): TODO: type description here.
        alpha_rafay_io_nodegroup_name (string): TODO: type description here.
        beta_kubernetes_io_arch (string): TODO: type description here.
        beta_kubernetes_io_instance_type (string): TODO: type description
            here.
        beta_kubernetes_io_os (string): TODO: type description here.
        failure_domain_beta_kubernetes_io_region (string): TODO: type
            description here.
        failure_domain_beta_kubernetes_io_zone (string): TODO: type
            description here.
        kubernetes_io_arch (string): TODO: type description here.
        kubernetes_io_hostname (string): TODO: type description here.
        kubernetes_io_os (string): TODO: type description here.
        node_lifecycle (string): TODO: type description here.
        node_kubernetes_io_instance_type (string): TODO: type description
            here.
        topology_kubernetes_io_region (string): TODO: type description here.
        topology_kubernetes_io_zone (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alpha_rafay_io_cluster_name": 'alpha.rafay.io/cluster-name',
        "alpha_rafay_io_instance_id": 'alpha.rafay.io/instance-id',
        "alpha_rafay_io_nodegroup_name": 'alpha.rafay.io/nodegroup-name',
        "beta_kubernetes_io_arch": 'beta.kubernetes.io/arch',
        "beta_kubernetes_io_instance_type": 'beta.kubernetes.io/instance-type',
        "beta_kubernetes_io_os": 'beta.kubernetes.io/os',
        "failure_domain_beta_kubernetes_io_region": 'failure-domain.beta.kubernetes.io/region',
        "failure_domain_beta_kubernetes_io_zone": 'failure-domain.beta.kubernetes.io/zone',
        "kubernetes_io_arch": 'kubernetes.io/arch',
        "kubernetes_io_hostname": 'kubernetes.io/hostname',
        "kubernetes_io_os": 'kubernetes.io/os',
        "node_lifecycle": 'node-lifecycle',
        "node_kubernetes_io_instance_type": 'node.kubernetes.io/instance-type',
        "topology_kubernetes_io_region": 'topology.kubernetes.io/region',
        "topology_kubernetes_io_zone": 'topology.kubernetes.io/zone'
    }

    _optionals = [
        'alpha_rafay_io_cluster_name',
        'alpha_rafay_io_instance_id',
        'alpha_rafay_io_nodegroup_name',
        'beta_kubernetes_io_arch',
        'beta_kubernetes_io_instance_type',
        'beta_kubernetes_io_os',
        'failure_domain_beta_kubernetes_io_region',
        'failure_domain_beta_kubernetes_io_zone',
        'kubernetes_io_arch',
        'kubernetes_io_hostname',
        'kubernetes_io_os',
        'node_lifecycle',
        'node_kubernetes_io_instance_type',
        'topology_kubernetes_io_region',
        'topology_kubernetes_io_zone',
    ]

    def __init__(self,
                 alpha_rafay_io_cluster_name=APIHelper.SKIP,
                 alpha_rafay_io_instance_id=APIHelper.SKIP,
                 alpha_rafay_io_nodegroup_name=APIHelper.SKIP,
                 beta_kubernetes_io_arch=APIHelper.SKIP,
                 beta_kubernetes_io_instance_type=APIHelper.SKIP,
                 beta_kubernetes_io_os=APIHelper.SKIP,
                 failure_domain_beta_kubernetes_io_region=APIHelper.SKIP,
                 failure_domain_beta_kubernetes_io_zone=APIHelper.SKIP,
                 kubernetes_io_arch=APIHelper.SKIP,
                 kubernetes_io_hostname=APIHelper.SKIP,
                 kubernetes_io_os=APIHelper.SKIP,
                 node_lifecycle=APIHelper.SKIP,
                 node_kubernetes_io_instance_type=APIHelper.SKIP,
                 topology_kubernetes_io_region=APIHelper.SKIP,
                 topology_kubernetes_io_zone=APIHelper.SKIP):
        """Constructor for the MetadataLabel class"""

        # Initialize members of the class
        if alpha_rafay_io_cluster_name is not APIHelper.SKIP:
            self.alpha_rafay_io_cluster_name = alpha_rafay_io_cluster_name 
        if alpha_rafay_io_instance_id is not APIHelper.SKIP:
            self.alpha_rafay_io_instance_id = alpha_rafay_io_instance_id 
        if alpha_rafay_io_nodegroup_name is not APIHelper.SKIP:
            self.alpha_rafay_io_nodegroup_name = alpha_rafay_io_nodegroup_name 
        if beta_kubernetes_io_arch is not APIHelper.SKIP:
            self.beta_kubernetes_io_arch = beta_kubernetes_io_arch 
        if beta_kubernetes_io_instance_type is not APIHelper.SKIP:
            self.beta_kubernetes_io_instance_type = beta_kubernetes_io_instance_type 
        if beta_kubernetes_io_os is not APIHelper.SKIP:
            self.beta_kubernetes_io_os = beta_kubernetes_io_os 
        if failure_domain_beta_kubernetes_io_region is not APIHelper.SKIP:
            self.failure_domain_beta_kubernetes_io_region = failure_domain_beta_kubernetes_io_region 
        if failure_domain_beta_kubernetes_io_zone is not APIHelper.SKIP:
            self.failure_domain_beta_kubernetes_io_zone = failure_domain_beta_kubernetes_io_zone 
        if kubernetes_io_arch is not APIHelper.SKIP:
            self.kubernetes_io_arch = kubernetes_io_arch 
        if kubernetes_io_hostname is not APIHelper.SKIP:
            self.kubernetes_io_hostname = kubernetes_io_hostname 
        if kubernetes_io_os is not APIHelper.SKIP:
            self.kubernetes_io_os = kubernetes_io_os 
        if node_lifecycle is not APIHelper.SKIP:
            self.node_lifecycle = node_lifecycle 
        if node_kubernetes_io_instance_type is not APIHelper.SKIP:
            self.node_kubernetes_io_instance_type = node_kubernetes_io_instance_type 
        if topology_kubernetes_io_region is not APIHelper.SKIP:
            self.topology_kubernetes_io_region = topology_kubernetes_io_region 
        if topology_kubernetes_io_zone is not APIHelper.SKIP:
            self.topology_kubernetes_io_zone = topology_kubernetes_io_zone 

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

        alpha_rafay_io_cluster_name = dictionary.get("alpha.rafay.io/cluster-name") if dictionary.get("alpha.rafay.io/cluster-name") else APIHelper.SKIP
        alpha_rafay_io_instance_id = dictionary.get("alpha.rafay.io/instance-id") if dictionary.get("alpha.rafay.io/instance-id") else APIHelper.SKIP
        alpha_rafay_io_nodegroup_name = dictionary.get("alpha.rafay.io/nodegroup-name") if dictionary.get("alpha.rafay.io/nodegroup-name") else APIHelper.SKIP
        beta_kubernetes_io_arch = dictionary.get("beta.kubernetes.io/arch") if dictionary.get("beta.kubernetes.io/arch") else APIHelper.SKIP
        beta_kubernetes_io_instance_type = dictionary.get("beta.kubernetes.io/instance-type") if dictionary.get("beta.kubernetes.io/instance-type") else APIHelper.SKIP
        beta_kubernetes_io_os = dictionary.get("beta.kubernetes.io/os") if dictionary.get("beta.kubernetes.io/os") else APIHelper.SKIP
        failure_domain_beta_kubernetes_io_region = dictionary.get("failure-domain.beta.kubernetes.io/region") if dictionary.get("failure-domain.beta.kubernetes.io/region") else APIHelper.SKIP
        failure_domain_beta_kubernetes_io_zone = dictionary.get("failure-domain.beta.kubernetes.io/zone") if dictionary.get("failure-domain.beta.kubernetes.io/zone") else APIHelper.SKIP
        kubernetes_io_arch = dictionary.get("kubernetes.io/arch") if dictionary.get("kubernetes.io/arch") else APIHelper.SKIP
        kubernetes_io_hostname = dictionary.get("kubernetes.io/hostname") if dictionary.get("kubernetes.io/hostname") else APIHelper.SKIP
        kubernetes_io_os = dictionary.get("kubernetes.io/os") if dictionary.get("kubernetes.io/os") else APIHelper.SKIP
        node_lifecycle = dictionary.get("node-lifecycle") if dictionary.get("node-lifecycle") else APIHelper.SKIP
        node_kubernetes_io_instance_type = dictionary.get("node.kubernetes.io/instance-type") if dictionary.get("node.kubernetes.io/instance-type") else APIHelper.SKIP
        topology_kubernetes_io_region = dictionary.get("topology.kubernetes.io/region") if dictionary.get("topology.kubernetes.io/region") else APIHelper.SKIP
        topology_kubernetes_io_zone = dictionary.get("topology.kubernetes.io/zone") if dictionary.get("topology.kubernetes.io/zone") else APIHelper.SKIP
        # Return an object of this model
        return cls(alpha_rafay_io_cluster_name,
                   alpha_rafay_io_instance_id,
                   alpha_rafay_io_nodegroup_name,
                   beta_kubernetes_io_arch,
                   beta_kubernetes_io_instance_type,
                   beta_kubernetes_io_os,
                   failure_domain_beta_kubernetes_io_region,
                   failure_domain_beta_kubernetes_io_zone,
                   kubernetes_io_arch,
                   kubernetes_io_hostname,
                   kubernetes_io_os,
                   node_lifecycle,
                   node_kubernetes_io_instance_type,
                   topology_kubernetes_io_region,
                   topology_kubernetes_io_zone)
