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
from verizon.models.v3_account_device_list import V3AccountDeviceList
from verizon.models.device_list_result import DeviceListResult
from verizon.exceptions.fota_v3_result_exception import FotaV3ResultException


class AccountDevicesController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(AccountDevicesController, self).__init__(config)

    def get_account_device_information(self,
                                       acc,
                                       last_seen_device_id=None,
                                       protocol='LWM2M'):
        """Does a GET request to /devices/{acc}.

        Retrieve account device information such as reported firmware on the
        devices.

        Args:
            acc (string): Account identifier.
            last_seen_device_id (string, optional): Last seen device
                identifier.
            protocol (DevicesProtocolEnum, optional): Filter to retrieve a
                specific protocol type used.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Returns
                an array of devices.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V3)
            .path('/devices/{acc}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('acc')
                            .value(acc)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('lastSeenDeviceId')
                         .value(last_seen_device_id))
            .query_param(Parameter()
                         .key('protocol')
                         .value(protocol))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(V3AccountDeviceList.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV3ResultException)
        ).execute()

    def list_account_devices_information(self,
                                         acc,
                                         body):
        """Does a POST request to /devices/{acc}.

        Retrieve device information for a list of devices on an account.

        Args:
            acc (string): Account identifier.
            body (DeviceIMEI): Request device list information.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Get
                device list information.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V3)
            .path('/devices/{acc}')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('acc')
                            .value(acc)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DeviceListResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV3ResultException)
        ).execute()
