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
from verizon.models.wnp_request_response import WNPRequestResponse
from verizon.exceptions.wnp_rest_error_response_exception import WNPRestErrorResponseException


class WirelessNetworkPerformanceController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(WirelessNetworkPerformanceController, self).__init__(config)

    def near_real_time_network_conditions(self,
                                          body):
        """Does a POST request to /m2m/v1/intelligence/network-conditions.

        WNP Query for current network condition.

        Args:
            body (GetNetworkConditionsRequest): Request for current network
                health.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Request
                ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/intelligence/network-conditions')
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
            .deserialize_into(WNPRequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'Error response', WNPRestErrorResponseException)
        ).execute()

    def domestic_4_g_and_5g_nationwide_network_coverage(self,
                                                        body):
        """Does a POST request to /m2m/v1/intelligence/wireless-coverage.

        Run a report to determine network types available and available
        coverage. Network types covered include: CAT-M, NB-IOT, LTE, LTE-AWS
        and 5GNW.

        Args:
            body (GetWirelessCoverageRequest): Request for network coverage
                details.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Request
                ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/intelligence/wireless-coverage')
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
            .deserialize_into(WNPRequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'Error response', WNPRestErrorResponseException)
        ).execute()

    def site_proximity(self,
                       body):
        """Does a POST request to /m2m/v1/intelligence/site-proximity/action/list.

        Identify the direction and general distance of nearby cell sites and
        the technology supported by the equipment.

        Args:
            body (GetNetworkConditionsRequest): Request for cell site
                proximity.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Request
                ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/intelligence/site-proximity/action/list')
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
            .deserialize_into(WNPRequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'Error response', WNPRestErrorResponseException)
        ).execute()

    def device_experience_30_days_history(self,
                                          body):
        """Does a POST request to /m2m/v1/intelligence/device-experience/history/30-days.

        A report of a specific device's service scores over a 30 day period.

        Args:
            body (GetDeviceExperienceScoreHistoryRequest): Request for a
                device's 30 day experience.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Request
                ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/intelligence/device-experience/history/30-days')
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
            .deserialize_into(WNPRequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'Error response', WNPRestErrorResponseException)
        ).execute()

    def device_experience_bulk_latest(self,
                                      body):
        """Does a POST request to /m2m/v1/intelligence/device-experience/bulk/latest.

        Run a report to view the latest device experience score for specific
        devices.

        Args:
            body (GetDeviceExperienceScoreBulkRequest): Request for bulk
                latest history details.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Request
                ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/intelligence/device-experience/bulk/latest')
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
            .deserialize_into(WNPRequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'Error response', WNPRestErrorResponseException)
        ).execute()
