#!/bin/bash
# Get the status code of a website
curl -X GET -sLIw "%{http_code}\n" 0.0.0.0:5000/nop -o /dev/null
