#!/usr/bin/python3
"""
Some API stuff idk whatup
"""
import requests
import sys
# GET /repos/:owner/:repo/commits

if __name__ == "__main__":
    sess = requests.Session()
    owner = sys.argv[2]
    repo = sys.argv[1]
    comm = sess.get('https://api.github.com/repos/{}/{}/commits'.format(
        owner, repo))
    something = comm.json()[:10]
    for i in something:
        print(i['sha'] + ": " + i['commit']['author']['name'])
