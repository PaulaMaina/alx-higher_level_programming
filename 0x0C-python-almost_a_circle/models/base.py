#!/usr/bin/python3
"""Base Class Definition"""
import json


class Base:
    """The base class that manages the id attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Assigns the id of an instance

            Args:
                id: ID of an instance
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of a list of dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
