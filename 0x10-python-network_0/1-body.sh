#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
if [ "$(curl -sI "$1":"$2" | head -n 1 | awk '{print $2}')" -eq "200" ]; then curl "$1":"$2"; fi
