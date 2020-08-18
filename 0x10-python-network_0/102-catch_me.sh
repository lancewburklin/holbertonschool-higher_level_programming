#!/bin/bash
# Tracks down the body of the catch_me redirect
curl -sL "$1" -X PUT -d "user_id=98" -H "Origin: HolbertonSchool"
