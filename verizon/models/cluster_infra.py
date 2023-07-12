# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.cluster import Cluster
from verizon.models.cluster_infra_provision import ClusterInfraProvision
from verizon.models.cluster_provider_params import ClusterProviderParams
from verizon.models.cluster_version_info import ClusterVersionInfo
from verizon.models.metro import Metro
from verizon.models.node import Node
from verizon.models.node_group_item import NodeGroupItem
from verizon.models.project_item import ProjectItem
from verizon.models.storage_class_map import StorageClassMap


class ClusterInfra(object):

    """Implementation of the 'ClusterInfra' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        created_at (string): TODO: type description here.
        modified_at (string): TODO: type description here.
        organization_id (string): TODO: type description here.
        partner_id (string): TODO: type description here.
        country (string): TODO: type description here.
        city (string): TODO: type description here.
        latitude (string): TODO: type description here.
        longitude (string): TODO: type description here.
        cluster_id (string): TODO: type description here.
        status (string): TODO: type description here.
        cert (string): TODO: type description here.
        passphrase (string): TODO: type description here.
        id (string): TODO: type description here.
        cname (string): TODO: type description here.
        arecord (string): TODO: type description here.
        base_ratio (float): TODO: type description here.
        ha_enabled (bool): TODO: type description here.
        display_name (string): TODO: type description here.
        upgrade_status (string): TODO: type description here.
        provider_id (string): TODO: type description here.
        auto_create (bool): TODO: type description here.
        auto_approve_nodes (bool): TODO: type description here.
        provision_id (string): TODO: type description here.
        is_monitor_enabled (bool): TODO: type description here.
        health (int): TODO: type description here.
        health_status_modified_at (string): TODO: type description here.
        manufacturer (string): TODO: type description here.
        cluster_type (string): TODO: type description here.
        cluster_blueprint (string): TODO: type description here.
        gimage_used (string): TODO: type description here.
        reason (string): TODO: type description here.
        is_master_dedicated (bool): TODO: type description here.
        project_id (string): TODO: type description here.
        provision_os (string): TODO: type description here.
        default_storage_class (string): TODO: type description here.
        storage_class_map (StorageClassMap): TODO: type description here.
        cni_provider (string): TODO: type description here.
        provision_k_8_s (string): TODO: type description here.
        etcd_version (string): TODO: type description here.
        consul_version (string): TODO: type description here.
        cluster_blueprint_version (string): TODO: type description here.
        upgrade_protection (bool): TODO: type description here.
        provision (ClusterInfraProvision): TODO: type description here.
        metro (Metro): TODO: type description here.
        nodes (list of Node): TODO: type description here.
        cluster_provider_params (ClusterProviderParams): TODO: type
            description here.
        nodegroups (list of NodeGroupItem): TODO: type description here.
        cluster_version_info (ClusterVersionInfo): TODO: type description
            here.
        projects (list of ProjectItem): TODO: type description here.
        cluster (Cluster): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "created_at": 'created_at',
        "modified_at": 'modified_at',
        "organization_id": 'organization_id',
        "partner_id": 'partner_id',
        "country": 'country',
        "city": 'city',
        "latitude": 'latitude',
        "longitude": 'longitude',
        "cluster_id": 'cluster_id',
        "status": 'status',
        "cert": 'cert',
        "passphrase": 'passphrase',
        "id": 'id',
        "cname": 'cname',
        "arecord": 'arecord',
        "base_ratio": 'base_ratio',
        "ha_enabled": 'ha_enabled',
        "display_name": 'display_name',
        "upgrade_status": 'upgradeStatus',
        "provider_id": 'provider_id',
        "auto_create": 'auto_create',
        "auto_approve_nodes": 'auto_approve_nodes',
        "provision_id": 'provision_id',
        "is_monitor_enabled": 'is_monitor_enabled',
        "health": 'health',
        "health_status_modified_at": 'health_status_modified_at',
        "manufacturer": 'manufacturer',
        "cluster_type": 'cluster_type',
        "cluster_blueprint": 'cluster_blueprint',
        "gimage_used": 'gimage_used',
        "reason": 'reason',
        "is_master_dedicated": 'is_master_dedicated',
        "project_id": 'project_id',
        "provision_os": 'provision_os',
        "default_storage_class": 'default_storage_class',
        "storage_class_map": 'storage_class_map',
        "cni_provider": 'cni_provider',
        "provision_k_8_s": 'provision_k8s',
        "etcd_version": 'etcd_version',
        "consul_version": 'consul_version',
        "cluster_blueprint_version": 'cluster_blueprint_version',
        "upgrade_protection": 'upgrade_protection',
        "provision": 'provision',
        "metro": 'Metro',
        "nodes": 'nodes',
        "cluster_provider_params": 'cluster_provider_params',
        "nodegroups": 'nodegroups',
        "cluster_version_info": 'cluster_version_info',
        "projects": 'projects',
        "cluster": 'cluster'
    }

    _optionals = [
        'name',
        'created_at',
        'modified_at',
        'organization_id',
        'partner_id',
        'country',
        'city',
        'latitude',
        'longitude',
        'cluster_id',
        'status',
        'cert',
        'passphrase',
        'id',
        'cname',
        'arecord',
        'base_ratio',
        'ha_enabled',
        'display_name',
        'upgrade_status',
        'provider_id',
        'auto_create',
        'auto_approve_nodes',
        'provision_id',
        'is_monitor_enabled',
        'health',
        'health_status_modified_at',
        'manufacturer',
        'cluster_type',
        'cluster_blueprint',
        'gimage_used',
        'reason',
        'is_master_dedicated',
        'project_id',
        'provision_os',
        'default_storage_class',
        'storage_class_map',
        'cni_provider',
        'provision_k_8_s',
        'etcd_version',
        'consul_version',
        'cluster_blueprint_version',
        'upgrade_protection',
        'provision',
        'metro',
        'nodes',
        'cluster_provider_params',
        'nodegroups',
        'cluster_version_info',
        'projects',
        'cluster',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 modified_at=APIHelper.SKIP,
                 organization_id=APIHelper.SKIP,
                 partner_id=APIHelper.SKIP,
                 country=APIHelper.SKIP,
                 city=APIHelper.SKIP,
                 latitude=APIHelper.SKIP,
                 longitude=APIHelper.SKIP,
                 cluster_id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 cert=APIHelper.SKIP,
                 passphrase=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 cname=APIHelper.SKIP,
                 arecord=APIHelper.SKIP,
                 base_ratio=APIHelper.SKIP,
                 ha_enabled=APIHelper.SKIP,
                 display_name=APIHelper.SKIP,
                 upgrade_status=APIHelper.SKIP,
                 provider_id=APIHelper.SKIP,
                 auto_create=APIHelper.SKIP,
                 auto_approve_nodes=APIHelper.SKIP,
                 provision_id=APIHelper.SKIP,
                 is_monitor_enabled=APIHelper.SKIP,
                 health=APIHelper.SKIP,
                 health_status_modified_at=APIHelper.SKIP,
                 manufacturer=APIHelper.SKIP,
                 cluster_type=APIHelper.SKIP,
                 cluster_blueprint=APIHelper.SKIP,
                 gimage_used=APIHelper.SKIP,
                 reason=APIHelper.SKIP,
                 is_master_dedicated=APIHelper.SKIP,
                 project_id=APIHelper.SKIP,
                 provision_os=APIHelper.SKIP,
                 default_storage_class=APIHelper.SKIP,
                 storage_class_map=APIHelper.SKIP,
                 cni_provider=APIHelper.SKIP,
                 provision_k_8_s=APIHelper.SKIP,
                 etcd_version=APIHelper.SKIP,
                 consul_version=APIHelper.SKIP,
                 cluster_blueprint_version=APIHelper.SKIP,
                 upgrade_protection=APIHelper.SKIP,
                 provision=APIHelper.SKIP,
                 metro=APIHelper.SKIP,
                 nodes=APIHelper.SKIP,
                 cluster_provider_params=APIHelper.SKIP,
                 nodegroups=APIHelper.SKIP,
                 cluster_version_info=APIHelper.SKIP,
                 projects=APIHelper.SKIP,
                 cluster=APIHelper.SKIP):
        """Constructor for the ClusterInfra class"""

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
        if country is not APIHelper.SKIP:
            self.country = country 
        if city is not APIHelper.SKIP:
            self.city = city 
        if latitude is not APIHelper.SKIP:
            self.latitude = latitude 
        if longitude is not APIHelper.SKIP:
            self.longitude = longitude 
        if cluster_id is not APIHelper.SKIP:
            self.cluster_id = cluster_id 
        if status is not APIHelper.SKIP:
            self.status = status 
        if cert is not APIHelper.SKIP:
            self.cert = cert 
        if passphrase is not APIHelper.SKIP:
            self.passphrase = passphrase 
        if id is not APIHelper.SKIP:
            self.id = id 
        if cname is not APIHelper.SKIP:
            self.cname = cname 
        if arecord is not APIHelper.SKIP:
            self.arecord = arecord 
        if base_ratio is not APIHelper.SKIP:
            self.base_ratio = base_ratio 
        if ha_enabled is not APIHelper.SKIP:
            self.ha_enabled = ha_enabled 
        if display_name is not APIHelper.SKIP:
            self.display_name = display_name 
        if upgrade_status is not APIHelper.SKIP:
            self.upgrade_status = upgrade_status 
        if provider_id is not APIHelper.SKIP:
            self.provider_id = provider_id 
        if auto_create is not APIHelper.SKIP:
            self.auto_create = auto_create 
        if auto_approve_nodes is not APIHelper.SKIP:
            self.auto_approve_nodes = auto_approve_nodes 
        if provision_id is not APIHelper.SKIP:
            self.provision_id = provision_id 
        if is_monitor_enabled is not APIHelper.SKIP:
            self.is_monitor_enabled = is_monitor_enabled 
        if health is not APIHelper.SKIP:
            self.health = health 
        if health_status_modified_at is not APIHelper.SKIP:
            self.health_status_modified_at = health_status_modified_at 
        if manufacturer is not APIHelper.SKIP:
            self.manufacturer = manufacturer 
        if cluster_type is not APIHelper.SKIP:
            self.cluster_type = cluster_type 
        if cluster_blueprint is not APIHelper.SKIP:
            self.cluster_blueprint = cluster_blueprint 
        if gimage_used is not APIHelper.SKIP:
            self.gimage_used = gimage_used 
        if reason is not APIHelper.SKIP:
            self.reason = reason 
        if is_master_dedicated is not APIHelper.SKIP:
            self.is_master_dedicated = is_master_dedicated 
        if project_id is not APIHelper.SKIP:
            self.project_id = project_id 
        if provision_os is not APIHelper.SKIP:
            self.provision_os = provision_os 
        if default_storage_class is not APIHelper.SKIP:
            self.default_storage_class = default_storage_class 
        if storage_class_map is not APIHelper.SKIP:
            self.storage_class_map = storage_class_map 
        if cni_provider is not APIHelper.SKIP:
            self.cni_provider = cni_provider 
        if provision_k_8_s is not APIHelper.SKIP:
            self.provision_k_8_s = provision_k_8_s 
        if etcd_version is not APIHelper.SKIP:
            self.etcd_version = etcd_version 
        if consul_version is not APIHelper.SKIP:
            self.consul_version = consul_version 
        if cluster_blueprint_version is not APIHelper.SKIP:
            self.cluster_blueprint_version = cluster_blueprint_version 
        if upgrade_protection is not APIHelper.SKIP:
            self.upgrade_protection = upgrade_protection 
        if provision is not APIHelper.SKIP:
            self.provision = provision 
        if metro is not APIHelper.SKIP:
            self.metro = metro 
        if nodes is not APIHelper.SKIP:
            self.nodes = nodes 
        if cluster_provider_params is not APIHelper.SKIP:
            self.cluster_provider_params = cluster_provider_params 
        if nodegroups is not APIHelper.SKIP:
            self.nodegroups = nodegroups 
        if cluster_version_info is not APIHelper.SKIP:
            self.cluster_version_info = cluster_version_info 
        if projects is not APIHelper.SKIP:
            self.projects = projects 
        if cluster is not APIHelper.SKIP:
            self.cluster = cluster 

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
        country = dictionary.get("country") if dictionary.get("country") else APIHelper.SKIP
        city = dictionary.get("city") if dictionary.get("city") else APIHelper.SKIP
        latitude = dictionary.get("latitude") if dictionary.get("latitude") else APIHelper.SKIP
        longitude = dictionary.get("longitude") if dictionary.get("longitude") else APIHelper.SKIP
        cluster_id = dictionary.get("cluster_id") if dictionary.get("cluster_id") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        cert = dictionary.get("cert") if dictionary.get("cert") else APIHelper.SKIP
        passphrase = dictionary.get("passphrase") if dictionary.get("passphrase") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        cname = dictionary.get("cname") if dictionary.get("cname") else APIHelper.SKIP
        arecord = dictionary.get("arecord") if dictionary.get("arecord") else APIHelper.SKIP
        base_ratio = dictionary.get("base_ratio") if dictionary.get("base_ratio") else APIHelper.SKIP
        ha_enabled = dictionary.get("ha_enabled") if "ha_enabled" in dictionary.keys() else APIHelper.SKIP
        display_name = dictionary.get("display_name") if dictionary.get("display_name") else APIHelper.SKIP
        upgrade_status = dictionary.get("upgradeStatus") if dictionary.get("upgradeStatus") else APIHelper.SKIP
        provider_id = dictionary.get("provider_id") if dictionary.get("provider_id") else APIHelper.SKIP
        auto_create = dictionary.get("auto_create") if "auto_create" in dictionary.keys() else APIHelper.SKIP
        auto_approve_nodes = dictionary.get("auto_approve_nodes") if "auto_approve_nodes" in dictionary.keys() else APIHelper.SKIP
        provision_id = dictionary.get("provision_id") if dictionary.get("provision_id") else APIHelper.SKIP
        is_monitor_enabled = dictionary.get("is_monitor_enabled") if "is_monitor_enabled" in dictionary.keys() else APIHelper.SKIP
        health = dictionary.get("health") if dictionary.get("health") else APIHelper.SKIP
        health_status_modified_at = dictionary.get("health_status_modified_at") if dictionary.get("health_status_modified_at") else APIHelper.SKIP
        manufacturer = dictionary.get("manufacturer") if dictionary.get("manufacturer") else APIHelper.SKIP
        cluster_type = dictionary.get("cluster_type") if dictionary.get("cluster_type") else APIHelper.SKIP
        cluster_blueprint = dictionary.get("cluster_blueprint") if dictionary.get("cluster_blueprint") else APIHelper.SKIP
        gimage_used = dictionary.get("gimage_used") if dictionary.get("gimage_used") else APIHelper.SKIP
        reason = dictionary.get("reason") if dictionary.get("reason") else APIHelper.SKIP
        is_master_dedicated = dictionary.get("is_master_dedicated") if "is_master_dedicated" in dictionary.keys() else APIHelper.SKIP
        project_id = dictionary.get("project_id") if dictionary.get("project_id") else APIHelper.SKIP
        provision_os = dictionary.get("provision_os") if dictionary.get("provision_os") else APIHelper.SKIP
        default_storage_class = dictionary.get("default_storage_class") if dictionary.get("default_storage_class") else APIHelper.SKIP
        storage_class_map = StorageClassMap.from_dictionary(dictionary.get('storage_class_map')) if 'storage_class_map' in dictionary.keys() else APIHelper.SKIP
        cni_provider = dictionary.get("cni_provider") if dictionary.get("cni_provider") else APIHelper.SKIP
        provision_k_8_s = dictionary.get("provision_k8s") if dictionary.get("provision_k8s") else APIHelper.SKIP
        etcd_version = dictionary.get("etcd_version") if dictionary.get("etcd_version") else APIHelper.SKIP
        consul_version = dictionary.get("consul_version") if dictionary.get("consul_version") else APIHelper.SKIP
        cluster_blueprint_version = dictionary.get("cluster_blueprint_version") if dictionary.get("cluster_blueprint_version") else APIHelper.SKIP
        upgrade_protection = dictionary.get("upgrade_protection") if "upgrade_protection" in dictionary.keys() else APIHelper.SKIP
        provision = ClusterInfraProvision.from_dictionary(dictionary.get('provision')) if 'provision' in dictionary.keys() else APIHelper.SKIP
        metro = Metro.from_dictionary(dictionary.get('Metro')) if 'Metro' in dictionary.keys() else APIHelper.SKIP
        nodes = None
        if dictionary.get('nodes') is not None:
            nodes = [Node.from_dictionary(x) for x in dictionary.get('nodes')]
        else:
            nodes = APIHelper.SKIP
        cluster_provider_params = ClusterProviderParams.from_dictionary(dictionary.get('cluster_provider_params')) if 'cluster_provider_params' in dictionary.keys() else APIHelper.SKIP
        nodegroups = None
        if dictionary.get('nodegroups') is not None:
            nodegroups = [NodeGroupItem.from_dictionary(x) for x in dictionary.get('nodegroups')]
        else:
            nodegroups = APIHelper.SKIP
        cluster_version_info = ClusterVersionInfo.from_dictionary(dictionary.get('cluster_version_info')) if 'cluster_version_info' in dictionary.keys() else APIHelper.SKIP
        projects = None
        if dictionary.get('projects') is not None:
            projects = [ProjectItem.from_dictionary(x) for x in dictionary.get('projects')]
        else:
            projects = APIHelper.SKIP
        cluster = Cluster.from_dictionary(dictionary.get('cluster')) if 'cluster' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   created_at,
                   modified_at,
                   organization_id,
                   partner_id,
                   country,
                   city,
                   latitude,
                   longitude,
                   cluster_id,
                   status,
                   cert,
                   passphrase,
                   id,
                   cname,
                   arecord,
                   base_ratio,
                   ha_enabled,
                   display_name,
                   upgrade_status,
                   provider_id,
                   auto_create,
                   auto_approve_nodes,
                   provision_id,
                   is_monitor_enabled,
                   health,
                   health_status_modified_at,
                   manufacturer,
                   cluster_type,
                   cluster_blueprint,
                   gimage_used,
                   reason,
                   is_master_dedicated,
                   project_id,
                   provision_os,
                   default_storage_class,
                   storage_class_map,
                   cni_provider,
                   provision_k_8_s,
                   etcd_version,
                   consul_version,
                   cluster_blueprint_version,
                   upgrade_protection,
                   provision,
                   metro,
                   nodes,
                   cluster_provider_params,
                   nodegroups,
                   cluster_version_info,
                   projects,
                   cluster)
