#!/usr/bin/python3
'''script that takes in a URL, sends a request and displays the body of
If the HTTP status code is greater than or equal to 400, print error code
You are not allowed to import packages other than requests and sys
'''
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
