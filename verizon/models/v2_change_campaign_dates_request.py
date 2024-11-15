# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from verizon.api_helper import APIHelper
from verizon.models.v2_time_window import V2TimeWindow


class V2ChangeCampaignDatesRequest(object):

    """Implementation of the 'V2ChangeCampaignDatesRequest' model.

    New dates and time windows.

    Attributes:
        start_date (date): Campaign start date.
        end_date (date): Campaign end date.
        download_after_date (date): Specifies starting date client should
            download package. If null, client will download as soon as
            possible.
        download_time_window_list (List[V2TimeWindow]): List of allowed
            download time windows. Removing of existing windows is not allowed.
        install_after_date (date): Client will install package after date. If
            null, client will install as soon as possible.
        install_time_window_list (List[V2TimeWindow]): List of allowed install
            time windows. Removing of existing windows is not allowed.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "start_date": 'startDate',
        "end_date": 'endDate',
        "download_after_date": 'downloadAfterDate',
        "download_time_window_list": 'downloadTimeWindowList',
        "install_after_date": 'installAfterDate',
        "install_time_window_list": 'installTimeWindowList'
    }

    _optionals = [
        'download_after_date',
        'download_time_window_list',
        'install_after_date',
        'install_time_window_list',
    ]

    def __init__(self,
                 start_date=None,
                 end_date=None,
                 download_after_date=APIHelper.SKIP,
                 download_time_window_list=APIHelper.SKIP,
                 install_after_date=APIHelper.SKIP,
                 install_time_window_list=APIHelper.SKIP):
        """Constructor for the V2ChangeCampaignDatesRequest class"""

        # Initialize members of the class
        self.start_date = start_date 
        self.end_date = end_date 
        if download_after_date is not APIHelper.SKIP:
            self.download_after_date = download_after_date 
        if download_time_window_list is not APIHelper.SKIP:
            self.download_time_window_list = download_time_window_list 
        if install_after_date is not APIHelper.SKIP:
            self.install_after_date = install_after_date 
        if install_time_window_list is not APIHelper.SKIP:
            self.install_time_window_list = install_time_window_list 

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
        start_date = dateutil.parser.parse(dictionary.get('startDate')).date() if dictionary.get('startDate') else None
        end_date = dateutil.parser.parse(dictionary.get('endDate')).date() if dictionary.get('endDate') else None
        download_after_date = dateutil.parser.parse(dictionary.get('downloadAfterDate')).date() if dictionary.get('downloadAfterDate') else APIHelper.SKIP
        download_time_window_list = None
        if dictionary.get('downloadTimeWindowList') is not None:
            download_time_window_list = [V2TimeWindow.from_dictionary(x) for x in dictionary.get('downloadTimeWindowList')]
        else:
            download_time_window_list = APIHelper.SKIP
        install_after_date = dateutil.parser.parse(dictionary.get('installAfterDate')).date() if dictionary.get('installAfterDate') else APIHelper.SKIP
        install_time_window_list = None
        if dictionary.get('installTimeWindowList') is not None:
            install_time_window_list = [V2TimeWindow.from_dictionary(x) for x in dictionary.get('installTimeWindowList')]
        else:
            install_time_window_list = APIHelper.SKIP
        # Return an object of this model
        return cls(start_date,
                   end_date,
                   download_after_date,
                   download_time_window_list,
                   install_after_date,
                   install_time_window_list)
