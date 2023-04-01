#!/usr/bin/python3
'''Script that fetches https://alx-intranet.hbtn.io/status'''
import urllib.request


def main():
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as\
    webUrl:
        data = webUrl.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode('utf-8')))


if __name__ == "__main__":
    main()
