#!/usr/bin/python3
'''script that takes in a URL and an email, sends a POST request to the passed
URL with email as a parameter and displays the response body
You are not allowed to import packages other than requests and sys
'''
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    response = requests.post(url, data=value)
    print(response.text)
