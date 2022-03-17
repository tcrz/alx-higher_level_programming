#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
if [ "$(curl -sI -o /dev/null -w "%{http_code}" "$1")" -eq "200" ]; then curl -s "$1"; fi
