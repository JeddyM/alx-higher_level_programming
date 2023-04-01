#!/usr/bin/python3
'''script that takes in a URL and an email, sends a POST request to the passed
URL with email as a parameter and displays the response body (decoded in utf-8)
'''
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': 'sys.argv[2]'}
    data = urllib.parse.urlencode(value).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
