# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from enum import Enum
from apimatic_core.http.configurations.http_client_configuration import HttpClientConfiguration
from apimatic_requests_client_adapter.requests_client import RequestsClient


class Environment(Enum):
    """An enum for SDK environments"""
    PRODUCTION = 0
    MOCK_SERVER_FOR_LIMITED_AVAILABILITY_SEE_QUICK_START = 1


class Server(Enum):
    """An enum for API servers"""
    EDGE_DISCOVERY = 0
    THINGSPACE = 1
    OAUTH_SERVER = 2
    M2M = 3
    DEVICE_LOCATION = 4
    SUBSCRIPTION_SERVER = 5
    SOFTWARE_MANAGEMENT_V1 = 6
    SOFTWARE_MANAGEMENT_V2 = 7
    SOFTWARE_MANAGEMENT_V3 = 8
    PERFORMANCE = 9
    DEVICE_DIAGNOSTICS = 10
    CLOUD_CONNECTOR = 11
    HYPER_PRECISE_LOCATION = 12
    SERVICES = 13
    QUALITY_OF_SERVICE = 14


class Configuration(HttpClientConfiguration):
    """A class used for configuring the SDK by a user.
    """

    @property
    def environment(self):
        return self._environment

    @property
    def thingspace_oauth_credentials(self):
        return self._thingspace_oauth_credentials

    @property
    def vz_m2m_token_credentials(self):
        return self._vz_m2m_token_credentials

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=None, retry_methods=None,
                 environment=Environment.PRODUCTION,
                 thingspace_oauth_credentials=None,
                 vz_m2m_token_credentials=None):
        if retry_methods is None:
            retry_methods = ['GET', 'PUT']

        if retry_statuses is None:
            retry_statuses = [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]

        super().__init__(http_client_instance,
                         override_http_client_configuration, http_call_back,
                         timeout, max_retries, backoff_factor, retry_statuses,
                         retry_methods)

        # Current API environment
        self._environment = environment

        # The object holding OAuth 2 Client Credentials Grant credentials
        self._thingspace_oauth_credentials = thingspace_oauth_credentials

        # The object holding Custom Header Signature credentials
        self._vz_m2m_token_credentials = vz_m2m_token_credentials

        # The Http Client to use for making requests.
        self.set_http_client(self.create_http_client())

    def clone_with(self, http_client_instance=None,
                   override_http_client_configuration=None, http_call_back=None,
                   timeout=None, max_retries=None, backoff_factor=None,
                   retry_statuses=None, retry_methods=None, environment=None,
                   thingspace_oauth_credentials=None,
                   vz_m2m_token_credentials=None):
        http_client_instance = http_client_instance or self.http_client_instance
        override_http_client_configuration = override_http_client_configuration or self.override_http_client_configuration
        http_call_back = http_call_back or self.http_callback
        timeout = timeout or self.timeout
        max_retries = max_retries or self.max_retries
        backoff_factor = backoff_factor or self.backoff_factor
        retry_statuses = retry_statuses or self.retry_statuses
        retry_methods = retry_methods or self.retry_methods
        environment = environment or self.environment
        thingspace_oauth_credentials = thingspace_oauth_credentials or self.thingspace_oauth_credentials
        vz_m2m_token_credentials = vz_m2m_token_credentials or self.vz_m2m_token_credentials
        return Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            environment=environment,
            thingspace_oauth_credentials=thingspace_oauth_credentials,
            vz_m2m_token_credentials=vz_m2m_token_credentials
        )

    def create_http_client(self):
        return RequestsClient(
            timeout=self.timeout, max_retries=self.max_retries,
            backoff_factor=self.backoff_factor, retry_statuses=self.retry_statuses,
            retry_methods=self.retry_methods,
            http_client_instance=self.http_client_instance,
            override_http_client_configuration=self.override_http_client_configuration,
            response_factory=self.http_response_factory
        )

    # All the environments the SDK can run in
    environments = {
        Environment.PRODUCTION: {
            Server.EDGE_DISCOVERY: 'https://5gedge.verizon.com/api/mec/eds',
            Server.THINGSPACE: 'https://thingspace.verizon.com/api',
            Server.OAUTH_SERVER: 'https://thingspace.verizon.com/api/ts/v1',
            Server.M2M: 'https://thingspace.verizon.com/api/m2m',
            Server.DEVICE_LOCATION: 'https://thingspace.verizon.com/api/loc/v1',
            Server.SUBSCRIPTION_SERVER: 'https://thingspace.verizon.com/api/subsc/v1',
            Server.SOFTWARE_MANAGEMENT_V1: 'https://thingspace.verizon.com/api/fota/v1',
            Server.SOFTWARE_MANAGEMENT_V2: 'https://thingspace.verizon.com/api/fota/v2',
            Server.SOFTWARE_MANAGEMENT_V3: 'https://thingspace.verizon.com/api/fota/v3',
            Server.PERFORMANCE: 'https://5gedge.verizon.com/api/mec',
            Server.DEVICE_DIAGNOSTICS: 'https://thingspace.verizon.com/api/diagnostics/v1',
            Server.CLOUD_CONNECTOR: 'https://thingspace.verizon.com/api/cc/v1',
            Server.HYPER_PRECISE_LOCATION: 'https://thingspace.verizon.com/api/hyper-precise/v1',
            Server.SERVICES: 'https://5gedge.verizon.com/api/mec/services',
            Server.QUALITY_OF_SERVICE: 'https://thingspace.verizon.com/api/m2m/v1/devices'
        },
        Environment.MOCK_SERVER_FOR_LIMITED_AVAILABILITY_SEE_QUICK_START: {
            Server.EDGE_DISCOVERY: 'https://mock.thingspace.verizon.com/api/mec/eds',
            Server.THINGSPACE: 'https://mock.thingspace.verizon.com/api',
            Server.OAUTH_SERVER: 'https://mock.thingspace.verizon.com/api/ts/v1',
            Server.M2M: 'https://mock.thingspace.verizon.com/api/m2m',
            Server.DEVICE_LOCATION: 'https://mock.thingspace.verizon.com/api/loc/v1',
            Server.SUBSCRIPTION_SERVER: 'https://mock.thingspace.verizon.com/api/subsc/v1',
            Server.SOFTWARE_MANAGEMENT_V1: 'https://mock.thingspace.verizon.com/api/fota/v1',
            Server.SOFTWARE_MANAGEMENT_V2: 'https://mock.thingspace.verizon.com/api/fota/v2',
            Server.SOFTWARE_MANAGEMENT_V3: 'https://mock.thingspace.verizon.com/api/fota/v3',
            Server.PERFORMANCE: 'https://mock.thingspace.verizon.com/api/mec',
            Server.DEVICE_DIAGNOSTICS: 'https://mock.thingspace.verizon.com/api/diagnostics/v1',
            Server.CLOUD_CONNECTOR: 'https://mock.thingspace.verizon.com/api/cc/v1',
            Server.HYPER_PRECISE_LOCATION: 'https://mock.thingspace.verizon.com/api/hyper-precise/v1',
            Server.SERVICES: 'https://mock.thingspace.verizon.com/api/mec/services',
            Server.QUALITY_OF_SERVICE: 'https://mock.thingspace.verizon.com/api/m2m/v1/devices'
        }
    }

    def get_base_uri(self, server=Server.EDGE_DISCOVERY):
        """Generates the appropriate base URI for the environment and the
        server.

        Args:
            server (Configuration.Server): The server enum for which the base
            URI is required.

        Returns:
            String: The base URI.

        """
        return self.environments[self.environment][server]
