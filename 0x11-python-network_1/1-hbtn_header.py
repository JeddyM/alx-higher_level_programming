#!/usr/bin/python3
'''Sends request and displays value of the X-Request-Id variable found in the
header response'''
import urllib.request
import sys


def main():
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))


if __name__ == "__main__":
    main()
