#!/bin/bash
# Get the status code of a website
curl -X GET -sLIw "%{http_code}" "$1" -o /dev/null
