#!/bin/bash
# Get the allowed options from a website
curl -X OPTIONS "$1" -si | grep Allow | cut -b 8-
