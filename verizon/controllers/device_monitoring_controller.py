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
from verizon.models.request_response import RequestResponse
from verizon.exceptions.rest_error_response_exception import RestErrorResponseException


class DeviceMonitoringController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(DeviceMonitoringController, self).__init__(config)

    def device_reachability(self,
                            body):
        """Does a POST request to /m2m/v1/diagnostics/basic/devicereachability.

        TODO: type endpoint description here.

        Args:
            body (NotificationReportRequest): Create Reachability Report
                Request

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Request ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/diagnostics/basic/devicereachability')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(And(Single('thingspace_oauth'), Single('VZ-M2M-Token')))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(RequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Error Response', RestErrorResponseException)
        ).execute()

    def stop_device_reachability(self,
                                 body=None):
        """Does a DELETE request to /m2m/v1/diagnostics/basic/devicereachability.

        TODO: type endpoint description here.

        Args:
            body (StopMonitorRequest, optional): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Request ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/diagnostics/basic/devicereachability')
            .http_method(HttpMethodEnum.DELETE)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(And(Single('thingspace_oauth'), Single('VZ-M2M-Token')))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(RequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Error Response', RestErrorResponseException)
        ).execute()
