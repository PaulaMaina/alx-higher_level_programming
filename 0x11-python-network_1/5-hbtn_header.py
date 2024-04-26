#!/usr/bin/python3
""" This script displays the value of the X-Request-Id variable"""


import requests
from sys import argv


def get_header(url: str):
    try:
        req = requests.get(url)
            body = response.read()
        print(req.headers.get("X-Request-Id"))


if __name__ == "__main__":
    get_header(argv[1])
