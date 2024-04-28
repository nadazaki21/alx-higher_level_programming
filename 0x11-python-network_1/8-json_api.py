#!/usr/bin/python3
"""  script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user
with the letter as a parameter. """
import requests
import sys


if __name__ == "__main__":

    payload = {"q": ""}
    if len(sys.argv) > 1:
        payload = {"q": sys.argv[1]}

    try:
        r = requests.post("http://0.0.0.0:5000/search_user", params=payload)
        r.json()  # if json decoding fails , it raises an exception
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
    except Exception:
        if r.status_code == 204:
            print("No result")
