#!/usr/bin/python3
"""From json string module"""


def from_json_string(my_str):
    """Returns an object representes by a JSON string

        Args:
            my_str: JSON string
        Returns:
            The object represented by the JSON string
    """
    return json.loads(my_str)
