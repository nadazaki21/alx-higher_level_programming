#!/usr/bin/python3
""" list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails” """
import requests
import sys


if __name__ == "__main__":

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    head = {
        "accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    # cred = requests.auth.HTTPBasicAuth(username, password)

    r = requests.get(
        f"https://api.github.com/repos/{owner_name}/{repository_name}/commits",
        headers=head,
    )
    response = r.json()

    for i in range(10):

        # for item in response:
        sha = response[i].get("sha")
        name = response[i]["commit"]["author"]["name"]

        print(f"{sha}: {name}")
