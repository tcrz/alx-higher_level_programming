#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

curl -sI "$1":"$2" | grep Content-Length | awk '{print $2}'
