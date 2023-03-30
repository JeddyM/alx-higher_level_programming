#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -s -I -X OPTIONS "$url" | grep "Allow:" | cut -d " " -f 2-
