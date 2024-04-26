#!/usr/bin/python3
"""This script takes GitHub credentials and uses the API to display the id"""


import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def get_github_id(username: str, password: str):
    basic_auth = HTTPBasicAuth(username, password)
    url = "https://api.github.com/user"
    headers = {"Accept": "application/vnd.github.v3+json"}
    req = requests.get(url, headers=headers, auth=basic_auth)
    req_dict = req.json()

    print(req_dict.get("id"))


if __name__ == "__main__":
    get_github_id(argv[1], argv[2])
