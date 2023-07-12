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
from verizon.models.device_logging_status import DeviceLoggingStatus
from verizon.models.device_log import DeviceLog
from verizon.exceptions.fota_v2_result_exception import FotaV2ResultException


class ClientLoggingController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(ClientLoggingController, self).__init__(config)

    def list_devices_with_logging_enabled(self,
                                          account):
        """Does a GET request to /logging/{account}/devices.

        Returns an array of all devices in the specified account for which
        logging is enabled.

        Args:
            account (string): Account identifier.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. List
                containing device logging status information.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V2)
            .path('/logging/{account}/devices')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DeviceLoggingStatus.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV2ResultException)
        ).execute()

    def enable_logging_for_devices(self,
                                   account,
                                   body):
        """Does a PUT request to /logging/{account}/devices.

        Each customer may have a maximum of 20 devices enabled for logging.

        Args:
            account (string): Account identifier.
            body (DeviceLoggingRequest): Device logging information.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. List
                containing device logging status information.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V2)
            .path('/logging/{account}/devices')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('*/*'))
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
            .deserialize_into(DeviceLoggingStatus.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV2ResultException)
        ).execute()

    def disable_logging_for_devices(self,
                                    account,
                                    device_ids):
        """Does a DELETE request to /logging/{account}/devices.

        Turn logging off for a list of devices.

        Args:
            account (string): Account identifier.
            device_ids (string): The list of device IDs.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V2)
            .path('/logging/{account}/devices')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('deviceIds')
                         .value(device_ids))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV2ResultException)
        ).execute()

    def enable_device_logging(self,
                              account,
                              device_id):
        """Does a PUT request to /logging/{account}/devices/{deviceId}.

        Enables logging for a specific device.

        Args:
            account (string): Account identifier.
            device_id (string): Device IMEI identifier.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Device
                logging status information.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V2)
            .path('/logging/{account}/devices/{deviceId}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('deviceId')
                            .value(device_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DeviceLoggingStatus.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV2ResultException)
        ).execute()

    def disable_device_logging(self,
                               account,
                               device_id):
        """Does a DELETE request to /logging/{account}/devices/{deviceId}.

        Disables logging for a specific device.

        Args:
            account (string): Account identifier.
            device_id (string): Device IMEI identifier.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V2)
            .path('/logging/{account}/devices/{deviceId}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('deviceId')
                            .value(device_id)
                            .should_encode(True))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV2ResultException)
        ).execute()

    def list_device_logs(self,
                         account,
                         device_id):
        """Does a GET request to /logging/{account}/devices/{deviceId}/logs.

        Gets logs for a specific device.

        Args:
            account (string): Account identifier.
            device_id (string): Device IMEI identifier.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. List of
                device logs.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V2)
            .path('/logging/{account}/devices/{deviceId}/logs')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('deviceId')
                            .value(device_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DeviceLog.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV2ResultException)
        ).execute()