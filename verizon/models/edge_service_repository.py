# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.credential import Credential
from verizon.models.revision import Revision
from verizon.models.vendor_information import VendorInformation


class EdgeServiceRepository(object):

    """Implementation of the 'EdgeServiceRepository' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        description (string): TODO: type description here.
        revision (Revision): TODO: type description here.
        vendor_information (VendorInformation): TODO: type description here.
        mtype (RepositoryResTypeEnum): TODO: type description here.
        tag (string): TODO: type description here.
        endpoint (string): TODO: type description here.
        reacheability (ReacheabilityEnum): TODO: type description here.
        ca_certificate (string): Required if your repository uses a private
            certificate authencation.Please provide ur CA certificat in PEM
            format.
        agents (list of string): TODO: type description here.
        ssl_disabled (bool): TODO: type description here.
        credentials_type (CredentialsTypeEnum): TODO: type description here.
        credentials (Credential): TODO: type description here.
        ssh_key (string): SSH Private Key in PEM format.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "mtype": 'type',
        "endpoint": 'endpoint',
        "reacheability": 'reacheability',
        "description": 'description',
        "revision": 'revision',
        "vendor_information": 'vendorInformation',
        "tag": 'tag',
        "ca_certificate": 'CACertificate',
        "agents": 'Agents',
        "ssl_disabled": 'sslDisabled',
        "credentials_type": 'credentialsType',
        "credentials": 'credentials',
        "ssh_key": 'sshKey'
    }

    _optionals = [
        'description',
        'revision',
        'vendor_information',
        'tag',
        'ca_certificate',
        'agents',
        'ssl_disabled',
        'credentials_type',
        'credentials',
        'ssh_key',
    ]

    def __init__(self,
                 name=None,
                 mtype=None,
                 endpoint=None,
                 reacheability=None,
                 description=APIHelper.SKIP,
                 revision=APIHelper.SKIP,
                 vendor_information=APIHelper.SKIP,
                 tag=APIHelper.SKIP,
                 ca_certificate=APIHelper.SKIP,
                 agents=APIHelper.SKIP,
                 ssl_disabled=APIHelper.SKIP,
                 credentials_type=APIHelper.SKIP,
                 credentials=APIHelper.SKIP,
                 ssh_key=APIHelper.SKIP):
        """Constructor for the EdgeServiceRepository class"""

        # Initialize members of the class
        self.name = name 
        if description is not APIHelper.SKIP:
            self.description = description 
        if revision is not APIHelper.SKIP:
            self.revision = revision 
        if vendor_information is not APIHelper.SKIP:
            self.vendor_information = vendor_information 
        self.mtype = mtype 
        if tag is not APIHelper.SKIP:
            self.tag = tag 
        self.endpoint = endpoint 
        self.reacheability = reacheability 
        if ca_certificate is not APIHelper.SKIP:
            self.ca_certificate = ca_certificate 
        if agents is not APIHelper.SKIP:
            self.agents = agents 
        if ssl_disabled is not APIHelper.SKIP:
            self.ssl_disabled = ssl_disabled 
        if credentials_type is not APIHelper.SKIP:
            self.credentials_type = credentials_type 
        if credentials is not APIHelper.SKIP:
            self.credentials = credentials 
        if ssh_key is not APIHelper.SKIP:
            self.ssh_key = ssh_key 

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
        mtype = dictionary.get("type") if dictionary.get("type") else None
        endpoint = dictionary.get("endpoint") if dictionary.get("endpoint") else None
        reacheability = dictionary.get("reacheability") if dictionary.get("reacheability") else None
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        revision = Revision.from_dictionary(dictionary.get('revision')) if 'revision' in dictionary.keys() else APIHelper.SKIP
        vendor_information = VendorInformation.from_dictionary(dictionary.get('vendorInformation')) if 'vendorInformation' in dictionary.keys() else APIHelper.SKIP
        tag = dictionary.get("tag") if dictionary.get("tag") else APIHelper.SKIP
        ca_certificate = dictionary.get("CACertificate") if dictionary.get("CACertificate") else APIHelper.SKIP
        agents = dictionary.get("Agents") if dictionary.get("Agents") else APIHelper.SKIP
        ssl_disabled = dictionary.get("sslDisabled") if "sslDisabled" in dictionary.keys() else APIHelper.SKIP
        credentials_type = dictionary.get("credentialsType") if dictionary.get("credentialsType") else APIHelper.SKIP
        credentials = Credential.from_dictionary(dictionary.get('credentials')) if 'credentials' in dictionary.keys() else APIHelper.SKIP
        ssh_key = dictionary.get("sshKey") if dictionary.get("sshKey") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   mtype,
                   endpoint,
                   reacheability,
                   description,
                   revision,
                   vendor_information,
                   tag,
                   ca_certificate,
                   agents,
                   ssl_disabled,
                   credentials_type,
                   credentials,
                   ssh_key)