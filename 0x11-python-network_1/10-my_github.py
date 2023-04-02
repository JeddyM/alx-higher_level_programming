#!/usr/bin/python3
'''script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
You must use Basic Authentication with a personal access token as password
to access to your information
First argument will be username second password
'''
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get(url, auth=auth)
    print(response.json().get("id"))
