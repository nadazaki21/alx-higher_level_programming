#!/usr/bin/python3
""" script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id """
import requests
import sys


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    # head = {'accept': 'application/vnd.github+json', }
    cred = requests.auth.HTTPBasicAuth(username, password)

    r = requests.get(f"https://api.github.com/users/{username}", auth=cred)
    print(r.json().get("id"))
