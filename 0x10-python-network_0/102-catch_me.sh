#!/bin/bash
# Tracks down the body of the catch_me redirect
curl -sL 0.0.0.0:5000/catch_me -X PUT -d "user_id=98" -H "Origin: HolbertonSchool"
