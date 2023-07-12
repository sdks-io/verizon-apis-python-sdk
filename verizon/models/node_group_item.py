# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.node_group_item_tag import NodeGroupItemTag
from verizon.models.node_label import NodeLabel
from verizon.models.provision import Provision
from verizon.models.upgrade_info import UpgradeInfo
from verizon.models.version_info import VersionInfo


class NodeGroupItem(object):

    """Implementation of the 'NodeGroupItem' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        created_at (string): TODO: type description here.
        modified_at (string): TODO: type description here.
        organization_id (string): TODO: type description here.
        partner_id (string): TODO: type description here.
        instance_type (string): TODO: type description here.
        edge_id (string): TODO: type description here.
        id (string): TODO: type description here.
        provision_id (string): TODO: type description here.
        node_type (string): TODO: type description here.
        nodes (int): TODO: type description here.
        nodes_min (int): TODO: type description here.
        nodes_max (int): TODO: type description here.
        node_volume_size (int): TODO: type description here.
        node_volume_type (string): TODO: type description here.
        node_private_networking (bool): TODO: type description here.
        node_zones (list of string): TODO: type description here.
        node_ami_family (string): TODO: type description here.
        node_labels (NodeLabel): TODO: type description here.
        nodegroup_type (int): TODO: type description here.
        enable_asg_access (bool): TODO: type description here.
        enable_full_access_to_ecr (bool): TODO: type description here.
        version_info_id (string): TODO: type description here.
        upgrade_info_id (string): TODO: type description here.
        tags (NodeGroupItemTag): TODO: type description here.
        config_file_content (string): TODO: type description here.
        provision (Provision): TODO: type description here.
        version_info (VersionInfo): TODO: type description here.
        upgrade_info (UpgradeInfo): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "created_at": 'created_at',
        "modified_at": 'modified_at',
        "organization_id": 'organization_id',
        "partner_id": 'partner_id',
        "instance_type": 'instance_type',
        "edge_id": 'edge_id',
        "id": 'id',
        "provision_id": 'provision_id',
        "node_type": 'node_type',
        "nodes": 'nodes',
        "nodes_min": 'nodes_min',
        "nodes_max": 'nodes_max',
        "node_volume_size": 'node_volume_size',
        "node_volume_type": 'node_volume_type',
        "node_private_networking": 'node_private_networking',
        "node_zones": 'node_zones',
        "node_ami_family": 'node_ami_family',
        "node_labels": 'node_labels',
        "nodegroup_type": 'nodegroup_type',
        "enable_asg_access": 'enable_asg_access',
        "enable_full_access_to_ecr": 'enable_full_access_to_ecr',
        "version_info_id": 'version_info_id',
        "upgrade_info_id": 'upgrade_info_id',
        "tags": 'tags',
        "config_file_content": 'config_file_content',
        "provision": 'provision',
        "version_info": 'version_info',
        "upgrade_info": 'upgrade_info'
    }

    _optionals = [
        'name',
        'created_at',
        'modified_at',
        'organization_id',
        'partner_id',
        'instance_type',
        'edge_id',
        'id',
        'provision_id',
        'node_type',
        'nodes',
        'nodes_min',
        'nodes_max',
        'node_volume_size',
        'node_volume_type',
        'node_private_networking',
        'node_zones',
        'node_ami_family',
        'node_labels',
        'nodegroup_type',
        'enable_asg_access',
        'enable_full_access_to_ecr',
        'version_info_id',
        'upgrade_info_id',
        'tags',
        'config_file_content',
        'provision',
        'version_info',
        'upgrade_info',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 modified_at=APIHelper.SKIP,
                 organization_id=APIHelper.SKIP,
                 partner_id=APIHelper.SKIP,
                 instance_type=APIHelper.SKIP,
                 edge_id=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 provision_id=APIHelper.SKIP,
                 node_type=APIHelper.SKIP,
                 nodes=APIHelper.SKIP,
                 nodes_min=APIHelper.SKIP,
                 nodes_max=APIHelper.SKIP,
                 node_volume_size=APIHelper.SKIP,
                 node_volume_type=APIHelper.SKIP,
                 node_private_networking=APIHelper.SKIP,
                 node_zones=APIHelper.SKIP,
                 node_ami_family=APIHelper.SKIP,
                 node_labels=APIHelper.SKIP,
                 nodegroup_type=APIHelper.SKIP,
                 enable_asg_access=APIHelper.SKIP,
                 enable_full_access_to_ecr=APIHelper.SKIP,
                 version_info_id=APIHelper.SKIP,
                 upgrade_info_id=APIHelper.SKIP,
                 tags=APIHelper.SKIP,
                 config_file_content=APIHelper.SKIP,
                 provision=APIHelper.SKIP,
                 version_info=APIHelper.SKIP,
                 upgrade_info=APIHelper.SKIP):
        """Constructor for the NodeGroupItem class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if modified_at is not APIHelper.SKIP:
            self.modified_at = modified_at 
        if organization_id is not APIHelper.SKIP:
            self.organization_id = organization_id 
        if partner_id is not APIHelper.SKIP:
            self.partner_id = partner_id 
        if instance_type is not APIHelper.SKIP:
            self.instance_type = instance_type 
        if edge_id is not APIHelper.SKIP:
            self.edge_id = edge_id 
        if id is not APIHelper.SKIP:
            self.id = id 
        if provision_id is not APIHelper.SKIP:
            self.provision_id = provision_id 
        if node_type is not APIHelper.SKIP:
            self.node_type = node_type 
        if nodes is not APIHelper.SKIP:
            self.nodes = nodes 
        if nodes_min is not APIHelper.SKIP:
            self.nodes_min = nodes_min 
        if nodes_max is not APIHelper.SKIP:
            self.nodes_max = nodes_max 
        if node_volume_size is not APIHelper.SKIP:
            self.node_volume_size = node_volume_size 
        if node_volume_type is not APIHelper.SKIP:
            self.node_volume_type = node_volume_type 
        if node_private_networking is not APIHelper.SKIP:
            self.node_private_networking = node_private_networking 
        if node_zones is not APIHelper.SKIP:
            self.node_zones = node_zones 
        if node_ami_family is not APIHelper.SKIP:
            self.node_ami_family = node_ami_family 
        if node_labels is not APIHelper.SKIP:
            self.node_labels = node_labels 
        if nodegroup_type is not APIHelper.SKIP:
            self.nodegroup_type = nodegroup_type 
        if enable_asg_access is not APIHelper.SKIP:
            self.enable_asg_access = enable_asg_access 
        if enable_full_access_to_ecr is not APIHelper.SKIP:
            self.enable_full_access_to_ecr = enable_full_access_to_ecr 
        if version_info_id is not APIHelper.SKIP:
            self.version_info_id = version_info_id 
        if upgrade_info_id is not APIHelper.SKIP:
            self.upgrade_info_id = upgrade_info_id 
        if tags is not APIHelper.SKIP:
            self.tags = tags 
        if config_file_content is not APIHelper.SKIP:
            self.config_file_content = config_file_content 
        if provision is not APIHelper.SKIP:
            self.provision = provision 
        if version_info is not APIHelper.SKIP:
            self.version_info = version_info 
        if upgrade_info is not APIHelper.SKIP:
            self.upgrade_info = upgrade_info 

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

        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else APIHelper.SKIP
        modified_at = dictionary.get("modified_at") if dictionary.get("modified_at") else APIHelper.SKIP
        organization_id = dictionary.get("organization_id") if dictionary.get("organization_id") else APIHelper.SKIP
        partner_id = dictionary.get("partner_id") if dictionary.get("partner_id") else APIHelper.SKIP
        instance_type = dictionary.get("instance_type") if dictionary.get("instance_type") else APIHelper.SKIP
        edge_id = dictionary.get("edge_id") if dictionary.get("edge_id") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        provision_id = dictionary.get("provision_id") if dictionary.get("provision_id") else APIHelper.SKIP
        node_type = dictionary.get("node_type") if dictionary.get("node_type") else APIHelper.SKIP
        nodes = dictionary.get("nodes") if dictionary.get("nodes") else APIHelper.SKIP
        nodes_min = dictionary.get("nodes_min") if dictionary.get("nodes_min") else APIHelper.SKIP
        nodes_max = dictionary.get("nodes_max") if dictionary.get("nodes_max") else APIHelper.SKIP
        node_volume_size = dictionary.get("node_volume_size") if dictionary.get("node_volume_size") else APIHelper.SKIP
        node_volume_type = dictionary.get("node_volume_type") if dictionary.get("node_volume_type") else APIHelper.SKIP
        node_private_networking = dictionary.get("node_private_networking") if "node_private_networking" in dictionary.keys() else APIHelper.SKIP
        node_zones = dictionary.get("node_zones") if dictionary.get("node_zones") else APIHelper.SKIP
        node_ami_family = dictionary.get("node_ami_family") if dictionary.get("node_ami_family") else APIHelper.SKIP
        node_labels = NodeLabel.from_dictionary(dictionary.get('node_labels')) if 'node_labels' in dictionary.keys() else APIHelper.SKIP
        nodegroup_type = dictionary.get("nodegroup_type") if dictionary.get("nodegroup_type") else APIHelper.SKIP
        enable_asg_access = dictionary.get("enable_asg_access") if "enable_asg_access" in dictionary.keys() else APIHelper.SKIP
        enable_full_access_to_ecr = dictionary.get("enable_full_access_to_ecr") if "enable_full_access_to_ecr" in dictionary.keys() else APIHelper.SKIP
        version_info_id = dictionary.get("version_info_id") if dictionary.get("version_info_id") else APIHelper.SKIP
        upgrade_info_id = dictionary.get("upgrade_info_id") if dictionary.get("upgrade_info_id") else APIHelper.SKIP
        tags = NodeGroupItemTag.from_dictionary(dictionary.get('tags')) if 'tags' in dictionary.keys() else APIHelper.SKIP
        config_file_content = dictionary.get("config_file_content") if dictionary.get("config_file_content") else APIHelper.SKIP
        provision = Provision.from_dictionary(dictionary.get('provision')) if 'provision' in dictionary.keys() else APIHelper.SKIP
        version_info = VersionInfo.from_dictionary(dictionary.get('version_info')) if 'version_info' in dictionary.keys() else APIHelper.SKIP
        upgrade_info = UpgradeInfo.from_dictionary(dictionary.get('upgrade_info')) if 'upgrade_info' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   created_at,
                   modified_at,
                   organization_id,
                   partner_id,
                   instance_type,
                   edge_id,
                   id,
                   provision_id,
                   node_type,
                   nodes,
                   nodes_min,
                   nodes_max,
                   node_volume_size,
                   node_volume_type,
                   node_private_networking,
                   node_zones,
                   node_ami_family,
                   node_labels,
                   nodegroup_type,
                   enable_asg_access,
                   enable_full_access_to_ecr,
                   version_info_id,
                   upgrade_info_id,
                   tags,
                   config_file_content,
                   provision,
                   version_info,
                   upgrade_info)