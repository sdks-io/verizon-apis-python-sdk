# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.repository_credential import RepositoryCredential


class Repository(object):

    """Implementation of the 'Repository' model.

    Users can create a repository to maintain service artifacts. Repository
    would be either a Git or HELM repository.

    Attributes:
        id (string): System generated unique identifier to identify repository
            uniquely.
        name (string): Name of the repository to be created.
        description (string): Description of the repository being created.
        mtype (EdgeServiceRepositoryTypeEnum): Type for the repository which
            can be Git or Helm.
        tag (string): Attribute which can be used to tag a repository.
        endpoint (string): Endpoint URL for the repository from where
            resources needs to be fetched.
        reacheability (RepositoryReacheabilityEnum): Reachability can be of
            two types, Internet and Private Network.
        ca_certificate (string): Required if your repository uses a private
            certificate authencation.Please provide ur CA certificat in PEM
            format.
        agents (list of string): This attribute can be used to specify GITOps
            Agent to fetch details from private repository.
        ssl_disabled (bool): Boolean value to check the SSL certification.
        is_validated (bool): True if CSP is validated using provided
            credential, false otherwise.
        validation_status (string): Status when the repository is validated
            eg: CREDENTIAL_VALIDATION_SUCCESS.
        credentials_type (RepositoryCredentialTypeEnum): Credentials can be of
            two types, UserPassCredentials and SSHCredentials.
        credentials (RepositoryCredential): Credentials of a repository.
        ssh_key (string): SSH Private Key in PEM format.
        last_validated_date (datetime): Time when the repository was
            validated.
        created_date (datetime): Date when the repository was created.
        last_modified_date (datetime): Date when the repository was updated.
        created_by (string): User information by whom the repository was
            created.
        updated_by (string): User information by whom the repository was
            updated.
        is_deleted (bool): When it will be soft deleted, status will be
            changed.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "id": 'id',
        "description": 'description',
        "mtype": 'type',
        "tag": 'tag',
        "endpoint": 'endpoint',
        "reacheability": 'reacheability',
        "ca_certificate": 'CACertificate',
        "agents": 'Agents',
        "ssl_disabled": 'sslDisabled',
        "is_validated": 'isValidated',
        "validation_status": 'validationStatus',
        "credentials_type": 'credentialsType',
        "credentials": 'credentials',
        "ssh_key": 'sshKey',
        "last_validated_date": 'lastValidatedDate',
        "created_date": 'createdDate',
        "last_modified_date": 'lastModifiedDate',
        "created_by": 'createdBy',
        "updated_by": 'updatedBy',
        "is_deleted": 'isDeleted'
    }

    _optionals = [
        'id',
        'description',
        'mtype',
        'tag',
        'endpoint',
        'reacheability',
        'ca_certificate',
        'agents',
        'ssl_disabled',
        'is_validated',
        'validation_status',
        'credentials_type',
        'credentials',
        'ssh_key',
        'last_validated_date',
        'created_date',
        'last_modified_date',
        'created_by',
        'updated_by',
        'is_deleted',
    ]

    _nullables = [
        'agents',
    ]

    def __init__(self,
                 name=None,
                 id=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 tag=APIHelper.SKIP,
                 endpoint=APIHelper.SKIP,
                 reacheability=APIHelper.SKIP,
                 ca_certificate=APIHelper.SKIP,
                 agents=APIHelper.SKIP,
                 ssl_disabled=APIHelper.SKIP,
                 is_validated=APIHelper.SKIP,
                 validation_status=APIHelper.SKIP,
                 credentials_type=APIHelper.SKIP,
                 credentials=APIHelper.SKIP,
                 ssh_key=APIHelper.SKIP,
                 last_validated_date=APIHelper.SKIP,
                 created_date=APIHelper.SKIP,
                 last_modified_date=APIHelper.SKIP,
                 created_by=APIHelper.SKIP,
                 updated_by=APIHelper.SKIP,
                 is_deleted=APIHelper.SKIP):
        """Constructor for the Repository class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        self.name = name 
        if description is not APIHelper.SKIP:
            self.description = description 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if tag is not APIHelper.SKIP:
            self.tag = tag 
        if endpoint is not APIHelper.SKIP:
            self.endpoint = endpoint 
        if reacheability is not APIHelper.SKIP:
            self.reacheability = reacheability 
        if ca_certificate is not APIHelper.SKIP:
            self.ca_certificate = ca_certificate 
        if agents is not APIHelper.SKIP:
            self.agents = agents 
        if ssl_disabled is not APIHelper.SKIP:
            self.ssl_disabled = ssl_disabled 
        if is_validated is not APIHelper.SKIP:
            self.is_validated = is_validated 
        if validation_status is not APIHelper.SKIP:
            self.validation_status = validation_status 
        if credentials_type is not APIHelper.SKIP:
            self.credentials_type = credentials_type 
        if credentials is not APIHelper.SKIP:
            self.credentials = credentials 
        if ssh_key is not APIHelper.SKIP:
            self.ssh_key = ssh_key 
        if last_validated_date is not APIHelper.SKIP:
            self.last_validated_date = APIHelper.RFC3339DateTime(last_validated_date) if last_validated_date else None 
        if created_date is not APIHelper.SKIP:
            self.created_date = APIHelper.RFC3339DateTime(created_date) if created_date else None 
        if last_modified_date is not APIHelper.SKIP:
            self.last_modified_date = APIHelper.RFC3339DateTime(last_modified_date) if last_modified_date else None 
        if created_by is not APIHelper.SKIP:
            self.created_by = created_by 
        if updated_by is not APIHelper.SKIP:
            self.updated_by = updated_by 
        if is_deleted is not APIHelper.SKIP:
            self.is_deleted = is_deleted 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        tag = dictionary.get("tag") if dictionary.get("tag") else APIHelper.SKIP
        endpoint = dictionary.get("endpoint") if dictionary.get("endpoint") else APIHelper.SKIP
        reacheability = dictionary.get("reacheability") if dictionary.get("reacheability") else APIHelper.SKIP
        ca_certificate = dictionary.get("CACertificate") if dictionary.get("CACertificate") else APIHelper.SKIP
        agents = dictionary.get("Agents") if "Agents" in dictionary.keys() else APIHelper.SKIP
        ssl_disabled = dictionary.get("sslDisabled") if "sslDisabled" in dictionary.keys() else APIHelper.SKIP
        is_validated = dictionary.get("isValidated") if "isValidated" in dictionary.keys() else APIHelper.SKIP
        validation_status = dictionary.get("validationStatus") if dictionary.get("validationStatus") else APIHelper.SKIP
        credentials_type = dictionary.get("credentialsType") if dictionary.get("credentialsType") else APIHelper.SKIP
        credentials = RepositoryCredential.from_dictionary(dictionary.get('credentials')) if 'credentials' in dictionary.keys() else APIHelper.SKIP
        ssh_key = dictionary.get("sshKey") if dictionary.get("sshKey") else APIHelper.SKIP
        last_validated_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("lastValidatedDate")).datetime if dictionary.get("lastValidatedDate") else APIHelper.SKIP
        created_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("createdDate")).datetime if dictionary.get("createdDate") else APIHelper.SKIP
        last_modified_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("lastModifiedDate")).datetime if dictionary.get("lastModifiedDate") else APIHelper.SKIP
        created_by = dictionary.get("createdBy") if dictionary.get("createdBy") else APIHelper.SKIP
        updated_by = dictionary.get("updatedBy") if dictionary.get("updatedBy") else APIHelper.SKIP
        is_deleted = dictionary.get("isDeleted") if "isDeleted" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   id,
                   description,
                   mtype,
                   tag,
                   endpoint,
                   reacheability,
                   ca_certificate,
                   agents,
                   ssl_disabled,
                   is_validated,
                   validation_status,
                   credentials_type,
                   credentials,
                   ssh_key,
                   last_validated_date,
                   created_date,
                   last_modified_date,
                   created_by,
                   updated_by,
                   is_deleted)