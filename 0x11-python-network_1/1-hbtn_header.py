#!/usr/bin/python3
""" This script displays the value of the X-Request-Id variable"""


from urllib.request import Request, urlopen
from urllib.error import URLError
from sys import argv


def response_header_value(url: str):
    try:
        req = Request(url)
        with urlopen(req) as response:
            body = response.read()
        print(response.info().get("X-Request-Id"))
    except URLError as e:
        if hasattr(e, 'reason'):
            print(e.reason)
        elif hasattr(e, 'code'):
            print(e.code)


if __name__ == "__main__":
    response_header_value(argv[1])
