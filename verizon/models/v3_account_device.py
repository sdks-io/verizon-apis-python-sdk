# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.v3_software_info import V3SoftwareInfo


class V3AccountDevice(object):

    """Implementation of the 'V3AccountDevice' model.

    Device information.

    Attributes:
        device_id (string): Device identifier.
        mdn (string): MDN.
        model (string): Device model.
        make (string): Device make.
        firmware (string): Device firmware version.
        fota_eligible (bool): Value=true if the device software can be
            upgraded over the air using the Software Management Services API.
        status (string): Device status.
        license_assigned (bool): License assigned device.
        protocol (string): Firmware protocol. Valid values include: LWM2M,
            OMADM, HTTP or NONE.
        software_list (list of V3SoftwareInfo): List of sofware.
        file_list (list of V3SoftwareInfo): List of files.
        create_time (string): The date and time of when the device is
            created.
        upgrade_time (string): The date and time of when the device firmware
            or software is updated.
        update_time (string): The date and time of when the device is
            updated.
        refresh_time (string): The date and time of when the device is
            refreshed.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_id": 'deviceId',
        "mdn": 'mdn',
        "model": 'model',
        "make": 'make',
        "firmware": 'firmware',
        "fota_eligible": 'fotaEligible',
        "status": 'status',
        "license_assigned": 'licenseAssigned',
        "protocol": 'protocol',
        "software_list": 'softwareList',
        "file_list": 'fileList',
        "create_time": 'createTime',
        "upgrade_time": 'upgradeTime',
        "update_time": 'updateTime',
        "refresh_time": 'refreshTime'
    }

    _optionals = [
        'file_list',
        'create_time',
        'upgrade_time',
        'update_time',
        'refresh_time',
    ]

    def __init__(self,
                 device_id=None,
                 mdn=None,
                 model=None,
                 make=None,
                 firmware=None,
                 fota_eligible=None,
                 status=None,
                 license_assigned=None,
                 protocol=None,
                 software_list=None,
                 file_list=APIHelper.SKIP,
                 create_time=APIHelper.SKIP,
                 upgrade_time=APIHelper.SKIP,
                 update_time=APIHelper.SKIP,
                 refresh_time=APIHelper.SKIP):
        """Constructor for the V3AccountDevice class"""

        # Initialize members of the class
        self.device_id = device_id 
        self.mdn = mdn 
        self.model = model 
        self.make = make 
        self.firmware = firmware 
        self.fota_eligible = fota_eligible 
        self.status = status 
        self.license_assigned = license_assigned 
        self.protocol = protocol 
        self.software_list = software_list 
        if file_list is not APIHelper.SKIP:
            self.file_list = file_list 
        if create_time is not APIHelper.SKIP:
            self.create_time = create_time 
        if upgrade_time is not APIHelper.SKIP:
            self.upgrade_time = upgrade_time 
        if update_time is not APIHelper.SKIP:
            self.update_time = update_time 
        if refresh_time is not APIHelper.SKIP:
            self.refresh_time = refresh_time 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        device_id = dictionary.get("deviceId") if dictionary.get("deviceId") else None
        mdn = dictionary.get("mdn") if dictionary.get("mdn") else None
        model = dictionary.get("model") if dictionary.get("model") else None
        make = dictionary.get("make") if dictionary.get("make") else None
        firmware = dictionary.get("firmware") if dictionary.get("firmware") else None
        fota_eligible = dictionary.get("fotaEligible") if "fotaEligible" in dictionary.keys() else None
        status = dictionary.get("status") if dictionary.get("status") else None
        license_assigned = dictionary.get("licenseAssigned") if "licenseAssigned" in dictionary.keys() else None
        protocol = dictionary.get("protocol") if dictionary.get("protocol") else None
        software_list = None
        if dictionary.get('softwareList') is not None:
            software_list = [V3SoftwareInfo.from_dictionary(x) for x in dictionary.get('softwareList')]
        file_list = None
        if dictionary.get('fileList') is not None:
            file_list = [V3SoftwareInfo.from_dictionary(x) for x in dictionary.get('fileList')]
        else:
            file_list = APIHelper.SKIP
        create_time = dictionary.get("createTime") if dictionary.get("createTime") else APIHelper.SKIP
        upgrade_time = dictionary.get("upgradeTime") if dictionary.get("upgradeTime") else APIHelper.SKIP
        update_time = dictionary.get("updateTime") if dictionary.get("updateTime") else APIHelper.SKIP
        refresh_time = dictionary.get("refreshTime") if dictionary.get("refreshTime") else APIHelper.SKIP
        # Return an object of this model
        return cls(device_id,
                   mdn,
                   model,
                   make,
                   firmware,
                   fota_eligible,
                   status,
                   license_assigned,
                   protocol,
                   software_list,
                   file_list,
                   create_time,
                   upgrade_time,
                   update_time,
                   refresh_time)
