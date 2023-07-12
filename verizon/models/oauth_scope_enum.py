# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class OauthScopeEnum(object):

    """Implementation of the 'OAuth Scope' enum.

    OAuth 2 scopes supported by the API

    Attributes:
        DISCOVERYREAD: Grant read-only access to discovery data
        SERVICEPROFILEREAD: Grant read-only access to service profile data
        SERVICEPROFILEWRITE: Grant write access to service profile data
        SERVICEREGISTRYREAD: Grant read-only access to Service registry data
        SERVICEREGISTRYWRITE: Grant write access to Service registry data
        TS.MEC.FULLACCESS: Full access for /serviceprofiles and
            /serviceendpoints.
        TS.MEC.LIMITACCESS: Limited access. Will not allow use of
            /serviceprofiles and /serviceendpoints but will allow discovery.
        TS.APPLICATION.RO: TODO: type description here.
        EDGEDISCOVERYREAD: TODO: type description here.
        EDGESERVICEPROFILEREAD: TODO: type description here.
        EDGESERVICEPROFILEWRITE: TODO: type description here.
        EDGESERVICEREGISTRYREAD: TODO: type description here.
        EDGESERVICEREGISTRYWRITE: TODO: type description here.
        READ: read access
        WRITE: read/write access

    """

    DISCOVERYREAD = 'discovery:read'

    SERVICEPROFILEREAD = 'serviceprofile:read'

    SERVICEPROFILEWRITE = 'serviceprofile:write'

    SERVICEREGISTRYREAD = 'serviceregistry:read'

    SERVICEREGISTRYWRITE = 'serviceregistry:write'

    TS_MEC_FULLACCESS = 'ts.mec.fullaccess'

    TS_MEC_LIMITACCESS = 'ts.mec.limitaccess'

    TS_APPLICATION_RO = 'ts.application.ro'

    EDGEDISCOVERYREAD = 'edge:discovery:read'

    EDGESERVICEPROFILEREAD = 'edge:serviceprofile:read'

    EDGESERVICEPROFILEWRITE = 'edge:serviceprofile:write'

    EDGESERVICEREGISTRYREAD = 'edge:serviceregistry:read'

    EDGESERVICEREGISTRYWRITE = 'edge:serviceregistry:write'

    READ = 'read'

    WRITE = 'write'
