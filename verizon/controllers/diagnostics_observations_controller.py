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
from verizon.models.diagnostics_observation_result import DiagnosticsObservationResult
from verizon.exceptions.device_diagnostics_result_exception import DeviceDiagnosticsResultException


class DiagnosticsObservationsController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(DiagnosticsObservationsController, self).__init__(config)

    def start_diagnostics_observation(self,
                                      body):
        """Does a POST request to /devices/attributes/actions/observe.

        This endpoint allows the user to start or change observe diagnostics.

        Args:
            body (ObservationRequest): Request for device observation
                information.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.
                Diagnostics observation result.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEVICE_DIAGNOSTICS)
            .path('/devices/attributes/actions/observe')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('*/*'))
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
            .deserialize_into(DiagnosticsObservationResult.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'Error response.', DeviceDiagnosticsResultException)
        ).execute()

    def stop_diagnostics_observation(self,
                                     transaction_id,
                                     account_name):
        """Does a DELETE request to /devices/attributes/actions/observe.

        This endpoint allows the user to stop or reset observe diagnostics.

        Args:
            transaction_id (str): The ID value associated with the transaction.
            account_name (str): The numeric account name.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.
                Diagnostics observation result.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEVICE_DIAGNOSTICS)
            .path('/devices/attributes/actions/observe')
            .http_method(HttpMethodEnum.DELETE)
            .query_param(Parameter()
                         .key('transactionId')
                         .value(transaction_id))
            .query_param(Parameter()
                         .key('accountName')
                         .value(account_name))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(And(Single('thingspace_oauth'), Single('VZ-M2M-Token')))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DiagnosticsObservationResult.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'Error response.', DeviceDiagnosticsResultException)
        ).execute()
