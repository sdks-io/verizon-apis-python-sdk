# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class IErrorMessage(object):

    """Implementation of the 'IErrorMessage' model.

    Error message.

    Attributes:
        error_code (ErrorResponseCodeEnum): Error Code.
        error_message (str): Details and additional information about the
            error code.
        http_status_code (HttpStatusCodeEnum): HTML error code and description.
        detail_error_message (str): More detail and information about the HTML
            error code.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error_code": 'errorCode',
        "error_message": 'errorMessage',
        "http_status_code": 'httpStatusCode',
        "detail_error_message": 'detailErrorMessage'
    }

    _optionals = [
        'error_code',
        'error_message',
        'http_status_code',
        'detail_error_message',
    ]

    def __init__(self,
                 error_code=APIHelper.SKIP,
                 error_message=APIHelper.SKIP,
                 http_status_code=APIHelper.SKIP,
                 detail_error_message=APIHelper.SKIP):
        """Constructor for the IErrorMessage class"""

        # Initialize members of the class
        if error_code is not APIHelper.SKIP:
            self.error_code = error_code 
        if error_message is not APIHelper.SKIP:
            self.error_message = error_message 
        if http_status_code is not APIHelper.SKIP:
            self.http_status_code = http_status_code 
        if detail_error_message is not APIHelper.SKIP:
            self.detail_error_message = detail_error_message 

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
        error_code = dictionary.get("errorCode") if dictionary.get("errorCode") else APIHelper.SKIP
        error_message = dictionary.get("errorMessage") if dictionary.get("errorMessage") else APIHelper.SKIP
        http_status_code = dictionary.get("httpStatusCode") if dictionary.get("httpStatusCode") else APIHelper.SKIP
        detail_error_message = dictionary.get("detailErrorMessage") if dictionary.get("detailErrorMessage") else APIHelper.SKIP
        # Return an object of this model
        return cls(error_code,
                   error_message,
                   http_status_code,
                   detail_error_message)
