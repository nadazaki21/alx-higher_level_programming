#!/usr/bin/python3
""" script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8) """
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    
    
    url = sys.argv[1]
    #values = {'email': sys.argv[2]}
    email = sys.argv[2]

    data = urllib.parse.urlencode(email)
    data = data.encode('ascii') # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
       the_page = response.read()
       print(the_page)
   
    # url = sys.argv[1]
    # email = sys.argv[2]

    # # Prepare POST data as a byte string with proper encoding
    # data = {"email": email}
    # data = urllib.parse.urlencode(data).encode("utf-8")
    # # Create a POST request with the data
    # req = urllib.request.Request(url, data)


    # with urllib.request.urlopen(req) as response:
    #     the_page = response.read().decode("utf-8")
    #     print(the_page)
