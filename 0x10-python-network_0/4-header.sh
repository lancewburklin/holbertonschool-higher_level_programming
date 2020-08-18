#!/bin/bash
# Get the header information from a website
curl -sL "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
