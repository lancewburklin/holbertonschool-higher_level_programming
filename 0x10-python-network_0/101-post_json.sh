#!/bin/bash
# Posts a JSON file to a server
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
