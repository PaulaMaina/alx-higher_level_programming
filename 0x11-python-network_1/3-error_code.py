#!/usr/bin/python3
"""This script displays the response body of an error code"""


from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from sys import argv


def error_code(url: str):
    try:
        req = Request(url)
        with urlopen(req) as response:
            body = response.read()
        print(body.decode("uft-8"))
    except HTTPError as e:
        print("Error code: ", e.code)
    except URLError as e:
        print("Error reason: ", e.reason)


if __name__ == "__main__":
    error_code(argv[1])
