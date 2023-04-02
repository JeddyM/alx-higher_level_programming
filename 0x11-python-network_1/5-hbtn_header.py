#!/usr/bin/python3
'''Sends request and displays value of the X-Request-Id variable found in the
header response import packages requests and sys ONLY'''
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
