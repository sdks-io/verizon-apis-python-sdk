# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class PositionData(object):

    """Implementation of the 'PositionData' model.

    Position data.

    Attributes:
        time (string): Time location obtained.
        utcoffset (string): UTC offset of time.
        x (string): X coordinate of location.
        y (string): Y coordinate of location.
        radius (string): Radius of the location in meters.
        qos (bool): Whether requested accurary is met or not.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "time": 'time',
        "utcoffset": 'utcoffset',
        "x": 'x',
        "y": 'y',
        "radius": 'radius',
        "qos": 'qos'
    }

    _optionals = [
        'time',
        'utcoffset',
        'x',
        'y',
        'radius',
        'qos',
    ]

    def __init__(self,
                 time=APIHelper.SKIP,
                 utcoffset=APIHelper.SKIP,
                 x=APIHelper.SKIP,
                 y=APIHelper.SKIP,
                 radius=APIHelper.SKIP,
                 qos=APIHelper.SKIP):
        """Constructor for the PositionData class"""

        # Initialize members of the class
        if time is not APIHelper.SKIP:
            self.time = time 
        if utcoffset is not APIHelper.SKIP:
            self.utcoffset = utcoffset 
        if x is not APIHelper.SKIP:
            self.x = x 
        if y is not APIHelper.SKIP:
            self.y = y 
        if radius is not APIHelper.SKIP:
            self.radius = radius 
        if qos is not APIHelper.SKIP:
            self.qos = qos 

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

        time = dictionary.get("time") if dictionary.get("time") else APIHelper.SKIP
        utcoffset = dictionary.get("utcoffset") if dictionary.get("utcoffset") else APIHelper.SKIP
        x = dictionary.get("x") if dictionary.get("x") else APIHelper.SKIP
        y = dictionary.get("y") if dictionary.get("y") else APIHelper.SKIP
        radius = dictionary.get("radius") if dictionary.get("radius") else APIHelper.SKIP
        qos = dictionary.get("qos") if "qos" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(time,
                   utcoffset,
                   x,
                   y,
                   radius,
                   qos)