#!/bin/bash
# attempts to access redirect
curl -s 0.0.0.0:5000/catch_me -X PUT -d "found you"
