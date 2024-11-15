# -*- coding: utf-8 -*-

"""
verizonthingspacequalityofserviceapiendpoints

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.authentication.header_auth import HeaderAuth


class VzM2mSessionToken(HeaderAuth):

    @property
    def error_message(self):
        """Display error message on occurrence of authentication failure
        in VzM2mSessionToken

        """
        return "VzM2mSessionToken: VZ-M2M-Token is undefined."

    def __init__(self, vz_m_2_m_session_token_credentials):
        auth_params = {}
        if vz_m_2_m_session_token_credentials is not None \
                and vz_m_2_m_session_token_credentials.vz_m_2_m_token is not None:
            auth_params["VZ-M2M-Token"] = vz_m_2_m_session_token_credentials.vz_m_2_m_token
        super().__init__(auth_params=auth_params)


class VzM2mSessionTokenCredentials:

    @property
    def vz_m_2_m_token(self):
        return self._vz_m_2_m_token

    def __init__(self, vz_m_2_m_token):
        if vz_m_2_m_token is None:
            raise ValueError('vz_m_2_m_token cannot be None')
        self._vz_m_2_m_token = vz_m_2_m_token

    def clone_with(self, vz_m_2_m_token=None):
        return VzM2mSessionTokenCredentials(
            vz_m_2_m_token or self.vz_m_2_m_token)
