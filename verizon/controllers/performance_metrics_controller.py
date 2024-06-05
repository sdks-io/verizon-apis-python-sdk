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
from verizon.models.mec_performance_metrics import MECPerformanceMetrics
from verizon.exceptions.edge_performance_result_exception import EdgePerformanceResultException


class PerformanceMetricsController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(PerformanceMetricsController, self).__init__(config)

    def query_mec_performance_metrics(self,
                                      body=None):
        """Does a POST request to /performance/device/network/metrics.

        Query the most recent data for Key Performance Indicators (KPIs) like
        network availability, MEC hostnames and more.

        Args:
            body (QueryMECPerformanceMetricsRequest, optional): TODO: type
                description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. MEC
                performance metrics.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PERFORMANCE)
            .path('/performance/device/network/metrics')
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
            .deserialize_into(MECPerformanceMetrics.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad Request.', EdgePerformanceResultException)
            .local_error('401', 'Unauthorized request.', EdgePerformanceResultException)
            .local_error('403', 'Request forbidden.', EdgePerformanceResultException)
            .local_error('404', 'Resource Not Found.', EdgePerformanceResultException)
            .local_error('405', 'Method Not Allowed.', EdgePerformanceResultException)
            .local_error('503', 'Service Unavailable.', EdgePerformanceResultException)
        ).execute()
