#!/usr/bin/python3
""" This script fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import Request, urlopen
from urllib.error import URLError


def fetch_body():
    try:
        req = Request("https://alx-intranet.hbtn.io/status")
        with urlopen(req) as response:
            html = response.read()
        print("Body response: ")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
    except URLError as e:
        if hasattr(e, 'reason'):
            print(e.reason)
        elif hasattr(e, 'code'):
            print(e.code)


if __name__ == "__main__":
    fetch_body()
