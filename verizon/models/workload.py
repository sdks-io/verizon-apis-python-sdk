# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.repository import Repository
from verizon.models.service_onboarding_helm_git_branch import ServiceOnboardingHelmGitBranch
from verizon.models.service_onboarding_helm_git_tag import ServiceOnboardingHelmGitTag
from verizon.models.service_onboarding_helm_helmrepo import ServiceOnboardingHelmHelmrepo
from verizon.models.service_onboarding_helm_yaml_git_tag import ServiceOnboardingHelmYamlGitTag
from verizon.models.service_onboarding_terraform_git_branch import ServiceOnboardingTerraformGitBranch
from verizon.models.service_onboarding_terraform_git_tag import ServiceOnboardingTerraformGitTag
from verizon.models.service_onboarding_yaml_git_branch import ServiceOnboardingYamlGitBranch


class Workload(object):

    """Implementation of the 'Workload' model.

    Workload attribute of a service.

    Attributes:
        id (string): The auto-generated Id of the workload.
        name (string): Name of the workload needs to be deployed.
        description (string): A brief workload description.
        package_type (ServiceDependencyPackageTypeEnum): Deployment package
            type.
        upload_type (UploadTypeEnum): Allowed values are: GIT files
            (PULL_FROM_REPO), MANUAL_UPLOAD.
        repository_type (WorkloadRepositoryTypeEnum): Repository types
            allowed: GIT/HELM.
        repository_id (string): In case of 'Pull files from my repository',
            The user can provide the existing repositoryID.
        repository (Repository): Users can create a repository to maintain
            service artifacts. Repository would be either a Git or HELM
            repository.
        files (list of string): Files which are being generated.
        revision_type (WorkloadRevisionTypeEnum): Revision type can be a
            BRANCH or TAG.
        helm_git_branch (ServiceOnboardingHelmGitBranch): TODO: type
            description here.
        helm_git_tag (ServiceOnboardingHelmGitTag): TODO: type description
            here.
        helm_yaml_git_tag (ServiceOnboardingHelmYamlGitTag): TODO: type
            description here.
        helm_helmrepo (ServiceOnboardingHelmHelmrepo): TODO: type description
            here.
        yaml_git_branch (ServiceOnboardingYamlGitBranch): TODO: type
            description here.
        terraform_git_branch (ServiceOnboardingTerraformGitBranch): TODO: type
            description here.
        terraform_git_tag (ServiceOnboardingTerraformGitTag): TODO: type
            description here.
        created_date (datetime): The date on which the workload is created.
        last_modified_dte (datetime): The date when the created workload was
            last modified.
        created_by (string): Identity of the user who created the workload.
        updated_by (string): Identity of the user who updated the workload.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "id": 'id',
        "description": 'description',
        "package_type": 'packageType',
        "upload_type": 'uploadType',
        "repository_type": 'repositoryType',
        "repository_id": 'repositoryId',
        "repository": 'repository',
        "files": 'files',
        "revision_type": 'revisionType',
        "helm_git_branch": 'helmGitBranch',
        "helm_git_tag": 'helmGitTag',
        "helm_yaml_git_tag": 'helmYamlGitTag',
        "helm_helmrepo": 'helmHelmrepo',
        "yaml_git_branch": 'yamlGitBranch',
        "terraform_git_branch": 'terraformGitBranch',
        "terraform_git_tag": 'terraformGitTag',
        "created_date": 'createdDate',
        "last_modified_dte": 'lastModifiedDte',
        "created_by": 'createdBy',
        "updated_by": 'updatedBy'
    }

    _optionals = [
        'id',
        'description',
        'package_type',
        'upload_type',
        'repository_type',
        'repository_id',
        'repository',
        'files',
        'revision_type',
        'helm_git_branch',
        'helm_git_tag',
        'helm_yaml_git_tag',
        'helm_helmrepo',
        'yaml_git_branch',
        'terraform_git_branch',
        'terraform_git_tag',
        'created_date',
        'last_modified_dte',
        'created_by',
        'updated_by',
    ]

    _nullables = [
        'description',
        'package_type',
        'repository_type',
        'repository_id',
        'files',
    ]

    def __init__(self,
                 name=None,
                 id=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 package_type=APIHelper.SKIP,
                 upload_type=APIHelper.SKIP,
                 repository_type=APIHelper.SKIP,
                 repository_id=APIHelper.SKIP,
                 repository=APIHelper.SKIP,
                 files=APIHelper.SKIP,
                 revision_type=APIHelper.SKIP,
                 helm_git_branch=APIHelper.SKIP,
                 helm_git_tag=APIHelper.SKIP,
                 helm_yaml_git_tag=APIHelper.SKIP,
                 helm_helmrepo=APIHelper.SKIP,
                 yaml_git_branch=APIHelper.SKIP,
                 terraform_git_branch=APIHelper.SKIP,
                 terraform_git_tag=APIHelper.SKIP,
                 created_date=APIHelper.SKIP,
                 last_modified_dte=APIHelper.SKIP,
                 created_by=APIHelper.SKIP,
                 updated_by=APIHelper.SKIP):
        """Constructor for the Workload class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        self.name = name 
        if description is not APIHelper.SKIP:
            self.description = description 
        if package_type is not APIHelper.SKIP:
            self.package_type = package_type 
        if upload_type is not APIHelper.SKIP:
            self.upload_type = upload_type 
        if repository_type is not APIHelper.SKIP:
            self.repository_type = repository_type 
        if repository_id is not APIHelper.SKIP:
            self.repository_id = repository_id 
        if repository is not APIHelper.SKIP:
            self.repository = repository 
        if files is not APIHelper.SKIP:
            self.files = files 
        if revision_type is not APIHelper.SKIP:
            self.revision_type = revision_type 
        if helm_git_branch is not APIHelper.SKIP:
            self.helm_git_branch = helm_git_branch 
        if helm_git_tag is not APIHelper.SKIP:
            self.helm_git_tag = helm_git_tag 
        if helm_yaml_git_tag is not APIHelper.SKIP:
            self.helm_yaml_git_tag = helm_yaml_git_tag 
        if helm_helmrepo is not APIHelper.SKIP:
            self.helm_helmrepo = helm_helmrepo 
        if yaml_git_branch is not APIHelper.SKIP:
            self.yaml_git_branch = yaml_git_branch 
        if terraform_git_branch is not APIHelper.SKIP:
            self.terraform_git_branch = terraform_git_branch 
        if terraform_git_tag is not APIHelper.SKIP:
            self.terraform_git_tag = terraform_git_tag 
        if created_date is not APIHelper.SKIP:
            self.created_date = APIHelper.RFC3339DateTime(created_date) if created_date else None 
        if last_modified_dte is not APIHelper.SKIP:
            self.last_modified_dte = APIHelper.RFC3339DateTime(last_modified_dte) if last_modified_dte else None 
        if created_by is not APIHelper.SKIP:
            self.created_by = created_by 
        if updated_by is not APIHelper.SKIP:
            self.updated_by = updated_by 

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
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        package_type = dictionary.get("packageType") if "packageType" in dictionary.keys() else APIHelper.SKIP
        upload_type = dictionary.get("uploadType") if dictionary.get("uploadType") else APIHelper.SKIP
        repository_type = dictionary.get("repositoryType") if "repositoryType" in dictionary.keys() else APIHelper.SKIP
        repository_id = dictionary.get("repositoryId") if "repositoryId" in dictionary.keys() else APIHelper.SKIP
        repository = Repository.from_dictionary(dictionary.get('repository')) if 'repository' in dictionary.keys() else APIHelper.SKIP
        files = dictionary.get("files") if "files" in dictionary.keys() else APIHelper.SKIP
        revision_type = dictionary.get("revisionType") if dictionary.get("revisionType") else APIHelper.SKIP
        helm_git_branch = ServiceOnboardingHelmGitBranch.from_dictionary(dictionary.get('helmGitBranch')) if 'helmGitBranch' in dictionary.keys() else APIHelper.SKIP
        helm_git_tag = ServiceOnboardingHelmGitTag.from_dictionary(dictionary.get('helmGitTag')) if 'helmGitTag' in dictionary.keys() else APIHelper.SKIP
        helm_yaml_git_tag = ServiceOnboardingHelmYamlGitTag.from_dictionary(dictionary.get('helmYamlGitTag')) if 'helmYamlGitTag' in dictionary.keys() else APIHelper.SKIP
        helm_helmrepo = ServiceOnboardingHelmHelmrepo.from_dictionary(dictionary.get('helmHelmrepo')) if 'helmHelmrepo' in dictionary.keys() else APIHelper.SKIP
        yaml_git_branch = ServiceOnboardingYamlGitBranch.from_dictionary(dictionary.get('yamlGitBranch')) if 'yamlGitBranch' in dictionary.keys() else APIHelper.SKIP
        terraform_git_branch = ServiceOnboardingTerraformGitBranch.from_dictionary(dictionary.get('terraformGitBranch')) if 'terraformGitBranch' in dictionary.keys() else APIHelper.SKIP
        terraform_git_tag = ServiceOnboardingTerraformGitTag.from_dictionary(dictionary.get('terraformGitTag')) if 'terraformGitTag' in dictionary.keys() else APIHelper.SKIP
        created_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("createdDate")).datetime if dictionary.get("createdDate") else APIHelper.SKIP
        last_modified_dte = APIHelper.RFC3339DateTime.from_value(dictionary.get("lastModifiedDte")).datetime if dictionary.get("lastModifiedDte") else APIHelper.SKIP
        created_by = dictionary.get("createdBy") if dictionary.get("createdBy") else APIHelper.SKIP
        updated_by = dictionary.get("updatedBy") if dictionary.get("updatedBy") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   id,
                   description,
                   package_type,
                   upload_type,
                   repository_type,
                   repository_id,
                   repository,
                   files,
                   revision_type,
                   helm_git_branch,
                   helm_git_tag,
                   helm_yaml_git_tag,
                   helm_helmrepo,
                   yaml_git_branch,
                   terraform_git_branch,
                   terraform_git_tag,
                   created_date,
                   last_modified_dte,
                   created_by,
                   updated_by)
