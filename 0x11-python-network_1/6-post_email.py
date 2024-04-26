#!/usr/bin/python3
"""This script displays the body of the response of a POST request"""


import requests
from sys import argv


def request_email(url: str, email: str):
    email_data = {"email": email}
    req = requests.post(url, data=email_data)
    print(req.text)


if __name__ == "__main__":
    request_email(argv[1], argv[2])
