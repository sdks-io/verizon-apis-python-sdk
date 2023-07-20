# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from verizon.api_helper import APIHelper
from verizon.configuration import Server
from verizon.http.api_response import ApiResponse
from verizon.utilities.file_wrapper import FileWrapper
from verizon.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from verizon.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from verizon.models.services import Services
from verizon.models.service import Service
from verizon.models.service_file import ServiceFile
from verizon.models.service_management_result import ServiceManagementResult
from verizon.models.edge_service_onboarding_delete_result import EdgeServiceOnboardingDeleteResult
from verizon.models.current_status import CurrentStatus
from verizon.exceptions.edge_service_onboarding_result_error_exception import EdgeServiceOnboardingResultErrorException


class ServiceOnboardingController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(ServiceOnboardingController, self).__init__(config)

    def list_services(self,
                      account_name,
                      correlation_id=None,
                      name=None,
                      q=None,
                      limit=None,
                      off_set=None,
                      sort_key='createdDate',
                      sort_dir=None,
                      details_flag=True):
        """Does a GET request to /v1/services.

        Fetch all organizational services in the platform.

        Args:
            account_name (string): User account name.
            correlation_id (string, optional): TODO: type description here.
            name (string, optional): Name of the service whose information
                needs to be fetched.
            q (string, optional): Use the comma (:) character to separate
                multiple values eg
                type=myService:workloads.packageType=Helm,YAML:state=DRAFTED,VA
                LIDATION_COMPLETED.
            limit (long|int, optional): Number of items to return.
            off_set (long|int, optional): Id of the last respose value in the
                previous list.
            sort_key (string, optional): Sorts the response by an attribute.
                Default is createdDate.
            sort_dir (SortDirectionEnum, optional): Sorts the response. Use
                asc for ascending or desc for descending order. The default is
                desc.
            details_flag (bool, optional): Default as true. If it is true,
                then it will return all details.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. OK.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SERVICES)
            .path('/v1/services')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .header_param(Parameter()
                          .key('correlationId')
                          .value(correlation_id))
            .query_param(Parameter()
                         .key('name')
                         .value(name))
            .query_param(Parameter()
                         .key('q')
                         .value(q))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('offSet')
                         .value(off_set))
            .query_param(Parameter()
                         .key('sortKey')
                         .value(sort_key))
            .query_param(Parameter()
                         .key('sortDir')
                         .value(sort_dir))
            .query_param(Parameter()
                         .key('detailsFlag')
                         .value(details_flag))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Services.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad Request.', EdgeServiceOnboardingResultErrorException)
            .local_error('401', 'Unauthorized.', EdgeServiceOnboardingResultErrorException)
            .local_error('404', 'Not Found.', EdgeServiceOnboardingResultErrorException)
            .local_error('500', 'Internal Server Error.', EdgeServiceOnboardingResultErrorException)
        ).execute()

    def register_service(self,
                         account_name,
                         body,
                         correlation_id=None):
        """Does a POST request to /v1/services.

        Create a new service within user's organization.

        Args:
            account_name (string): User account name.
            body (Service): TODO: type description here.
            correlation_id (string, optional): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Created.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SERVICES)
            .path('/v1/services')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('correlationId')
                          .value(correlation_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Service.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad Request.', EdgeServiceOnboardingResultErrorException)
            .local_error('401', 'Unauthorized.', EdgeServiceOnboardingResultErrorException)
            .local_error('403', 'Forbidden.', EdgeServiceOnboardingResultErrorException)
            .local_error('404', 'Not found.', EdgeServiceOnboardingResultErrorException)
            .local_error('415', 'Unsupported media type.', EdgeServiceOnboardingResultErrorException)
            .local_error('429', 'Too many requests.', EdgeServiceOnboardingResultErrorException)
            .local_error('500', 'Internal Server Error.', EdgeServiceOnboardingResultErrorException)
        ).execute()

    def upload_service_workload_file(self,
                                     account_name,
                                     service_name,
                                     version,
                                     category_type,
                                     category_name,
                                     payload,
                                     correlation_id=None,
                                     category_version=None):
        """Does a POST request to /v1/files/{serviceName}/{version}/uploadAndValidate.

        Upload workload payload/package in the MEC platform.

        Args:
            account_name (string): User account name.
            service_name (string): Service name to which the file is going to
                be associated.
            version (string): Version of the service being used.
            category_type (CategoryTypeEnum): Type of the file being
                uploaded.
            category_name (string): `workloadName` used in the service while
                creation.
            payload (typing.BinaryIO): Payload/file which is to be uploaded
                should be provided in formData.
            correlation_id (string, optional): TODO: type description here.
            category_version (string, optional): It is mandatory for only
                service file, not mandatory for workload and workflow file.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Upload
                success.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SERVICES)
            .path('/v1/files/{serviceName}/{version}/uploadAndValidate')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .template_param(Parameter()
                            .key('serviceName')
                            .value(service_name)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('version')
                            .value(version)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('categoryType')
                         .value(category_type))
            .query_param(Parameter()
                         .key('categoryName')
                         .value(category_name))
            .multipart_param(Parameter()
                             .key('payload')
                             .value(payload)
                             .default_content_type('application/octet-stream'))
            .header_param(Parameter()
                          .key('correlationId')
                          .value(correlation_id))
            .query_param(Parameter()
                         .key('categoryVersion')
                         .value(category_version))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServiceFile.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad Request.', EdgeServiceOnboardingResultErrorException)
            .local_error('401', 'Unauthorized.', EdgeServiceOnboardingResultErrorException)
            .local_error('404', 'Not found.', EdgeServiceOnboardingResultErrorException)
            .local_error('500', 'Internal Server Error.', EdgeServiceOnboardingResultErrorException)
        ).execute()

    def list_service_details(self,
                             account_name,
                             service_name,
                             version,
                             correlation_id=None):
        """Does a GET request to /v1/services/{serviceName}/{version}.

        Fetch a service details within user's organization using service name
        and version.

        Args:
            account_name (string): User account name.
            service_name (string): Name of the service whose information needs
                to be fetched.
            version (string): Version of service whose information needs to be
                fetched.
            correlation_id (string, optional): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. OK.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SERVICES)
            .path('/v1/services/{serviceName}/{version}')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .template_param(Parameter()
                            .key('serviceName')
                            .value(service_name)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('version')
                            .value(version)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('correlationId')
                          .value(correlation_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Service.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad Request.', EdgeServiceOnboardingResultErrorException)
            .local_error('401', 'Unauthorized.', EdgeServiceOnboardingResultErrorException)
            .local_error('404', 'Not Found.', EdgeServiceOnboardingResultErrorException)
            .local_error('500', 'Internal Server Error.', EdgeServiceOnboardingResultErrorException)
            .local_error('default', 'Unexpected error.', EdgeServiceOnboardingResultErrorException)
        ).execute()

    def start_service_claim_sand_box_testing(self,
                                             account_name,
                                             service_id,
                                             claim_id,
                                             body,
                                             correlation_id=None):
        """Does a PUT request to /v1/services/{serviceId}/claims/{claimId}/sandBoxStart.

        Initiate testing of a service in sandbox environment per claim based
        on service's compatibility(s).

        Args:
            account_name (string): User account name.
            service_id (string): An id of the service created e.g. UUID.
            claim_id (string): Id of the claim created e.g. UUID.
            body (ClusterInfoDetails): TODO: type description here.
            correlation_id (string, optional): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. OK.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SERVICES)
            .path('/v1/services/{serviceId}/claims/{claimId}/sandBoxStart')
            .http_method(HttpMethodEnum.PUT)
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .template_param(Parameter()
                            .key('serviceId')
                            .value(service_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('claimId')
                            .value(claim_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('correlationId')
                          .value(correlation_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServiceManagementResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad Request.', EdgeServiceOnboardingResultErrorException)
            .local_error('401', 'Unauthorized.', EdgeServiceOnboardingResultErrorException)
            .local_error('500', 'Internal Server Error.', EdgeServiceOnboardingResultErrorException)
            .local_error('default', 'Unexpected error.', EdgeServiceOnboardingResultErrorException)
        ).execute()

    def remove_service(self,
                       account_name,
                       service_name,
                       version,
                       correlation_id=None):
        """Does a DELETE request to /v1/services/{serviceName}/{version}.

        Remove a service from user's organization.

        Args:
            account_name (string): User account name.
            service_name (string): Name of the service which is about to be
                deleted.
            version (string): Version of the service which is about to be
                deleted.
            correlation_id (string, optional): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. OK.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SERVICES)
            .path('/v1/services/{serviceName}/{version}')
            .http_method(HttpMethodEnum.DELETE)
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .template_param(Parameter()
                            .key('serviceName')
                            .value(service_name)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('version')
                            .value(version)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('correlationId')
                          .value(correlation_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(EdgeServiceOnboardingDeleteResult.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Unauthorized.', EdgeServiceOnboardingResultErrorException)
            .local_error('404', 'Not found.', EdgeServiceOnboardingResultErrorException)
            .local_error('500', 'Internal Server Error.', EdgeServiceOnboardingResultErrorException)
        ).execute()

    def stop_service_testing(self,
                             account_name,
                             service_name,
                             version,
                             correlation_id=None):
        """Does a PUT request to /v1/services/{serviceName}/{version}/certify.

        Start service certification process. On successful completion of this
        process, service's status will change to certified.

        Args:
            account_name (string): User account name.
            service_name (string): Name of the service e.g. any sub string of
                serviceName.
            version (string): Version of service which is to be certified.
            correlation_id (string, optional): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. OK.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SERVICES)
            .path('/v1/services/{serviceName}/{version}/certify')
            .http_method(HttpMethodEnum.PUT)
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .template_param(Parameter()
                            .key('serviceName')
                            .value(service_name)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('version')
                            .value(version)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('correlationId')
                          .value(correlation_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServiceManagementResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad Request.', EdgeServiceOnboardingResultErrorException)
            .local_error('401', 'Unauthorized.', EdgeServiceOnboardingResultErrorException)
            .local_error('500', 'Internal Server Error.', EdgeServiceOnboardingResultErrorException)
            .local_error('default', 'Unexpected error.', EdgeServiceOnboardingResultErrorException)
        ).execute()

    def mark_service_as_ready_for_public_use(self,
                                             account_name,
                                             service_name,
                                             version,
                                             correlation_id=None):
        """Does a PUT request to /v1/services/{serviceName}/{version}/readyToPublicUse.

        Start the process to change a service's status to "Ready to Use". On
        success, service's status will be changed to "Ready to Use". Only a
        ready to use service can be deployed in production environment.

        Args:
            account_name (string): User account name.
            service_name (string): Name of the service e.g. any sub string of
                serviceName.
            version (string): Version of the service which is already
                certified and is ready for public use.
            correlation_id (string, optional): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. OK.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SERVICES)
            .path('/v1/services/{serviceName}/{version}/readyToPublicUse')
            .http_method(HttpMethodEnum.PUT)
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .template_param(Parameter()
                            .key('serviceName')
                            .value(service_name)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('version')
                            .value(version)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('correlationId')
                          .value(correlation_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServiceManagementResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad Request.', EdgeServiceOnboardingResultErrorException)
            .local_error('401', 'Unauthorized.', EdgeServiceOnboardingResultErrorException)
            .local_error('500', 'Internal Server Error.', EdgeServiceOnboardingResultErrorException)
            .local_error('default', 'Unexpected error.', EdgeServiceOnboardingResultErrorException)
        ).execute()

    def start_service_onboarding(self,
                                 account_name,
                                 service_name,
                                 version,
                                 correlation_id=None):
        """Does a PUT request to /v1/services/{serviceName}/{version}/startOnboarding.

        Start service onboarding process to kick off service artifact
        validation and making the service ready for sandbox testing. On
        successful completion of this process system will generate claims for
        each selected cloud provider using which user can start sandbox
        testing.

        Args:
            account_name (string): User account name.
            service_name (string): Name of the service which is to be
                onboarded.
            version (string): Version of service which is to be onboarded.
            correlation_id (string, optional): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. OK.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SERVICES)
            .path('/v1/services/{serviceName}/{version}/startOnboarding')
            .http_method(HttpMethodEnum.PUT)
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .template_param(Parameter()
                            .key('serviceName')
                            .value(service_name)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('version')
                            .value(version)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('correlationId')
                          .value(correlation_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServiceManagementResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad Request.', EdgeServiceOnboardingResultErrorException)
            .local_error('401', 'Unauthorized.', EdgeServiceOnboardingResultErrorException)
            .local_error('403', 'Forbidden.', EdgeServiceOnboardingResultErrorException)
            .local_error('404', 'Not found.', EdgeServiceOnboardingResultErrorException)
            .local_error('415', 'Unsupported media type.', EdgeServiceOnboardingResultErrorException)
            .local_error('429', 'Too many requests.', EdgeServiceOnboardingResultErrorException)
            .local_error('500', 'Internal Server Error.', EdgeServiceOnboardingResultErrorException)
        ).execute()

    def get_service_job_status(self,
                               account_name,
                               job_id,
                               correlation_id=None):
        """Does a GET request to /v1/services/{jobId}/status.

        Check current status of job for a service using job ID.

        Args:
            account_name (string): User account name.
            job_id (string): Auto-generated Id of the job.
            correlation_id (string, optional): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. OK.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SERVICES)
            .path('/v1/services/{jobId}/status')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .template_param(Parameter()
                            .key('jobId')
                            .value(job_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('correlationId')
                          .value(correlation_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CurrentStatus.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Unauthorized.', EdgeServiceOnboardingResultErrorException)
            .local_error('404', 'Not found.', EdgeServiceOnboardingResultErrorException)
            .local_error('500', 'Internal Server Error.', EdgeServiceOnboardingResultErrorException)
        ).execute()

    def start_service_publishing(self,
                                 account_name,
                                 service_name,
                                 version,
                                 correlation_id=None):
        """Does a PUT request to /v1/services/{serviceName}/{version}/publish.

        Start publishing a service. On successful completion, service's status
        can be marked as Publish.

        Args:
            account_name (string): User account name.
            service_name (string): Name of the service e.g. any sub string of
                serviceName.
            version (string): Version of service which is to be published.
            correlation_id (string, optional): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. OK.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SERVICES)
            .path('/v1/services/{serviceName}/{version}/publish')
            .http_method(HttpMethodEnum.PUT)
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .template_param(Parameter()
                            .key('serviceName')
                            .value(service_name)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('version')
                            .value(version)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('correlationId')
                          .value(correlation_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServiceManagementResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad Request.', EdgeServiceOnboardingResultErrorException)
            .local_error('401', 'Unauthorized.', EdgeServiceOnboardingResultErrorException)
            .local_error('500', 'Internal Server Error.', EdgeServiceOnboardingResultErrorException)
            .local_error('default', 'Unexpected error.', EdgeServiceOnboardingResultErrorException)
        ).execute()
