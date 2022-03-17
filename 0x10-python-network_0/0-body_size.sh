#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI -o /dev/null -w "%{size_request}\n" "$1":"$2"
