#1/usr/bin/python3
"""Save to JSON module"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation

        Args:
            my_obj: the object
            filename: the name of the file
    """
    with open(filename, "w", encoding="uft-8") as f:
        f.write(json.dumps(my_obj))
