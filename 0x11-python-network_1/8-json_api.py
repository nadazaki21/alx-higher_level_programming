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
        r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

        if r.json() == {}:
            print("No result")

        else:
            print(f"[{r.json().get('id')}] {r.json().get('name')}")

    except Exception:
        print("Not a valid JSON")
