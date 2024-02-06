#!/usr/bin/python3
"""Load from JSON file"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file

        Args:
            filename: The name of the file
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
