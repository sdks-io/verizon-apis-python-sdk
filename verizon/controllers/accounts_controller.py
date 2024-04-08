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
from verizon.models.account import Account
from verizon.models.account_states_and_services import AccountStatesAndServices
from verizon.models.account_leads_result import AccountLeadsResult
from verizon.exceptions.connectivity_management_result_exception import ConnectivityManagementResultException


class AccountsController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(AccountsController, self).__init__(config)

    def get_account_information(self,
                                aname):
        """Does a GET request to /m2m/v1/accounts/{aname}.

        Returns information about a specified account.

        Args:
            aname (str): Account name.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. The
                account information.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/accounts/{aname}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('aname')
                            .value(aname)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Account.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Error response.', ConnectivityManagementResultException)
        ).execute()

    def list_account_states_and_services(self,
                                         aname):
        """Does a GET request to /m2m/v1/accounts/{aname}/statesandservices.

        Returns a list and details of all custom services and states defined
        for a specified account.

        Args:
            aname (str): Account name.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. The
                account's engagements, services, and states.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/accounts/{aname}/statesandservices')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('aname')
                            .value(aname)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AccountStatesAndServices.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Error response.', ConnectivityManagementResultException)
        ).execute()

    def list_account_leads(self,
                           aname,
                           next=None):
        """Does a GET request to /m2m/v1/leads/{aname}.

        When HTTP status is 202, a URL will be returned in the Location header
        of the form /leads/{aname}?next={token}. This URL can be used to
        request the next set of leads.

        Args:
            aname (str): Account name.
            next (long|int, optional): Continue the previous query from the
                pageUrl in Location Header.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. The list
                of leads associated with the account.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/leads/{aname}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('aname')
                            .value(aname)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('next')
                         .value(next))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AccountLeadsResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Error response.', ConnectivityManagementResultException)
        ).execute()
