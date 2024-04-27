#!/usr/bin/python3
import urllib.parse
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
   html = response.read()
   print ("- type: " + str(type(html)))
   print ("- content: " + str(html))
   print("- utf8 content: " + str(html.decode("utf-8")))
   
   
   
# user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
# values = {'name': 'Michael Foord',
#           'location': 'Northampton',
#           'language': 'Python' }
# headers = {'User-Agent': user_agent}

# data = urllib.parse.urlencode(values)
# data = data.encode('ascii')
# req = urllib.request.Request(url, data, headers)
# with urllib.request.urlopen(req) as response:
#    the_page = response.read()
#    print( the_page)