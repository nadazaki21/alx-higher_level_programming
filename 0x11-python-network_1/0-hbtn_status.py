#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request


url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    html = response.read()
    print("Body response:")
    print("    - type: " + str(type(html)))
    print("    - content: " + str(html))
    print("    - utf8 content: " + str(html.decode("utf-8")))
