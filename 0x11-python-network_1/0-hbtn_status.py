#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request


url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    html = response.read()
    print("Body response:")
    print("\t- type: " + str(type(html)))
    print("\t- content: " + str(html))
    print("\t- utf8 content: " + str(html.decode("utf-8")))
