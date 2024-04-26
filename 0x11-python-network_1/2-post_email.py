#!/usr/bin/python3
"""This script displays the body of the response of a POST request"""


from urllib.request import Request, urlopen
from urllib.error import URLError
from urllib.parse import urlencode
from sys import argv


def post_email(url: str, email: str):
    try:
        data = urlencode({"email": email})
        email_encode = data.encode("utf-8")
        req = Request(url, email_encode)
        with urlopen(req) as response:
            body = response.read()
        print(body.decode("utf-8"))
    except URLError as e:
        if hasattr(e, 'reason'):
            print(e.reason)
        elif hasattr(e, 'code'):
            print(e.code)


if __name__ == "__main__":
    post_email(argv[1], argv[2])
