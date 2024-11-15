# -*- coding: utf-8 -*-

"""
verizonthingspacequalityofserviceapiendpoints

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.authentication.header_auth import HeaderAuth
from verizonthingspacequalityofserviceapiendpoints.api_helper import APIHelper
from verizonthingspacequalityofserviceapiendpoints.models.o_auth_token import OAuthToken
from apimatic_core.utilities.auth_helper import AuthHelper
from verizonthingspacequalityofserviceapiendpoints.controllers.o_auth_authorization_controller import\
    OAuthAuthorizationController
from verizonthingspacequalityofserviceapiendpoints.exceptions.api_exception import APIException


class ThingspaceOauth(HeaderAuth):

    @property
    def error_message(self):
        """Display error message on occurrence of authentication failure
        in ThingspaceOauth

        """
        return "ThingspaceOauth: OAuthToken is undefined or expired."

    def __init__(self, thingspace_oauth_credentials, config):
        self._o_auth_client_id = thingspace_oauth_credentials.o_auth_client_id \
            if thingspace_oauth_credentials is not None else None
        self._o_auth_client_secret = thingspace_oauth_credentials.o_auth_client_secret \
            if thingspace_oauth_credentials is not None else None
        if thingspace_oauth_credentials is not None \
                and isinstance(thingspace_oauth_credentials.o_auth_token, OAuthToken):
            self._o_auth_token = OAuthToken.from_dictionary(
                APIHelper.to_dictionary(thingspace_oauth_credentials.o_auth_token))
        else:
            self._o_auth_token = thingspace_oauth_credentials.o_auth_token \
                if thingspace_oauth_credentials is not None else None
        self._o_auth_clock_skew = thingspace_oauth_credentials.o_auth_clock_skew \
            if thingspace_oauth_credentials is not None else None
        self._o_auth_token_provider = thingspace_oauth_credentials.o_auth_token_provider \
            if thingspace_oauth_credentials is not None else None
        self._o_auth_on_token_update = thingspace_oauth_credentials.o_auth_on_token_update \
            if thingspace_oauth_credentials is not None else None
        self._o_auth_api = OAuthAuthorizationController(config)
        super().__init__(auth_params={})

    def is_valid(self):
        self._o_auth_token = self._get_token_from_provider()
        return (self._o_auth_token and isinstance(self._o_auth_token, OAuthToken)
                and not self.is_token_expired(self._o_auth_token))

    def build_basic_auth_header(self):
        """ Builds the basic auth header for endpoints in the
            OAuth Authorization Controller.

        Returns:
            str: The value of the Authentication header.

        """
        return "Basic {}".format(AuthHelper.get_base64_encoded_value(
            self._o_auth_client_id, self._o_auth_client_secret))

    def fetch_token(self, additional_params=None):
        """ Authorizes the client.

            
            additional_params (dict):  Any additional form parameters.

        Returns:
            OAuthToken: The OAuth token.

        """
        token = self._o_auth_api.request_token_thingspace_oauth(
            self.build_basic_auth_header(),
            _optional_form_parameters=additional_params
        )
        if hasattr(token, 'expires_in'):
            current_utc_timestamp = AuthHelper.get_current_utc_timestamp()
            token.expiry = AuthHelper.get_token_expiry(current_utc_timestamp, token.expires_in)
        return token

    def is_token_expired(self, o_auth_token=None):
        """ Checks if OAuth token has expired.

        Args:
            o_auth_token (OAuthToken): The OAuth token whose expiry is to be checked.

        Returns:
            bool: True if OAuth token has expired, False otherwise.

        """
        if o_auth_token is None:
            return (hasattr(self._o_auth_token, 'expiry')
                    and AuthHelper.is_token_expired(self._o_auth_token.expiry, self._o_auth_clock_skew))

        return (hasattr(o_auth_token, 'expiry')
                and AuthHelper.is_token_expired(o_auth_token.expiry, self._o_auth_clock_skew))

    def apply(self, http_request):
        auth_params = {"Authorization": "Bearer {}".format(self._o_auth_token.access_token)}
        AuthHelper.apply(auth_params, http_request.add_header)

    def _get_token_from_provider(self):
        """ This provides the OAuth Token from either the user configured callbacks or from default provider.
        Returns:
            OAuthToken: The fetched OAuth token.
        """
        if self._o_auth_token is not None and not self.is_token_expired(self._o_auth_token):
            return self._o_auth_token

        if self._o_auth_token_provider is not None:
            o_auth_token = self._o_auth_token_provider(self._o_auth_token, self)
            self._apply_on_token_update_callback(o_auth_token)
            return o_auth_token

        try:
            o_auth_token = self.fetch_token()
            self._apply_on_token_update_callback(o_auth_token)
            return o_auth_token
        except APIException:
            return self._o_auth_token

    def _apply_on_token_update_callback(self, o_auth_token):
        """ This function applies the OAuth token update callback provided by the user.
        """
        if self._o_auth_on_token_update is not None:
            self._o_auth_on_token_update(o_auth_token)


class ThingspaceOauthCredentials:

    @property
    def o_auth_client_id(self):
        return self._o_auth_client_id

    @property
    def o_auth_client_secret(self):
        return self._o_auth_client_secret

    @property
    def o_auth_token(self):
        return self._o_auth_token

    @property
    def o_auth_token_provider(self):
        return self._o_auth_token_provider

    @property
    def o_auth_on_token_update(self):
        return self._o_auth_on_token_update

    @property
    def o_auth_clock_skew(self):
        return self._o_auth_clock_skew

    def __init__(self, o_auth_client_id, o_auth_client_secret,
                 o_auth_token=None, o_auth_token_provider=None,
                 o_auth_on_token_update=None, o_auth_clock_skew=None):
        if o_auth_client_id is None:
            raise ValueError('o_auth_client_id cannot be None')
        if o_auth_client_secret is None:
            raise ValueError('o_auth_client_secret cannot be None')
        self._o_auth_client_id = o_auth_client_id
        self._o_auth_client_secret = o_auth_client_secret
        self._o_auth_token = o_auth_token
        self._o_auth_token_provider = o_auth_token_provider
        self._o_auth_on_token_update = o_auth_on_token_update
        self._o_auth_clock_skew = o_auth_clock_skew

    def clone_with(self, o_auth_client_id=None, o_auth_client_secret=None,
                   o_auth_token=None, o_auth_token_provider=None,
                   o_auth_on_token_update=None, o_auth_clock_skew=None):
        return ThingspaceOauthCredentials(
            o_auth_client_id or self.o_auth_client_id,
            o_auth_client_secret or self.o_auth_client_secret,
            o_auth_token or self.o_auth_token,
            o_auth_token_provider or self.o_auth_token_provider,
            o_auth_on_token_update or self.o_auth_on_token_update,
            o_auth_clock_skew or self.o_auth_clock_skew)