#!/bin/bash
# Send variables with curl request
curl "$1" -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
