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
from verizon.models.software_package import SoftwarePackage
from verizon.models.v2_account_device_list import V2AccountDeviceList
from verizon.models.device_software_upgrade import DeviceSoftwareUpgrade
from verizon.models.v2_campaign_history import V2CampaignHistory
from verizon.models.v2_campaign_device import V2CampaignDevice
from verizon.exceptions.fota_v2_result_exception import FotaV2ResultException


class SoftwareManagementReportsV2Controller(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(SoftwareManagementReportsV2Controller, self).__init__(config)

    def list_available_software(self,
                                account,
                                distribution_type=None):
        """Does a GET request to /software/{account}.

        This endpoint allows user to list a certain type of software of an
        account.

        Args:
            account (str): Account identifier.
            distribution_type (str, optional): Filter distributionType to get
                specific type of software. Value is LWM2M, OMD-DM or HTTP.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Return
                array of software.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V2)
            .path('/software/{account}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('distributionType')
                         .value(distribution_type))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SoftwarePackage.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV2ResultException)
        ).execute()

    def list_account_devices(self,
                             account,
                             last_seen_device_id=None,
                             distribution_type=None):
        """Does a GET request to /devices/{account}.

        The device endpoint gets devices information of an account.

        Args:
            account (str): Account identifier.
            last_seen_device_id (str, optional): Last seen device identifier.
            distribution_type (str, optional): Filter distributionType to get
                specific type of devices. Values is LWM2M, OMD-DM or HTTP.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Return
                array of devices.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V2)
            .path('/devices/{account}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('lastSeenDeviceId')
                         .value(last_seen_device_id))
            .query_param(Parameter()
                         .key('distributionType')
                         .value(distribution_type))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(V2AccountDeviceList.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV2ResultException)
        ).execute()

    def get_device_firmware_upgrade_history(self,
                                            account,
                                            device_id):
        """Does a GET request to /reports/{account}/devices/{deviceId}.

        The endpoint allows user to get software upgrade history of a device
        based on device IMEI.

        Args:
            account (str): Account identifier.
            device_id (str): Device IMEI identifier.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Return
                array of upgrades.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V2)
            .path('/reports/{account}/devices/{deviceId}')
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
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DeviceSoftwareUpgrade.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV2ResultException)
        ).execute()

    def get_campaign_history_by_status(self,
                                       account,
                                       campaign_status,
                                       last_seen_campaign_id=None):
        """Does a GET request to /reports/{account}/campaigns.

        The report endpoint allows user to get campaign history of an account
        for specified status.

        Args:
            account (str): Account identifier.
            campaign_status (str): Status of the campaign.
            last_seen_campaign_id (str, optional): Last seen campaign Id.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Return
                list of campaign history.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V2)
            .path('/reports/{account}/campaigns')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('campaignStatus')
                         .value(campaign_status))
            .query_param(Parameter()
                         .key('lastSeenCampaignId')
                         .value(last_seen_campaign_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(V2CampaignHistory.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV2ResultException)
        ).execute()

    def get_campaign_device_status(self,
                                   account,
                                   campaign_id,
                                   last_seen_device_id=None):
        """Does a GET request to /reports/{account}/campaigns/{campaignId}/devices.

        The report endpoint allows user to get the full list of device of a
        campaign.

        Args:
            account (str): Account identifier.
            campaign_id (str): Campaign identifier.
            last_seen_device_id (str, optional): Last seen device identifier.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Return
                list of campaign history.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V2)
            .path('/reports/{account}/campaigns/{campaignId}/devices')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('campaignId')
                            .value(campaign_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('lastSeenDeviceId')
                         .value(last_seen_device_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(V2CampaignDevice.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV2ResultException)
        ).execute()
