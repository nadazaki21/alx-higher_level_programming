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
        
        if r.json() == r'{}':
            print("No result")

        print("{{}}")
        if r.json() == "{{}}":
            print("No result")
            
            

        
        
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")