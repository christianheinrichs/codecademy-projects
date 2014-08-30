#!/usr/bin/env python2

# access_token can be used alone, while apiKey needs the login argument
# user/info endpoint for example doesn't work with apiKey at all.

import sys
from json import loads
from pprint import pprint
from urllib.parse import urlencode
from urllib.request import urlopen

# Set a minimum of API variables
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
API_KEY = "YOUR_API_KEY"
LOGIN = "YOUR_LOGIN"
LONGURL = "URL"
USE_PPRINT = False

# Check if the API variables are provided or not
if ACCESS_TOKEN == "" or API_KEY == "" or LOGIN == "" or LONGURL == "":
    print("Please fill out all parameters.")
    sys.exit(1)
else:
    pass

query_params = ({"access_token": ACCESS_TOKEN,
                "apiKey": API_KEY,
                "login": LOGIN,
                "longUrl": LONGURL})
query_params = urlencode(query_params)

url = "https://api-ssl.bitly.com/v3/"
endpoint = input("Please enter a bitly endpoint e.g. shorten: ")
url = url + endpoint

response = urlopen('%s?%s' % (url, query_params)).read().decode()

jsoncontent = loads(response)

# Decide whether to use print or pprint
if url == "https://api-ssl.bitly.com/v3/shorten":
    if USE_PPRINT == False:
        print("The shortened link of " + LONGURL + " is:")
        print(jsoncontent["data"]["url"])
    else:
        print("The shortened link of " + LONGURL + " is:")
        pprint(jsoncontent["data"]["url"])
else:
    if USE_PPRINT == False:
        print(jsoncontent)
    else:
        pprint(jsoncontent)
