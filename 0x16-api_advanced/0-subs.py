#!/usr/bin/python3
"""
API
"""
import json
import requests


def number_of_subscribers(subreddit):

    h = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0)"
    e = "Gecko/20100101 Firefox/80.0"
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(
        url,
        headers={
            'User-Agent': h + e},
        allow_redirects=False).json()
    try:
        return (res["data"]["subscribers"])
    except BaseException:
        return(0)
