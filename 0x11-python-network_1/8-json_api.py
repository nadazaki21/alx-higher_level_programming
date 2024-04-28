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
    #print(payload)
    
    empty_dic = {}

    try:
        r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
        # print(r.status_code)
        # print(r.text)
        
        print('{}')
        print('{\}')
        print(r.text)
        if r.text == str(empty_dic):
            print(r.text)
            print('{}')
            print("No result")
        
        # if (r.status_code == 204):
        #     print("No result")
        r.json()
        
        
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
    except Exception:
        print("No result")