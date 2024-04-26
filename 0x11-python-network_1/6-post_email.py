#!/usr/bin/python3
"""This script displays the body of the response of a POST request"""


import requests
from sys import argv


def request_email(url: str, email: str):
    data = urlencode({"email": email})
    email_encode = data.encode("utf-8")
    req = requests.get(url, email_encode)


if __name__ == "__main__":
    request_email(argv[1], argv[2])
