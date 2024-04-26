#!/usr/bin/python3
"""This script takes in a letter & sends a POST request to the URL"""


import requests
from sys import argv


def search_user(letter: str):
    """Sends a POST request to http://0.0.0.0:5000/search_user with a letter"""
    letter_data = {"q": letter}
    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url, data=letter_data)

    try:
        req_dict = req.json()
        if req_dict:
            print("[{}] {}".format(req_dict.get("id"), req_dict.get("name")))
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")


if __name__ == "__main__":
    try:
        letter = argv[1]
    except IndexError:
        letter = ""
    finally:
        search_user(letter)
