#!/usr/bin/python3
'''Script that fetches https://alx-intranet.hbtn.io/status
You are not allowed to import packages other than requests'''
import requests


def main():
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))


if __name__ == "__main__":
    main()
