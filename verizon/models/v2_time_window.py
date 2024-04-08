# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class V2TimeWindow(object):

    """Implementation of the 'V2TimeWindow' model.

    Allowed start and end time windows.

    Attributes:
        start_time (int): Start hour in range [0..23], current hour >=
            startTime.
        end_time (int): End hour in range [1..24], current hour < endTime.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "start_time": 'startTime',
        "end_time": 'endTime'
    }

    def __init__(self,
                 start_time=None,
                 end_time=None):
        """Constructor for the V2TimeWindow class"""

        # Initialize members of the class
        self.start_time = start_time 
        self.end_time = end_time 

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
        start_time = dictionary.get("startTime") if dictionary.get("startTime") else None
        end_time = dictionary.get("endTime") if dictionary.get("endTime") else None
        # Return an object of this model
        return cls(start_time,
                   end_time)
