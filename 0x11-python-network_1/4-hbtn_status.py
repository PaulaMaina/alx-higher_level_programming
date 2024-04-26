#!/usr/bin/python3
""" Script fetches https://alx-intranet.hbtn.io/status"""


import requests
from urllib.error import URLError


def fetch_requests():
    try:
        req = requests.get("https://alx-intranet.hbtn.io/status")
        print("Body response:")
        print("\t- type: {}".format(type(req.text)))
        print("\t- content: {}".format(req.text))
    except URLError as e:
        if hasattr(e, 'reason'):
            print(e.reason)
        elif hasattr(e, 'code'):
            print(e.code)


if __name__ == "__main__":
    fetch_requests()
