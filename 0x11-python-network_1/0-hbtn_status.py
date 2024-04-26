#!/usr/bin/python3
""" Script fetches https://alx-intranet.hbtn.io/status"""


from urllib.request import Request, urlopen
from urllib.error import URLError


def fetch_body():
    try:
        req = Request("https://alx-intranet.hbtn.io/status")
        with urlopen(req) as response:
            body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
    except URLError as e:
        if hasattr(e, 'reason'):
            print(e.reason)
        elif hasattr(e, 'code'):
            print(e.code)


if __name__ == "__main__":
    fetch_body()
