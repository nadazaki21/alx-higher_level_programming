#!/usr/bin/python3
""" script that takes in a URL, sends a request
to the URL and displays the value of the X-Request-Id
variable found in the header of the response. """
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    header_name = "X-Request-Id"

    with urllib.request.urlopen(url) as response:
        headers = response.headers
        if header_name in headers:
            print(headers.get(header_name))
