#!/bin/bash
curl -sI -X OPTIONS $1 | grep Allow | awk '{print $2}'
