#!/bin/bash
# Send variables with curl request
curl -sL "$1" -X POST -d "email: hr@holbertonschool.com" -d "subject: I will always be here for PLD"
