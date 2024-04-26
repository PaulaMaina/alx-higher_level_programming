#!/usr/bin/python3
"""This script displays the response body of an error code"""


from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv


def error_code(url: str):
    """This function displays the error code"""
    try:
        req = Request(url)
        with urlopen(req) as response:
            body = response.read()
        print(body.decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    error_code(argv[1])
