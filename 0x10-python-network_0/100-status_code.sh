#!/bin/bash
# Get the status code of a website
curl -sI "$1" | head -n 1 | cut -b 10-12
