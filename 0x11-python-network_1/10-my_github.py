#!/usr/bin/python3
""" script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id """
import requests
import sys


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    head = {'accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'  }
    cred = requests.auth.HTTPBasicAuth(username, password)

    try:
        r = requests.get(f"https://api.github.com/user", auth=cred , headers=head)
        print(r.json().get("id"))
    except Exception:
        pass
