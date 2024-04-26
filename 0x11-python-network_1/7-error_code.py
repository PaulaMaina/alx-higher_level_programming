#!/usr/bin/python3
"""This script displays the response body of an error code"""


import requests
from sys import argv


def get_error_code(url: str):
    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)


if __name__ == "__main__":
    get_error_code(argv[1])
