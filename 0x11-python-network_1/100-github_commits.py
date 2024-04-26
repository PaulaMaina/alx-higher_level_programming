#!/usr/bin/python3
"""This script uses the GitHub API to display 10 commits"""


import requests
from sys import argv


def get_github_commits(repo: str, owner: str):
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    headers = {"Accept": "application/vnd.github.v3+json"}
    req = requests.get(url, headers=headers)

    commits_list = req.json()

    for commit in commits_list[:10]:
        name = commit.get("commit").get("author").get("name")
        sha = commit.get("sha")
        print("{}: {}".format(sha, name))


if __name__ == "__main__":
    get_github_commits(argv[1], argv[2])
