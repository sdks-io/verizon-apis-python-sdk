# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from verizon.api_helper import APIHelper
from verizon.configuration import Server
from verizon.http.api_response import ApiResponse
from verizon.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from verizon.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from verizon.models.tag import Tag
from verizon.models.category import Category
from verizon.exceptions.edge_service_onboarding_result_error_exception import EdgeServiceOnboardingResultErrorException


class ServiceMetadataController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(ServiceMetadataController, self).__init__(config)

    def create_service_tag(self,
                           account_name,
                           body,
                           correlation_id=None):
        """Does a POST request to /v1/tag/.

        Create a new Tag within user's organization.

        Args:
            account_name (string): User account name.
            body (list of Tag): TODO: type description here.
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
            .path('/v1/tag/')
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
            .deserialize_into(Tag.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Unauthorized.', EdgeServiceOnboardingResultErrorException)
            .local_error('404', 'Not found.', EdgeServiceOnboardingResultErrorException)
            .local_error('415', 'Unsupported media type.', EdgeServiceOnboardingResultErrorException)
            .local_error('500', 'Internal Server Error.', EdgeServiceOnboardingResultErrorException)
        ).execute()

    def create_service_category(self,
                                account_name,
                                body,
                                correlation_id=None):
        """Does a POST request to /v1/category.

        Create a new category within user's organization.

        Args:
            account_name (string): User account name.
            body (list of Category): TODO: type description here.
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
            .path('/v1/category')
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
            .deserialize_into(Category.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad Request.', EdgeServiceOnboardingResultErrorException)
            .local_error('401', 'Unauthorized.', EdgeServiceOnboardingResultErrorException)
            .local_error('404', 'Not found.', EdgeServiceOnboardingResultErrorException)
            .local_error('500', 'Internal Server Error.', EdgeServiceOnboardingResultErrorException)
        ).execute()
