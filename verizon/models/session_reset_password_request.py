# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class SessionResetPasswordRequest(object):

    """Implementation of the 'SessionResetPasswordRequest' model.

    Request to a new, randomly generated password for the current username.

    Attributes:
        old_password (str): The current password for the username.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "old_password": 'oldPassword'
    }

    def __init__(self,
                 old_password=None):
        """Constructor for the SessionResetPasswordRequest class"""

        # Initialize members of the class
        self.old_password = old_password 

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
        old_password = dictionary.get("oldPassword") if dictionary.get("oldPassword") else None
        # Return an object of this model
        return cls(old_password)