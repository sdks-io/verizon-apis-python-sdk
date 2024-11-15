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
from verizon.models.get_trigger_response_list import GetTriggerResponseList
from verizon.models.anomaly_detection_trigger import AnomalyDetectionTrigger
from verizon.exceptions.intelligence_result_exception import IntelligenceResultException


class AnomalyTriggersController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(AnomalyTriggersController, self).__init__(config)

    def list_anomaly_detection_triggers(self):
        """Does a GET request to /m2m/v1/triggers.

        This corresponds to the M2M-MC SOAP interface, ```GetTriggers```.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. List of
                triggers associated to a Contact

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/triggers')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(And(Single('thingspace_oauth'), Single('VZ-M2M-Token')))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetTriggerResponseList.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad request', IntelligenceResultException)
            .local_error('401', 'Unauthorized', IntelligenceResultException)
            .local_error('403', 'Forbidden', IntelligenceResultException)
            .local_error('404', 'Not Found / Does not exist', IntelligenceResultException)
            .local_error('406', 'Format / Request Unacceptable', IntelligenceResultException)
            .local_error('429', 'Too many requests', IntelligenceResultException)
            .local_error('default', 'Error response', IntelligenceResultException)
        ).execute()

    def update_anomaly_detection_trigger(self,
                                         body):
        """Does a PUT request to /m2m/v1/triggers.

        This corresponds to the M2M-MC SOAP interface,
        ```UpdateTriggerRequest```.

        Args:
            body (UpdateTriggerRequest): Update Trigger Request

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Trigger ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/triggers')
            .http_method(HttpMethodEnum.PUT)
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
            .deserialize_into(AnomalyDetectionTrigger.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad request', IntelligenceResultException)
            .local_error('401', 'Unauthorized', IntelligenceResultException)
            .local_error('403', 'Forbidden', IntelligenceResultException)
            .local_error('404', 'Not Found / Does not exist', IntelligenceResultException)
            .local_error('406', 'Format / Request Unacceptable', IntelligenceResultException)
            .local_error('429', 'Too many requests', IntelligenceResultException)
            .local_error('default', 'Error response', IntelligenceResultException)
        ).execute()

    def create_anomaly_detection_trigger(self,
                                         body):
        """Does a POST request to /m2m/v1/triggers.

        This corresponds to the M2M-MC SOAP interface, ```CreateTrigger```.

        Args:
            body (CreateTriggerRequest): Create Trigger Request

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Trigger ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/triggers')
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
            .deserialize_into(AnomalyDetectionTrigger.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad request', IntelligenceResultException)
            .local_error('401', 'Unauthorized', IntelligenceResultException)
            .local_error('403', 'Forbidden', IntelligenceResultException)
            .local_error('404', 'Not Found / Does not exist', IntelligenceResultException)
            .local_error('406', 'Format / Request Unacceptable', IntelligenceResultException)
            .local_error('429', 'Too many requests', IntelligenceResultException)
            .local_error('default', 'Error response', IntelligenceResultException)
        ).execute()

    def list_anomaly_detection_trigger_settings(self,
                                                trigger_id):
        """Does a GET request to /m2m/v1/triggers/{triggerId}.

        This corresponds to the M2M-MC SOAP interface, ```GetTriggers```.

        Args:
            trigger_id (str): trigger ID

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Trigger
                information associated to a Trigger Id

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/triggers/{triggerId}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('triggerId')
                            .value(trigger_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(And(Single('thingspace_oauth'), Single('VZ-M2M-Token')))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetTriggerResponseList.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad request', IntelligenceResultException)
            .local_error('401', 'Unauthorized', IntelligenceResultException)
            .local_error('403', 'Forbidden', IntelligenceResultException)
            .local_error('404', 'Not Found / Does not exist', IntelligenceResultException)
            .local_error('406', 'Format / Request Unacceptable', IntelligenceResultException)
            .local_error('429', 'Too many requests', IntelligenceResultException)
            .local_error('default', 'Error response', IntelligenceResultException)
        ).execute()

    def delete_anomaly_detection_trigger(self,
                                         trigger_id):
        """Does a DELETE request to /m2m/v1/triggers/{triggerId}.

        Deletes a specific trigger ID

        Args:
            trigger_id (str): The trigger ID to be deleted

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. The ID of
                the deleted trigger is returned

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/triggers/{triggerId}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('triggerId')
                            .value(trigger_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(And(Single('thingspace_oauth'), Single('VZ-M2M-Token')))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AnomalyDetectionTrigger.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'Error response', IntelligenceResultException)
        ).execute()
