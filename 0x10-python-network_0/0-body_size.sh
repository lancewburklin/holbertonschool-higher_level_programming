#!/bin/bash
# This will get the length of content for a file
curl -sI $1| grep Content-Length | cut -b 17-18
