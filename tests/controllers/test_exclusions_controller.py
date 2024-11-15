# -*- coding: utf-8 -*-

"""
verizonthingspacequalityofserviceapiendpoints

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from verizonthingspacequalityofserviceapiendpoints.api_helper import APIHelper
from verizonthingspacequalityofserviceapiendpoints.models.account_consent_create import AccountConsentCreate


class ExclusionsControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(ExclusionsControllerTests, cls).setUpClass()
        cls.controller = cls.client.exclusions
        cls.response_catcher = cls.controller.http_call_back

    # Create a consent record to use location services as an asynchronous request.
    def test_devices_location_give_consent_async(self):
        # Parameters for the API call
        body = None

        # Perform the API call through the SDK function
        result = self.controller.devices_location_give_consent_async(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

