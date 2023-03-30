#!/bin/bash
# GET request with a value X-School-User-Id = 98, display the body response
curl -sH "X-School-User-Id:98" "$1"
