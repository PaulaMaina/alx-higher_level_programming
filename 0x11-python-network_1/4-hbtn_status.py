#!/usr/bin/python3
""" Script fetches https://alx-intranet.hbtn.io/status"""


import requests


def fetch_requests():
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))


if __name__ == "__main__":
    fetch_requests()
