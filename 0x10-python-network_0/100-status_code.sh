#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -si -o /dev/null -w "%{http_code}\n" $1
