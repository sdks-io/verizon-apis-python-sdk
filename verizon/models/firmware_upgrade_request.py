# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser


class FirmwareUpgradeRequest(object):

    """Implementation of the 'FirmwareUpgradeRequest' model.

    Details of the firmware upgrade request.

    Attributes:
        account_name (str): Account identifier in "##########-#####".
        firmware_name (str): The name of the firmware image that will be used
            for the upgrade, from a GET /firmware response.
        firmware_to (str): The name of the firmware version that will be on
            the devices after a successful upgrade.
        start_date (date): The date that the upgrade begins.
        end_date (date): The date that the upgrade ends.
        device_list (List[str]): The IMEIs of the devices.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "firmware_name": 'firmwareName',
        "firmware_to": 'firmwareTo',
        "start_date": 'startDate',
        "end_date": 'endDate',
        "device_list": 'deviceList'
    }

    def __init__(self,
                 account_name=None,
                 firmware_name=None,
                 firmware_to=None,
                 start_date=None,
                 end_date=None,
                 device_list=None):
        """Constructor for the FirmwareUpgradeRequest class"""

        # Initialize members of the class
        self.account_name = account_name 
        self.firmware_name = firmware_name 
        self.firmware_to = firmware_to 
        self.start_date = start_date 
        self.end_date = end_date 
        self.device_list = device_list 

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
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else None
        firmware_name = dictionary.get("firmwareName") if dictionary.get("firmwareName") else None
        firmware_to = dictionary.get("firmwareTo") if dictionary.get("firmwareTo") else None
        start_date = dateutil.parser.parse(dictionary.get('startDate')).date() if dictionary.get('startDate') else None
        end_date = dateutil.parser.parse(dictionary.get('endDate')).date() if dictionary.get('endDate') else None
        device_list = dictionary.get("deviceList") if dictionary.get("deviceList") else None
        # Return an object of this model
        return cls(account_name,
                   firmware_name,
                   firmware_to,
                   start_date,
                   end_date,
                   device_list)
