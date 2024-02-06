#!/usr/bin/python3
"""JSON string module"""
import json


def to_json_string(my_obj):
    """Returns the JSON string of an object

        Args:
            my_obj: object
        Returns:
            The JSON string of the object
    """
    return json.dumps(my_obj)
