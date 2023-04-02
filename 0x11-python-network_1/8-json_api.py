#!/usr/bin/python3
'''script that takes in a letter and sends a POST request to 
http://0.0.0.0:5000/search_user with the letter as a parameter.
Letter must be sent with variable q
If no argument is given, set q=""
If response body properly JSON formatted display [<id>] <name>
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You are not allowed to import packages other than requests and sys
'''
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    value = {'q': letter}
    response = requests.post(url, data=value)
    try:
        resjson = response.json()
        if resjson == {}:
            print("No result")
        else: 
            print("[{}] {}".format(resjson.get("id"), resjson.get("name")))
    except ValueError:
        print("Not a valid JSON")
